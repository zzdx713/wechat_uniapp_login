<template>
	<view class="index-container">
		<user-card :user="user" />
		<button @click="logout">退出登录</button>
	</view>
</template>

<script>
import UserCard from '@/components/user-card.vue';
import { mapState, mapMutations } from 'vuex';

export default {
	components: { UserCard },
	computed: {
		...mapState(['user'])
	},
	methods: {
		...mapMutations(['SET_TOKEN', 'SET_USER']),
		logout() {
			this.SET_TOKEN(null);
			this.SET_USER(null);
			uni.reLaunch({
				url: '/pages/login/login'
			});
		}
	}
};
</script>

<style scoped>
.index-container {
	padding: 40rpx;
}
</style>