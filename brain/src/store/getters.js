const getters = {
    name: state => state.user.name,
    token: state => state.user.token,
    roles: state => state.user.roles,
    uuid: state => state.uuid.uuid
}
export default getters