import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/views/HomePage.vue";
function requireAuth(to, from, next) {
  const isAuthenticated = localStorage.getItem("token");
  if (isAuthenticated) {
    next();
  } else {
    next("/login");
  }
}
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/admin",
      name: "AdminPage",
      component: () => import("../views/AdminController.vue"),
      beforeEnter: requireAuth,
    },
    {
      path: "/start-new-quiz-page",
      name: "new-quiz-page",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/NewQuizPage.vue"),
    },
    {
      path: "/login",
      name: "Login",
      component: () => import("../views/LoginPage.vue"),
    },
    {
      path: "/questions",
      name: "questions",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/QuestionManager.vue"),
    },
    {
      path: "/score",
      name: "score",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/Score.vue"),
    },
  ],
});

export default router;
