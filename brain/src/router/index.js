import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/test',
      name: 'testComponent',
      component: () => import('@/components/DeviceTable')
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

