import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/test',
      name: 'testComponent',
      component: () => import('@/components/Test')
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

