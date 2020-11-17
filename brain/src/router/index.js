import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/test',
      name: 'testComponent',
      component: () => import('@/components/DownloadButton')
    },
    {
      path: '/',
      component: () => import('@/views/HomePage')
    },

    {
      path: '/diagnosis/:id', //path:'/:id'  后面再组件中可以由 this.$route.params.id 取到
      component: () => import('@/views/UserReport')
    },
    {
      path: '/Device-Matrix',
      component: () => import('@/views/DeviceMatrix')
    },
    {
      path: '/Log-in',
      component: () => import('@/views/Login')
    },
    {
      path: '/modify',
      component: () => import('@/views/Modify')
    },
    {
      path: '/help',
      component: () => import('@/views/Help')
    },
    {
      path: '/step',
      component: () => import('@/views/Step')
    },
    {
      path: '/options',
      component: () => import('@/views/Options')
    },
    {
      path: '/tips',
      component: () => import('@/views/Tips')
    },
    {
      path: '/installstep',
      component: () => import('@/views/InstallStep')
    },
    {
      path: '/userlogin',
      component: () => import('@/views/UserLogin')
    },
    {
      path: '/userprocess',
      component: () => import('@/views/UserProcess')
    },
    {
      path: '/usermatrix',
      component: () => import('@/views/UserMatrix')
    },
  ]
})

