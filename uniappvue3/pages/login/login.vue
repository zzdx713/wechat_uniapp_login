<template>
	<view class="login-container">
		<image src="/static/logo.png" mode="aspectFit" class="logo"></image>
		<button type="primary" open-type="getUserInfo" @getuserinfo="onLogin">微信登录</button>
	</view>
</template>

<script setup>
import { post } from '@/utils/request';
import { useUserStore } from '@/stores/useUserStore';
import { ref } from 'vue';

const userStore = useUserStore();

const onLogin = async () => {
	const code = await getWxCode();
	const res = await loginToOdoo(code);

	if (res && res.data) {
		const { token, user } = res.data;
		userStore.setToken(token);
		userStore.setUser(user);
		uni.switchTab({
			url: '/pages/index/index'
		});
	}
};

const getWxCode = () => {
	return new Promise((resolve, reject) => {
		uni.login({
			provider: 'weixin',
			success: (res) => {
				resolve(res.code);
			},
			fail: () => {
				uni.showToast({ title: '获取微信登录失败', icon: 'none' });
				reject();
			}
		});
	});
};

const loginToOdoo = (code) => {
	return post('/wechat/miniapp/login', {
		code: code
	});
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