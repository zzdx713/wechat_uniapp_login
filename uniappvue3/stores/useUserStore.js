import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
	state: () => ({
		token: uni.getStorageSync('token') || null,
		user: uni.getStorageSync('user') || null,
	}),
	actions: {
		setToken(token) {
			this.token = token;
			uni.setStorageSync('token', token);
		},
		setUser(user) {
			this.user = user;
			uni.setStorageSync('user', user);
		},
		clearAuth() {
			this.token = null;
			this.user = null;
			uni.removeStorageSync('token');
			uni.removeStorageSync('user');
		}
	}
});