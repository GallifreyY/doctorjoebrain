import request from '@/utils/request'

export function getMatrix(){
    return request({
        url: '/matrix',
        method: 'get',
    })

}