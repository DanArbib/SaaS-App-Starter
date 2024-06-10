<template>
    <div class="center-container">
      <div class="auth-wrap">
        <img class="auth-logo" :src="logo" alt="Logo">
        <div class="text-email">
            <p>To complete your password reset request, please check your email and click on the reset request link.</p>   
        </div>
        <button class="btn-auth" @click="toLogin">Login</button>

      </div>
    </div>
</template>
  
  <script>
  import logo from '@/assets/logo/logo.png';

  export default {
    data() {
      return {
        logo: logo,
      }
    },


    methods: {

    toLogin() {
      this.$router.push({ name: 'login' });
    }
  }
  }
  </script>
  
  
  <style scoped>
  .center-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: url("@/assets/bg.jpg");
    background-size: cover;
  }
  .auth-wrap {
    max-width: 400px;
    padding: 25px;
    background: #fff;
    border-radius: 10px;
    box-shadow: 3px 4px 7px 0 hsl(0deg 3.17% 3.82% / 15%);
    margin: 10px;
  }
  .auth-logo {
    width:60px;
    margin: 0px 0;
  }

.text-email {
    margin: 33px 0px;
}
  </style>
  