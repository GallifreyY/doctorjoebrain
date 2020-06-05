import request from '@/utils/request'

export function getMatrix(){
    return request({
        url: '/matrix',
        method: 'get',
    })

}

export function submitData(data){
    return request({
        url: '/matrix/newData',
        method: 'post',
        data
    })
}