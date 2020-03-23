import { login, logout, getInfo } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'

const state = {
    token: 'false',          //using cookies: getToken()
    name: '',
    roles: []
}

const mutations = {
    SET_TOKEN: (state, token) => {
        state.token = token
    },
    SET_NAME: (state, name) => {
        state.name = name
    },
    SET_ROLES: (state, roles) => {
        state.roles = roles
    }

}

const actions = {
    //login
    login({ commit }, userInfo) {
        const { userName, password } = userInfo;
        return new Promise((resolved, rejected) => {
            login({ userName: userName.trim(), password: password }).then(response => {
                const { data } = response
                commit('SET_TOKEN', data.token)
                if (data.token == 'true') { //验证通过
                    commit('SET_NAME', data.name)
                    commit('SET_ROLES', data.roles)
                }
                resolved()
            }).catch(error => {
                rejected(error)
            })

        })
    },

    logout({ commit, state }) {
        return new Promise((resolve, reject) => {
            logout().then(() => {
                commit('SET_TOKEN', 'false')
                commit('SET_NAME', '')
                commit('SET_ROLES', '')
                resolve()
            }).catch(error => {
                reject(error)
            })

        })
    }




}

export default {
    namespaced: true,
    state,
    mutations,
    actions
}
