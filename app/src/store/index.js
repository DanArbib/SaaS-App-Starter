import { createStore } from 'vuex'
import authModule from './authModule';

export default createStore({
  state: {
    toggle: window.innerWidth > 768,
  },
  getters: {
  },
  mutations: {
    toggleSidebar(state) {
      state.toggle = !state.toggle;
    },
    updatePublicData(state, payload) {
      state.publicData = { ...state.publicData, ...payload };
    },
    updateSettingsData(state, payload) {
      state.settingsData = { ...state.settingsData, ...payload };
    },
  },
  actions: {
    updatePublicData({ commit }, payload) {
      commit('updatePublicData', payload);
    },
    updateSettingsData({ commit }, payload) {
      commit('updateSettingsData', payload);
    },
  },
  modules: {
    auth: authModule,
  }
})


