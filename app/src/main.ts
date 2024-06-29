import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './assets/index.css'
import App from './App.vue'
import axios from 'axios'
import router from '@/router'

// Base URL for Axios requests
axios.defaults.baseURL = 'http://localhost:5000';

createApp(App)
  .use(router)
  .use(createPinia())
  .mount('#app');
