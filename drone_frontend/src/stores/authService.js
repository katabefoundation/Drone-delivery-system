// import { api } from "boot/axios";

import { LocalStorage } from "quasar"

// const state = {
//   user: null,
//   isAuthenticated: false
// };

// const mutations = {
//   setUser(state, user) {
//     state.user = user;
//     state.isAuthenticated = true;
//   },
//   clearUser(state) {
//     state.user = null;
//     state.isAuthenticated = false;
//   },
// };

// const actions = {
//   async login({ commit }, credentails) {
//     try {
//       const response = await api.post('login/', credentails);
//       const user = response.data.user;
//       commit('setUser', user);
//       return user;
//     } catch (error) {
//       throw new Error(error.response.data.error);
//     }
//   },

//   async logout({ commit }) {
//     try {
//       await api.post('logout/');
//       commit('clearUser');
//     } catch (error) {
//       throw new Error(error.response.data.error);
//     }
//   },

//   async fetchUser({ commit }) {
//     try {
//       const response = await api.get('user/');
//       const user = response.data.user;
//       commit('setUser', user)
//     } catch (error) {
//       throw new Error(error.response.data.error);
//     }
//   }
// };

// const getters = {
//   user: (state) => state.user ,
//   isAuthenticated:(state)=> state.isAuthenticated,
// }

// export default {
//   state,
//   mutations,
//   actions,
//   getters
// }

const TOKEN_KEY = 'auth_token'
export function setAuthToken(token) {
  LocalStorage.set(TOKEN_KEY, token);
}

export function getAuthToken() {
  return LocalStorage.getItem(TOKEN_KEY);
}

export function removeAuthToken() {
  LocalStorage.remove(TOKEN_KEY);
}
