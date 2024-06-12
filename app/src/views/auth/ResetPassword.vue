<template>
    <div class="center-container">
      <div class="auth-wrap">
        <img class="auth-logo" :src="logo" alt="Logo">

        <div class="ex-text">
          Reset password
        </div>
        <div class="sm-text">
          Enter the fields below to reset your password
        </div>

        <form @submit.prevent="submitForm">
            <div class="inputs">
                <input v-model="password" name="password" type="password" placeholder="New password (8+ characters)" required autocomplete="new-password" pattern=".{8,}">
                <input v-model="confirmPassword" name="confirmPassword" type="password" placeholder="Confirm Password" required autocomplete="new-password">
            </div>
            <div v-if="error" class="error">
                {{ error }}
            </div>

            <button v-if="!is_sending" class="btn-auth" type="submit">Reset</button>
            <button v-if="is_sending" class="btn-auth" disabled><div class="spinner"></div></button>
        </form>

      </div>
    </div>
</template>
  
  <script>
  import axios from 'axios';
  import logo from '@/assets/logo/logo.png';

  export default {
    beforeRouteEnter(to, from, next) {
    next(vm => {
      vm.email = to.params.email || '';
    });
  },

    components: {
    },
    data() {
      return {
        logo: logo,
        error: '',
        password: '',
        confirmPassword: '',
        is_sending: false
      }
    },

    methods: {

        submitForm() {

        if (this.password.length < 8) {
        this.error = 'Password must be at least 8 characters long.';
        return;
        }

        if (this.password !== this.confirmPassword) {
        this.error = 'Passwords do not match.';
        return;
        }

        this.is_sending = true
        axios.post('/api/v1/reset-password', { password: this.password, token: this.$route.query.t })
        .then(response => {
            const status = response.data.status;

            if (response.status === 200) {
            this.$router.push({ name: 'login' });
            }
        })
        .catch(error => {
            this.error = 'An error occurred while processing your request.';
            console.error(error);
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

  .inputs {
    margin-top: 15px;
  }

  .inputs input {
    margin: 5px 0;
  }
  .policy-wrapper {
      text-align:left;
      margin-top:30px;
      font-size: 12px;
      line-height: 16px;
  }
  .error {
    color: #a90d0d;
    min-height: 39px;
    font-size: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.msg {
    min-height: 39px;
    font-size: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
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
    margin-top: 20px;
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
  