// stores/auth.ts
import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    userData: {user:'Guest', credits: '0', avatar: 'avatar' },
    loading: false,
  }),
  actions: {
    async getUserInfo() {
      this.loading = true;

      const accessToken = localStorage.getItem('accessToken');
      
      if (!accessToken) {
        this.isAuthenticated = false;
        this.loading = false;
        return;
      }

      try {
        const response = await axios.get('/api/v1/user', {
          headers: {
            'Authorization': `Bearer ${accessToken}`,
          },
        });

        if (response.status === 200) {
          this.isAuthenticated = true;
          this.userData = response.data;
        } else {
          this.isAuthenticated = false;
        }
      } catch (error) {
        this.isAuthenticated = false;
        console.error('Error fetching user data:', error);
      } finally {
        this.loading = false;
      }
    },
  },
  getters: {
    isUserAuthenticated: (state) => state.isAuthenticated,
    getUserData: (state) => state.userData,
  },
});
