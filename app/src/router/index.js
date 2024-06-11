import { createRouter, createWebHistory } from 'vue-router'
import store from '../store';
import MainView from '../views/main/MainView.vue'
import AuthView from '../views/auth/AuthView.vue'
import HandleAuth from '../views/auth/HandleAuth.vue'
import Login from '../views/auth/Login.vue'
import EmailSent from '../views/auth/EmailSent.vue'
import ResetSent from '../views/auth/ResetSent.vue'
import ResetPassword from '../views/auth/ResetPassword.vue'
import Signup from '../views/auth/Signup.vue'
import ResendEmail from '../views/auth/ResendEmail.vue'

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView,
    meta: { requiresAuth: true },
  },
  {
    path: '/auth',
    name: 'auth',
    component: AuthView
  },
  {
    path: '/handle-auth',
    name: 'HandleAuth',
    component: HandleAuth
  },
  {
    path: '/login:email?',
    name: 'login',
    component: Login
  },
  {
    path: '/signup/:email?',
    name: 'signup',
    component: Signup,
  },
  {
    path: '/verification',
    name: 'verification',
    component: EmailSent,
  },
  {
    path: '/reset-message',
    name: 'reset',
    component: ResetSent,
  },
  {
    path: '/reset-password',
    name: 'resetPassword',
    component: ResetPassword,
  },
  {
    path: '/resend',
    name: 'resend',
    component: ResendEmail,
  },
  {
    path: '/logout',
    name: 'logout',
    beforeEnter: (to, from, next) => {
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    },
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach(async (to, from, next) => {

  if (to.matched.some(record => record.meta.requiresAuth)) {
    await store.dispatch('getUserInfo');

    if (!store.getters['isAuthenticated']) {
      next({ name: 'auth' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router
