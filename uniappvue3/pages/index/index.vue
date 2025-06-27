<template>
	<view class="index-container">
		<user-card :user="user" />
		<button @click="logout">退出登录</button>
	</view>
</template>

<script setup>
import UserCard from '@/components/user-card.vue';
import { useUserStore } from '@/stores/useUserStore';

const userStore = useUserStore();
const user = userStore.user;

const logout = () => {
	userStore.clearAuth();
	uni.reLaunch({
		url: '/pages/login/login'
	});
};
</script>

<style scoped>
.index-container {
	padding: 40rpx;
}
</style>