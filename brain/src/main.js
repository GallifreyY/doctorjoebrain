// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.


import '@/style/index.scss' //global scss
import 'babel-polyfill'
98120127
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ViewUI from 'view-design'
import 'view-design/dist/styles/iview.css';

Vue.config.productionTip = false
Vue.use(ViewUI)

import axios from 'axios'
Vue.prototype.$axios = axios
axios.defaults.baseURL = '/api'  //important!src/main.js
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
