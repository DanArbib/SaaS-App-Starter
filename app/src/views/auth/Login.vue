<template>
    <div class="center-container">
      <div class="auth-wrap">
        <img class="auth-logo" :src="logo" alt="Logo">
  
        <div class="ex-text">
          Welcome back
        </div>
        <div class="sm-text">
          Login to your account
        </div>
  
        <form @submit.prevent="submitForm">
          <div class="inputs">
            <input v-model="email" name="email" type="email" placeholder="Email Address" required autocomplete="email">
            <input v-model="password" name="password" type="password" placeholder="Password (8+ characters)" required autocomplete="new-password" pattern=".{8,}">
          </div>
          <div class="error">
            {{ error }} 
          </div>
          <button class="btn-auth" type="submit">Login</button>
        </form>
  
        <div @click="resedEmail" class="reset">
          Forgot your password?
        </div>

        <div class="policy-wrapper">
          <p class="policy">By clicking "Login" you agree to Aipixy's <a href="https://aipixy.com/terms-of-service">Terms of Service</a> and acknowledge you have read our <a href="https://aipixy.com/privacy-policy">Privacy Policy</a>.</p>
        </div>
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
        password: '',
        showReset: false
      }
    },
    beforeRouteEnter(to, from, next) {
    next(vm => {
      vm.email = to.params.email || '';
    });
    },
    methods: {
      resedEmail() {
        this.$router.push({ name: 'resend' });
      },
      async submitForm() {
        this.error = '';
        if (this.email.length < 4) {
          this.error = 'Invalid email address.';
          return;
        }
  
        if (this.password.length < 8) {
          this.error = 'Password must be at least 8 characters long.';
          return;
        }
  
        try {
          const response = await axios.post('/api/v1/login', { email: this.email, password: this.password });
          if (response.status === 200) {
            if (response.data.access_token) {
              localStorage.setItem('access_token', response.data.access_token);
              this.$router.push({ name: 'main' });
            } else {
              this.error = 'Email is not verified.';
              this.showReset = true
            }
          } 
        } catch (error) {
          this.error = 'Wrong email or password.';
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
    font-size: 14px;
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
  