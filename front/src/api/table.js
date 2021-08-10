import request from "@/utils/request";

// api创建使用例子
export function getList(params) {
  return request({
    url: "/test",
    method: "get",
    params
  });
}
