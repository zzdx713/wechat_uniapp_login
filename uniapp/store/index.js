import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		token: uni.getStorageSync('token') || null,
		user: uni.getStorageSync('user') || null
	},
	mutations: {
		SET_TOKEN(state, token) {
			state.token = token;
			uni.setStorageSync('token', token);
		},
		SET_USER(state, user) {
			state.user = user;
			uni.setStorageSync('user', user);
		}
	},
	actions: {}
});