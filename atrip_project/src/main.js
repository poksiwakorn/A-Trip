import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import axios from "axios";

Vue.config.productionTip = false

axios.defaults.withCredentials = false
axios.defaults.headers.post['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5000';
axios.defaults.headers.post['Access-Control-Allow-Methods'] = "GET,HEAD,PUT,PATCH,POST,DELETE";
axios.defaults.headers.post['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Origin, xxx";
axios.defaults.baseURL = 'http://computerengineering.3bbddns.com:34673/';

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
