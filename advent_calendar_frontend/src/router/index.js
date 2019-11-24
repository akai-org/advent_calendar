import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Task from '../views/Task.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/task/:id',
    name: 'task',
    component: Task,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
