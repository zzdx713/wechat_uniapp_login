import { createApp } from 'vue';
import { createStore } from 'vuex';
import { createPinia, PiniaVuePlugin } from 'pinia';
import App from './App.vue';

// 创建 Pinia
const pinia = createPinia();
const app = createApp(App);

// 挂载 Pinia
app.use(pinia);
app.mount('#app');