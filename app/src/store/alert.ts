// stores/alert.ts
import { defineStore } from 'pinia';

export const useAlertStore = defineStore('alert', {
  state: () => ({
    alertMessage: '',
  }),
  actions: {
    setAlertMessage(message: string) {
      this.alertMessage = message;
    },
    clearAlertMessage() {
      this.alertMessage = '';
    },
  },
});
