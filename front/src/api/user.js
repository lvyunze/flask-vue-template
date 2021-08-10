import request from "@/utils/request";

// 登录接口
export function login(data) {
  return request({
    url: "/login",
    method: "post",
    data
  });
}

// 获取取用户信息接口
export function getInfo() {
  return request({
    url: "/protected",
    method: "get"
  });
}

// 登出接口
export function logout() {
  return request({
    url: "/logout",
    method: "post"
  });
}

