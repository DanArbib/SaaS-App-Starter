import axios from 'axios';

const state = {
  isAuthenticated: false,
  userData: null,
  loading: false,
};

const getters = {
  isAuthenticated: state => state.isAuthenticated,
  userData: state => state.userData,
};

const mutations = {
  SET_AUTHENTICATED(state, isAuthenticated) {
    state.isAuthenticated = isAuthenticated;
  },
  SET_USER_DATA(state, userData) {
    state.userData = userData;
  },
  SET_LOADING(state, loading) {
    state.loading = loading;
  },
};

const actions = {
  async getUserInfo({ commit }) {

    commit('SET_LOADING', true);

    const accessToken = localStorage.getItem('access_token');
    
    if (!accessToken) {
      commit('SET_AUTHENTICATED', false);
      return;
    }

    try {
      const response = await axios.get('/api/v1/user', {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
        },
      });

      if (response.status === 200) {
        commit('SET_AUTHENTICATED', true);
        commit('SET_USER_DATA', response.data);
      } else {
        commit('SET_AUTHENTICATED', false);
      }
    } catch (error) {
      commit('SET_AUTHENTICATED', false);
      console.log('Error fetching user data');
    } finally {
      commit('SET_LOADING', false);
    }
  },
  
  startLoading({ commit }) {
    commit('SET_LOADING', true);
  },
  stopLoading({ commit }) {
    commit('SET_LOADING', false);
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
