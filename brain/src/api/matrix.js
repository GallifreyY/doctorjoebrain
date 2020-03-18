import request from '@/utils/request'

export function fetchMatrix(){
    return request({
        url: '/matrix',
        method: 'get',
    })

}