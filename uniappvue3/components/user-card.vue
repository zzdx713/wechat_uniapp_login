<template>
	<view class="user-card">
		<image :src="user.avatarUrl" mode="aspectFill" class="avatar"></image>
		<text class="username">{{ user.name }}</text>
		<text class="mobile">{{ user.mobile }}</text>
	</view>
</template>

<script setup>
defineProps({
	user: {
		type: Object,
		default: () => ({})
	}
});
</script>

<style scoped>
.user-card {
	background-color: #f5f5f5;
	border-radius: 16rpx;
	padding: 40rpx;
	text-align: center;
	margin-bottom: 40rpx;
}

.avatar {
	width: 160rpx;
	height: 160rpx;
	border-radius: 80rpx;
	margin-bottom: 20rpx;
}

.username {
	font-size: 36rpx;
	font-weight: bold;
	color: #333;
	display: block;
	margin-bottom: 10rpx;
}

.mobile {
	font-size: 28rpx;
	color: #999;
}
</style>