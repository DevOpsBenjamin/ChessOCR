import { createRouter, createWebHistory } from 'vue-router';
import SignIn from './components/SignIn.vue';
import SignUp from './components/SignUp.vue';

const Home = { template: '<div class="p-4">Welcome to ChessOCR</div>' };

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/signin', component: SignIn },
    { path: '/signup', component: SignUp }
  ]
});
