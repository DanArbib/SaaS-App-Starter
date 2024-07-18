import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import { useAuthStore } from '@/store/auth';

const routes: Array<RouteRecordRaw> = [
  // Main site
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/Site/Main.vue'),
    meta: {
      title: import.meta.env.VITE_APP_SLOGAN,
    },
  },
  {
    path: '/auth',
    name: 'auth',
    component: () => import('@/views/Auth/Auth.vue'),
    meta: {
      title: 'Auth',
    },
  },
  {
    path: '/signin',
    name: 'signin',
    component: () => import('@/views/Auth/Signin.vue'),
    props: route => ({ email: route.query.email}),
    meta: {
      title: 'Sign In',
    },
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('@/views/Auth/Signup.vue'),
    props: route => ({ email: route.query.email}),
    meta: {
      title: 'Sign Up',
    },
  },
  {
    path: '/reset-password-request',
    name: 'resetPasswordRequest',
    component: () => import('@/views/Auth/ResetPassRequest.vue'),
    meta: {
      title: 'Reset Password',
    },
  },
  {
    path: '/reset-password',
    name: 'resetPassword',
    component: () => import('@/views/Auth/ResetPass.vue'),
    props: route => ({ token: route.query.t}),
    meta: {
      title: 'Reset Password',
    },
  },
  {
    path: '/handle-auth',
    name: 'handleAuth',
    component: () => import('@/views/Auth/handleAuth.vue'),
    props: route => ({ token: route.query.t}),
    meta: {
      title: 'Auth',
    },
  },
  // Application
  {
    path: '/app',
    name: 'app',
    component: () => import('@/views/Dashboard/Main.vue'),
    meta: {
      title: 'Dashboard',
      requiresAuth: true,
    },
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('@/views/Dashboard/Profile.vue'),
    meta: {
      title: 'My Profile',
      requiresAuth: true,
    },
  },
  {
    path: '/settings',
    name: 'settings',
    component: () => import('@/views/Dashboard/Settings.vue'),
    meta: {
      title: 'Settings',
      requiresAuth: true,
    },
  },
  {
    path: '/subscribe',
    name: 'subscribe',
    component: () => import('@/views/Dashboard/Subscribe.vue'),
    meta: {
      title: 'Subscribe',
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
  // Error
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
  scrollBehavior(to, __, savedPosition) {
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
  const appName = import.meta.env.VITE_APP_NAME || 'App';

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

  // Set the document title based on the route's meta title
  if (to.meta.title) {
    document.title = `${appName} - ${to.meta.title}`;
  } else {
    document.title = appName;
  }
});

export default router;
