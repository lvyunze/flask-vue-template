import request from "@/utils/request";

// 评论demo数据接口
export function demo(data) {
  return request({
    url: "/demo",
    params: data,
    method: "get"
  });
}