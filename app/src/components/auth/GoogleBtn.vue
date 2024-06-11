<template>
    <div>
        <button @click="authenticateWithGoogle" class="GoogleBtn"  :disabled="loading">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd">
        <path d="M20.16 12.193c0-.603-.054-1.182-.155-1.739H12v3.288h4.575a3.91 3.91 0 0 1-1.696 2.565v2.133h2.747c1.607-1.48 2.535-3.659 2.535-6.248z" fill="#4285f4"></path><path d="M12 20.5c2.295 0 4.219-.761 5.625-2.059l-2.747-2.133c-.761.51-1.735.811-2.878.811-2.214 0-4.088-1.495-4.756-3.504h-2.84v2.202A8.497 8.497 0 0 0 12 20.5z" fill="#34a853"></path><path d="M7.244 13.615A5.11 5.11 0 0 1 6.977 12a5.11 5.11 0 0 1 .267-1.615V8.183h-2.84C3.828 9.33 3.5 10.628 3.5 12s.328 2.67.904 3.817l2.84-2.202z" fill="#fbbc05"></path><path d="M12 6.881c1.248 0 2.368.429 3.249 1.271l2.438-2.438C16.215 4.342 14.291 3.5 12 3.5a8.497 8.497 0 0 0-7.596 4.683l2.84 2.202C7.912 8.376 9.786 6.881 12 6.881z" fill="#ea4335">
        </path>
        </svg>
        <div class="te">
          Continue with Google
        </div>
        <div v-if="loading" class="spinner"></div>
      </button>
    </div>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
    };
  },
  methods: {
    authenticateWithGoogle() {

      this.loading = true;
      window.location.href = `${process.env.VUE_APP_API_BASE_URL}/api/v1/google-login/`;
    }
  }
};
</script>

<style scoped>
  .GoogleBtn {
    display: flex;
    flex-direction: row;
    border: none;
    gap: 6px;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-weight: 450;
    font-size: inherit;
    font-size: 14px;
    text-align: center;
    padding: 0.6em 1rem;
    margin: 0;
    border-radius: 5px;
    width: 100%;
  }
svg {
    width: 32px;
}

.spinner {
  border: 3px solid rgba(0, 0, 0, 0.1);
  border-top: 3px solid #ffffff;
  border-radius: 50%;
  width: 15px;
  height: 15px;
  animation: spin 1s linear infinite;
}
</style>