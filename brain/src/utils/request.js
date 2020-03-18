import axios from 'axios'
// import store from '@/store'

// create an axios instance
const service = axios.create({
    baseURL: 'http://127.0.0.1:5000', //process.env.VUE_APP_BASE_API + request_url
    timeout: 5000
})

//console.log(process.env.VUE_APP_BASE_API) 为什么取不到

// response interceptor
service.interceptors.response.use(
    response => {
        const res = response.data
        if(res.code !== 20022){   //just an example
            console.log("InValid response code!")
            return Promise.reject(new Error(res.message || 'Error'))
        }else{
            return res;
        }


    },
    err => {
        console.log('err' + error)
        return Promise.reject(error)
    }
)
export default service