import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/test1',
      name: 'testComponent',
      component: () => import('@/components/NavBar')
    },
    {
      path: '/test2',
      component: () => import('@/components/TopBar')
    },
    {
      path: '/',
      component: () => import('@/views/HomePage')
    },
    {
      path: '/Device-Matrix',
      component: () => import('@/views/DeviceMatrix')
    }
    


  ]
})

