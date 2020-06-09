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

export function deleteData(data){
    return request({
        url: '/matrix/deletedData',
        method:'post',
        data

    })
}

export function editData(data){
    return request({
        url:'/matrix/editedData',
        method:'post',
        data
    })

}