import Vue from 'vue';
import store from './store';
import App from './App';

const app = new Vue({
	store,
	render: h => h(App)
});

app.$mount();