


<template>
    <div class="center-container">
      <div class="auth-wrap">
        <img class="auth-logo" :src="logo" alt="Logo">
  
        <div class="ex-text">
          Reset your password
        </div>
        <div class="sm-text">
          Enter your email in the field below
        </div>
  
        <form @submit.prevent="submitForm">
          <div class="inputs">
            <input v-model="email" name="email" type="email" placeholder="Email Address" required autocomplete="email">
          </div>
          <div class="error">
            {{ error }} 
          </div>
          <button class="btn-auth" type="submit">Send email</button>
        </form>


      </div>
    </div>
  </template>

  
  <script>
  import axios from 'axios';
  import logo from '@/assets/logo/logo.png';
  
  export default {
    data() {
      return {
        logo: logo,
        email: '',
        error: '',
      }
    },
    methods: {
      async submitForm() {
        this.error = '';
  
        if (this.email.length < 4) {
          this.error = 'Invalid email address.';
          return;
        }
  
        try {
          const response = await axios.post('/api/v1/reset-password-email', { email: this.email });
          if (response.status === 200) {
            this.$router.push({ name: 'reset' });
          } 
        } catch (error) {
          this.error = 'Error resending verification email.';
          console.error(error);
        }
      },
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
    min-width: 400px;
    margin: 10px;
  }
  .auth-logo {
    width:60px;
    margin: 0px 0;
  }

  .inputs {
    margin-top: 15px;
  }

  .inputs input {
    margin: 5px 0;
  }
  .policy-wrapper {
      text-align:left;
      margin-top:20px;
      font-size: 12px;
      line-height: 16px;
  }
.error {
    min-height: 32px;
    color: #a90d0d;
}
.reset {
    color: #033dab;
    margin: 10px 0px;
    cursor: pointer;
}

.ex-text {
    font-size: 22px;
    font-weight: 600;
    color: #2b2b30;
}

.sm-text {
    font-size: 14px;
    margin-bottom: 30px;
}
  </style>
  