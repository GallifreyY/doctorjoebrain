import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/test',
      name: 'testComponent',
      component: () => import('@/components/DeviceCard')
    },
    {
      path: '/', 
      component: () => import('@/views/HomePage')
    },

    {
      path: '/diagnosis/:id', //path:'/:id'  后面再组件中可以由 this.$route.params.id 取到
      component: () => import('@/views/Report')
    },
    {
      path: '/Device-Matrix',
      component: () => import('@/views/DeviceMatrix')
    },
    {
      path: '/Log-in',
      component: () => import('@/views/Login')
    }
    
  ]
})

