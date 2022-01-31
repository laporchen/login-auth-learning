import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            user: null,

        }
    },
    getters: {
        user: (state) => {
            return state.login
        }
    },
    actions: {
        user(context, user) {
            context.commit('user', user)
        }
    },
    mutations: {
        user(state, user) {
            state.login = user;
        },
    }
});

export default store;