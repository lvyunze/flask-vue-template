import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

/* Layout */
import Layout from "@/layout";

export const constantRoutes = [
  {
    path: "/login",
    component: () => import("@/views/login/index"),
    hidden: true
  },

  {
    path: "/404",
    component: () => import("@/views/404"),
    hidden: true
  },

  {
    path: "/",
    component: Layout,
    // redirect: "/dashboard",
    meta: { title: "dashboard", icon: "dashboard" },
    children: [
      {
        path: "board",
        // name: "Dashboard",
        component: () => import("@/views/demo/index"),
        meta: { title: "dashboard_children", icon: "table" }
      }
    ]
  },

  {
    path: "/page_demo",
    component: Layout,
    name: "",
    meta: { title: "page_demo", icon: "example" },
    children: [
      {
        path: "table",
        name: "Table",
        component: () => import("@/views/page_demo/index"),
        meta: { title: "page_one", icon: "table" }
      }
    ]
  },

  // 404 page must be placed at the end !!!
  { path: "*", redirect: "/404", hidden: true }
];

const createRouter = () =>
  new Router({
    // mode: 'history', // require service support
    scrollBehavior: () => ({ y: 0 }),
    routes: constantRoutes
  });

const router = createRouter();

export function resetRouter() {
  const newRouter = createRouter();
  router.matcher = newRouter.matcher; // reset router
}

export default router;
