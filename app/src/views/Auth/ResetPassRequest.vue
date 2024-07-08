<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios';
import DefaultAuthCard from '@/components/Auth/DefaultAuthCard.vue'
import AuthLayout from '@/layouts/AuthLayout.vue'
import { useAlertStore } from '@/store/alert';

const alertStore = useAlertStore();
const router = useRouter();
const email = ref('');
const errormsg = ref('');

const SubmitEmail = async () => {
  if (email.value.length < 4) {
    errormsg.value = 'Please enter a valid email address.';
    return;
  }

  try {
    const response = await axios.post('/api/v1/reset-password-email', { email: email.value });
    console.log(response.data);
    if (response.status === 200) {
      alertStore.setAlertMessage('To complete your password reset request, please check your email and click on the reset request link.');
      router.push({ name: 'signin', query: { email: email.value } });
    }
  } catch (error) {
    if (axios.isAxiosError(error)) {
      if (error.response && error.response.status === 404) {
        errormsg.value = 'If the email exists, a reset link will be sent.';
      } else {
        console.error('Error submitting email:', error);
        errormsg.value = 'Sorry, something went wrong. Please try again later.';
      }
    } else {
      console.error('Unexpected error:', error);
      errormsg.value = 'Sorry, something went wrong. Please try again later.';
    }
  }
};

const clearError = () => {
  errormsg.value = '';
};
</script>

<template>
  <AuthLayout>
    <DefaultAuthCard subtitle="" title="Reset Password">

        <!-- input -->
        <div class="mb-4" @click="clearError">
          <label class="mb-2.5 block font-medium text-black dark:text-white">Email</label>
          <div class="relative">
            <input
              v-model="email"
              name="email"
              type="email"
              placeholder="Enter your email"
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
                    d="M19.2516 3.30005H2.75156C1.58281 3.30005 0.585938 4.26255 0.585938 5.46567V16.6032C0.585938 17.7719 1.54844 18.7688 2.75156 18.7688H19.2516C20.4203 18.7688 21.4172 17.8063 21.4172 16.6032V5.4313C21.4172 4.26255 20.4203 3.30005 19.2516 3.30005ZM19.2516 4.84692C19.2859 4.84692 19.3203 4.84692 19.3547 4.84692L11.0016 10.2094L2.64844 4.84692C2.68281 4.84692 2.71719 4.84692 2.75156 4.84692H19.2516ZM19.2516 17.1532H2.75156C2.40781 17.1532 2.13281 16.8782 2.13281 16.5344V6.35942L10.1766 11.5157C10.4172 11.6875 10.6922 11.7563 10.9672 11.7563C11.2422 11.7563 11.5172 11.6875 11.7578 11.5157L19.8016 6.35942V16.5688C19.8703 16.9125 19.5953 17.1532 19.2516 17.1532Z"
                    fill=""
                  />
                </g>
              </svg>
            </span>
          </div>
        </div>
        <!-- input end -->

        <p v-if="errormsg" class="text-center w-full text-[#F87171]">{{ errormsg }}</p>

        <!-- submit button -->
        <div class="mb-5 mt-6 ">
          <input
            @click="SubmitEmail"
            value="Continue"
            class="text-center w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90"
          />
        </div>
        <!-- submit button end-->

    </DefaultAuthCard>
  </AuthLayout>
</template>

