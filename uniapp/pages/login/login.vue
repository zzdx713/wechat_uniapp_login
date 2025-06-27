<template>
	<view class="login-container">
		<image src="/static/logo.png" mode="aspectFit" class="logo"></image>
		<button type="primary" open-type="getUserInfo" @getuserinfo="onLogin">微信登录</button>
	</view>
</template>

<script>
import { post } from '@/utils/request';
import { mapMutations } from 'vuex';

export default {
	data() {
		return {
			isLogining: false
		};
	},
	methods: {
		...mapMutations(['SET_TOKEN', 'SET_USER']),
		async onLogin(e) {
			if (this.isLogining) return;
			this.isLogining = true;

			try {
				const code = await this.getWxCode();
				const res = await this.loginToOdoo(code);

				console.log("【DEBUG】登录接口响应:", res);

				if (res && res.code === 200) {
					const { token, partner_id, name } = res;
					this.SET_TOKEN(token);
					this.SET_USER({ id: partner_id, name });

					uni.switchTab({
						url: '/pages/index/index'
					});
				} else {
					uni.showToast({ title: res.message || '登录失败', icon: 'none' });
				}
			} catch (err) {
				console.error('【ERROR】登录异常:', err);
				uni.showToast({ title: '登录失败，请重试', icon: 'none' });
			} finally {
				this.isLogining = false;
			}
		},
		getWxCode() {
			return new Promise((resolve, reject) => {
				uni.login({
					provider: 'weixin',
					success: (res) => {
						if (res.code) {
							console.log('✅ 获取到 code:', res.code);
							resolve(res.code);
						} else {
							console.error('❌ 获取 code 失败:', res);
							reject('获取 code 失败');
						}
					},
					fail: (err) => {
						console.error('❌ uni.login 失败:', err);
						uni.showToast({ title: '微信登录失败', icon: 'none' });
						reject(err);
					}
				});
			});
		},
		loginToOdoo(code) {
			return post('/wechat/miniapp/login', {
				code: code
			});
		}
	}
};
</script>

<style scoped>
.login-container {
	padding: 40rpx;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	height: 100vh;
}

.logo {
	width: 300rpx;
	height: 300rpx;
	margin-bottom: 60rpx;
}
</style>