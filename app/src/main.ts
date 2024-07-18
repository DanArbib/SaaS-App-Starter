import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './assets/index.css'
import App from './App.vue'
import axios from 'axios'
import router from '@/router'

// Set Axios base URL from environment variable
axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL;

createApp(App)
  .use(router)
  .use(createPinia())
  .mount('#app');