const state = {
    uuid: "0"
}

const mutations = {
    SET_UUID: (state,uuid) => {
        state.uuid = uuid
    }
}

const actions = {
    identify({commit}, uuid){
        commit('SET_UUID',uuid)
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    actions
}
