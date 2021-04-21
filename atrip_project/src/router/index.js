import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignIn from '../views/SignIn.vue'
import Register from '../views/Register.vue'
import AllPlan from '../views/AllPlan.vue'
import YourPlan from '../views/YourPlan.vue'
import Account from '../views/Account.vue'
import Landing from '../views/Landing.vue'
import About from '../views/About.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/Home',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/SignIn',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/Register',
    name: 'Register',
    component: Register
  },
  {
    path: '/AllPlan',
    name: 'AllPlan',
    component: AllPlan
  },
  {
    path: '/YourPlan',
    name: 'YourPlan',
    component: YourPlan
  },
  {
    path: '/Account',
    name: 'Account',
    component: Account
  },
  {
    path: '/',
    name: 'Landing',
    component: Landing
  }
]

const router = new VueRouter({
  routes
})

export default router
