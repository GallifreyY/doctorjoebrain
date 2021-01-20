import request from '@/utils/request'

export function getBasicInfo(id) {
    return request({
        url: '/device_and_client_info',
        method: 'get',
        params: { id: id }
    })
}
export function getLanguageInfo(data) {
    return request({
        url: '/get_language',
        method: 'post',
        params: { data: data }
    })
}
export function getDiagnosisInfo(id, index) {
    return request({
        url: '/diagnosis_info',
        method: 'get',
        params: {
            id: id,
            index: index
        }
    })

}
