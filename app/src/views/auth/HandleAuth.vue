<template>
  <div>
    <div class="wrap-spinner">
      <div class="spinner"></div>
      <h2>Email Verification Successful</h2>
      <p>Your email has been successfully verified.</p>
      <p>Redirecting to the login page...</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HandleAuth',
  mounted() {
    const accessToken = this.$route.query.access_token;
    localStorage.setItem('access_token', accessToken);
    this.$router.push('/');
  },
};
</script>


<style scoped>
.wrap-spinner {
    display: flex;
    height: 100vh;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}
</style>