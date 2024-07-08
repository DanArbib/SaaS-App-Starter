import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import { useAuthStore } from '@/store/auth';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/Site/Main.vue'),
    meta: {
      title: 'home',
    },
  },
  {
    path: '/auth',
    name: 'auth',
    component: () => import('@/views/Auth/Auth.vue'),
    meta: {
      title: 'auth',
    },
  },
  {
    path: '/signin',
    name: 'signin',
    component: () => import('@/views/Auth/Signin.vue'),
    props: route => ({ email: route.query.email}),
    meta: {
      title: 'signin',
    },
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('@/views/Auth/Signup.vue'),
    props: route => ({ email: route.query.email}),
    meta: {
      title: 'signup',
    },
  },
  {
    path: '/reset-password-request',
    name: 'resetPasswordRequest',
    component: () => import('@/views/Auth/ResetPassRequest.vue'),
    meta: {
      title: 'reset-password-request',
    },
  },
  {
    path: '/reset-password',
    name: 'resetPassword',
    component: () => import('@/views/Auth/ResetPass.vue'),
    props: route => ({ token: route.query.t}),
    meta: {
      title: 'reset-password',
    },
  },
  {
    path: '/handle-auth',
    name: 'handleAuth',
    component: () => import('@/views/Auth/handleAuth.vue'),
    props: route => ({ token: route.query.t}),
    meta: {
      title: 'handleAuth',
    },
  },
  {
    path: '/app',
    name: 'app',
    component: () => import('@/views/Dashboard/Main.vue'),
    meta: {
      title: 'app',
      requiresAuth: true,
    },
  },
  {
    path: '/logout',
    name: 'Logout',
    component: {
      beforeRouteEnter(_, __, next) {
        localStorage.removeItem('accessToken');
        next('/signin');
      }
    }
  },
  {
    path: '/403',
    name: '403',
    component: () => import('@/views/Error/403/index.vue'),
    meta: {
      title: '403',
    },
  },
  {
    path: '/404',
    name: '404',
    component: () => import('@/views/Error/404/index.vue'),
    meta: {
      title: '404',
    },
  },
  {
    path: '/500',
    name: '500',
    component: () => import('@/views/Error/500/index.vue'),
    meta: {
      title: '500',
    },
  },
  {
    path: '/:pathMatch(.*)*',
    component: () => import('@/views/Error/404/index.vue'),
    name: '404',
    meta: {
      title: '404',
    },
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return { ...savedPosition, behavior: 'smooth' };
    } else if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      };
    } else {
      return { left: 0, top: 0, behavior: 'smooth' };
    }
  },
});

router.beforeEach(async (to, __, next) => {
  const authStore = useAuthStore();

  if (to.matched.some(record => record.meta.requiresAuth)) {
    await authStore.getUserInfo();

    if (!authStore.isUserAuthenticated) {
      next({ name: 'signin' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
