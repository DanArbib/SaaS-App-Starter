import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios';
import './assets/style.css';

axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;

const app = createApp(App);
app.use(store);
app.use(router);
app.mount('#app');
