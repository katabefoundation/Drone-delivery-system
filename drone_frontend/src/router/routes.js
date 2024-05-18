import { createRouter, createWebHistory } from "vue-router";
import api from "axios";
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      {path:'login',component:()=>import('components/LoginView.vue')}
    ]
  },

  {
    path: '/user/',
    component: () => import('layouts/UserLayout.vue'),
    children: [
      { path: 'dashboard', component: () => import('pages/user/IndexPage.vue') },
      { path: 'notification', component: () => import('pages/user/NotificationPage.vue') },
      { path: 'history', component: () => import('pages/user/HistoryPage.vue') },
      { path: 'edit_profile', component: () => import('pages/user/ProfilePage.vue') },
      { path: 'policy', component: () => import('pages/user/PrivacyPage.vue') },
      { path: 'help',component: () => import('pages/user/DroneRequest.vue') }
    ]
  },
  {
    path: '/admin/',
    component: () => import('layouts/AdminLayout.vue'),
    children : [
      { path: 'dashboard', component: () => import('pages/admin/IndexPage.vue') },
      { path: 'user_management', component: () => import('pages/admin/UserManage.vue') },
      { path: 'drone_management', component: () => import('pages/admin/DroneManage.vue') },
      { path: 'notification', component: () => import('pages/admin/NotifyHistory.vue') },
      { path: 'policy', component: () => import('pages/user/PrivacyPage.vue') },
      { path: 'configuration', component: () => import('pages/admin/ConfigurationPage.vue') },
      { path: 'analysis', component: () => import('pages/admin/ReportAnalysis.vue') },
      { path: 'edit_profile', component: () => import('pages/admin/ProfilePage.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

const router = createRouter({
  history:api,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireAuth)) {
    api.get('user/')
      .then(response => {
        next();
      })
      .catch(error => {
      // user is not authenticated
      next('login/')
    })
  } else {
    next();
  }
})

export default routes
