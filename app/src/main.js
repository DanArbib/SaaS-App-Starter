import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/style.css';
import './index.css'
// import '../node_modules/flowbite-vue/dist/index.css'

const app = createApp(App);
app.use(store);
app.use(router);
app.mount('#app');
