import { createStore } from 'vuex'
import axios from 'axios'
const store = createStore({
    state() {
        return {
            user: null,
            todoList: [],
            requestSuccess: false,
        }
    },
    getters: {
        user: (state) => {
            return state.login
        },
        todoList: (state) => {
            return state.todoList
        },
        requestSuccess: (state) => {
            return state.requestSuccess
        }
    },
    actions: {
        user(context, user) {
            context.commit('user', user)
        },
        todoList(context, todoList) {
            context.commit('todoList', todoList)
        },
        updateTodoList(context, todoList) {
            context.commit('updateTodoList', todoList)
        },
    },
    mutations: {
        user(state, user) {
            state.login = user;
        },
        todoList(state, todoList) {
            state.todoList = todoList;
        },
        async updateTodoList(state, todoList) {
            state.todoList = todoList;
            const response = await axios.post("/update", state.todoList);
            console.log(response)
            if (response.data.success === 200) {
                state.requestSuccess = true;
            } else {
                state.requestSuccess = false;
            }
        },
    }
});

export default store;