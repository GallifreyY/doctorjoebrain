import request from '@/utils/request'

export function login(data){
    return request({
        url:'/user/login',
        method:'post',
        data
    })
}
export function modifyPassword(data){
    return request({
        url:'/reg',
        method:'post',
        data
    })
}
export function trsPassword(data){
    return request({
        url:'/result',
        method:'get',
        data
    })
}
export function getInfo(token) {
    return request({
      url: '/user/info',
      method: 'get',
      params: { token }
    })
  }


export function logout() {
    return request({
      url: '/user/logout',
      method: 'post'
    })
  }

