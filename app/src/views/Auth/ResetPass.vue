<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import DefaultAuthCard from '@/components/Auth/DefaultAuthCard.vue'
import AuthLayout from '@/layouts/AuthLayout.vue'
import { useAlertStore } from '@/store/alert';

const props = defineProps(['token'])

const token = ref(props.token)
const alertStore = useAlertStore();
const router = useRouter();
const password = ref('');
const RePassword = ref('');
const errormsg = ref('');

const resetPassword = async () => {

  if (password.value.length < 6) {
    errormsg.value = 'Password must be at least 6 characters long.';
  return;
  }

  if (password.value !== RePassword.value) {
    errormsg.value = 'Passwords do not match.';
  return;
  }

  try {
    const response = await axios.post(`/api/v1/reset-password`, {
      token: token.value,
      password: password.value,
    });

    if (response.status === 200) {
      alertStore.setAlertMessage("Your password has been changed, please signin to your account.");
      router.push({ name: 'signin' });
    } else {
      errormsg.value = 'An error occurred while processing your request.';
    }
  } catch (error) {
    errormsg.value = 'An error occurred while processing your request.';
    console.error('Error logging in:', error);
  }
};


const clearError = () => {
  errormsg.value = '';
};

</script>

<template>
  <AuthLayout>

    <DefaultAuthCard subtitle="Enter the fields below to reset your password" title="Reset password">

        <!-- input -->
        <div class="mb-4" @click="clearError">
          <label class="mb-2.5 block font-medium text-black dark:text-white">Password</label>
          <div class="relative">
            <input
              v-model="password"
              name="Password"
              type="Password"
              placeholder="6+ Characters, 1 Capital letter"
              class="w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary text-black dark:text-white"
            />
            <span class="absolute right-4 top-4">
              <svg
                class="fill-current"
                width="22"
                height="22"
                viewBox="0 0 22 22"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <g opacity="0.5">
                  <path
                    d="M16.1547 6.80626V5.91251C16.1547 3.16251 14.0922 0.825009 11.4797 0.618759C10.0359 0.481259 8.59219 0.996884 7.52656 1.95938C6.46094 2.92188 5.84219 4.29688 5.84219 5.70626V6.80626C3.84844 7.18438 2.33594 8.93751 2.33594 11.0688V17.2906C2.33594 19.5594 4.19219 21.3813 6.42656 21.3813H15.5016C17.7703 21.3813 19.6266 19.525 19.6266 17.2563V11C19.6609 8.93751 18.1484 7.21876 16.1547 6.80626ZM8.55781 3.09376C9.31406 2.40626 10.3109 2.06251 11.3422 2.16563C13.1641 2.33751 14.6078 3.98751 14.6078 5.91251V6.70313H7.38906V5.67188C7.38906 4.70938 7.80156 3.78126 8.55781 3.09376ZM18.1141 17.2906C18.1141 18.7 16.9453 19.8688 15.5359 19.8688H6.46094C5.05156 19.8688 3.91719 18.7344 3.91719 17.325V11.0688C3.91719 9.52189 5.15469 8.28438 6.70156 8.28438H15.2953C16.8422 8.28438 18.1141 9.52188 18.1141 11V17.2906Z"
                    fill=""
                  />
                  <path
                    d="M10.9977 11.8594C10.5852 11.8594 10.207 12.2031 10.207 12.65V16.2594C10.207 16.6719 10.5508 17.05 10.9977 17.05C11.4102 17.05 11.7883 16.7063 11.7883 16.2594V12.6156C11.7883 12.2031 11.4102 11.8594 10.9977 11.8594Z"
                    fill=""
                  />
                </g>
              </svg>
            </span>
          </div>
        </div>
        <!-- input end -->

        <!-- input -->
        <div class="mb-4" @click="clearError">
          <label class="mb-2.5 block font-medium text-black dark:text-white">Confirm Password</label>
          <div class="relative">
            <input
              v-model="RePassword"
              name="RePassword"
              type="Password"
              placeholder="Re-enter your password"
              class="w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary text-black dark:text-white"
            />
            <span class="absolute right-4 top-4">
              <svg
                class="fill-current"
                width="22"
                height="22"
                viewBox="0 0 22 22"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <g opacity="0.5">
                  <path
                    d="M16.1547 6.80626V5.91251C16.1547 3.16251 14.0922 0.825009 11.4797 0.618759C10.0359 0.481259 8.59219 0.996884 7.52656 1.95938C6.46094 2.92188 5.84219 4.29688 5.84219 5.70626V6.80626C3.84844 7.18438 2.33594 8.93751 2.33594 11.0688V17.2906C2.33594 19.5594 4.19219 21.3813 6.42656 21.3813H15.5016C17.7703 21.3813 19.6266 19.525 19.6266 17.2563V11C19.6609 8.93751 18.1484 7.21876 16.1547 6.80626ZM8.55781 3.09376C9.31406 2.40626 10.3109 2.06251 11.3422 2.16563C13.1641 2.33751 14.6078 3.98751 14.6078 5.91251V6.70313H7.38906V5.67188C7.38906 4.70938 7.80156 3.78126 8.55781 3.09376ZM18.1141 17.2906C18.1141 18.7 16.9453 19.8688 15.5359 19.8688H6.46094C5.05156 19.8688 3.91719 18.7344 3.91719 17.325V11.0688C3.91719 9.52189 5.15469 8.28438 6.70156 8.28438H15.2953C16.8422 8.28438 18.1141 9.52188 18.1141 11V17.2906Z"
                    fill=""
                  />
                  <path
                    d="M10.9977 11.8594C10.5852 11.8594 10.207 12.2031 10.207 12.65V16.2594C10.207 16.6719 10.5508 17.05 10.9977 17.05C11.4102 17.05 11.7883 16.7063 11.7883 16.2594V12.6156C11.7883 12.2031 11.4102 11.8594 10.9977 11.8594Z"
                    fill=""
                  />
                </g>
              </svg>
            </span>
          </div>
        </div>
        <!-- input end -->

        <p v-if="errormsg" class="text-center w-full text-[#F87171]">{{ errormsg }}</p>

        <div class="mb-5 mt-6">
          <input
            @click="resetPassword"
            value="Create account"
            class="text-center w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90"
          />
        </div>
    </DefaultAuthCard>
  </AuthLayout>
</template>