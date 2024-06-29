import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

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
    path: '/app',
    name: 'app',
    component: () => import('@/views/Dashboard/Main.vue'),
    meta: {
      title: 'app',
    },
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
    return savedPosition || { left: 0, top: 0 }
  }
});

export default router;
