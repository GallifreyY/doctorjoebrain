import request from '@/utils/request'

export function getDeviceInfo(){
    return request({
        url :'/device_info',
        method: 'get'
    }) 
}

export function getClientInfo(){
    return request({
        url : '/client_info',
        method:'get'
    })

}

export function getDiagnosisInfo(){  
    return request({
        url : '/diagnosis_info',
        method:'get'
    })

}