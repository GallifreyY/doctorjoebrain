import request from '@/utils/request'

export function getBasicInfo(id){
    return request({
        url :'/device_and_client_info',
        method: 'get',
        params:{id:id}
    }) 
}

export function getDiagnosisInfo(id){  
    return request({
        url : '/diagnosis_info',
        method:'get',
        params:{id:id}
    })

}