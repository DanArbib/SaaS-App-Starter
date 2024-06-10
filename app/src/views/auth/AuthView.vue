<template>
    <div class="center-container">

      <div class="auth-wrap">
        <img class="auth-logo" :src="logo" alt="Logo">
        <div class="ex-text">
          Let's get started
        </div>
        <div class="sm-text">
          Enter your email in the field below
        </div>
        <div class="inputs">
          <input v-model="email" name="email" type="email" placeholder="Email Address" required autocomplete="email">
        </div>
        <div class="error">
          {{ error }}
        </div>

        <button v-if="!is_sending" class="btn-auth" @click="submitForm">Continue</button>
        <button v-if="is_sending" class="btn-auth" disabled><div class="spinner"></div></button>
        
        <div class="OrSection">
          <hr class="line">
          <div class="text">or</div>
          <hr class="line">
        </div>

        <GoogleBtn></GoogleBtn>

        <div class="policy-wrapper">
          <p class="policy">By clicking “Continue,” you agree to Aipixy's <a href="https://aipixy.com/terms-of-service">Terms of Service</a> and acknowledge you have read our <a href="https://aipixy.com/privacy-policy">Privacy Policy</a>.</p>
        </div>

      </div>
    </div>
</template>
  
  <script>
  import axios from 'axios';
  import logo from '@/assets/logo/logo.png';
  import GoogleBtn from '@/components/auth/GoogleBtn.vue';

  export default {
    components: {
      GoogleBtn,
    },
    data() {
      return {
        logo: logo,
        email: '',
        error: '',
        is_sending: false
      }
    },
    methods: {
    submitForm() {
      this.is_sending = true
      axios.post('/email', { email: this.email })
        .then(response => {
          if (response.data.userFound) {
            this.$router.push({ name: 'login', params: { email: this.email } });
          } else {
            this.$router.push({ name: 'signup', params: { email: this.email } });
          }
        })
        .catch(error => {
          this.is_sending = false
        });
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

  .OrSection {
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 1rem 0;
    
  }
  .line {
    height: 1px;
    border: none;
    background-color: #f1f2f2;
    flex: 1 1;
  }
  .text {
    text-align: center;
    font-size: 14px;
    margin: 0 1rem;
    font-weight: 450;
    color: #5d6565;
  }
  .policy-wrapper {
      text-align:left;
      margin-top:30px;
      font-size: 12px;
      line-height: 16px;
  }

  .inputs {
    margin-top: 15px;
  }

  .inputs input {
    margin: 0px 0;
  }
  .error {
    min-height: 32px;
    color: #a90d0d;
}

.spinner {
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-top: 2px solid #3498db;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    animation: spin 1s linear infinite;
}

.btn-auth {
    display: flex;
    justify-content: center;
    align-items: center;
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
  