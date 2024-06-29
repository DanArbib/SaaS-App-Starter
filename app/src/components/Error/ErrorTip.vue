<script setup lang="ts">
import { useRouter } from 'vue-router';
defineProps<{
  type: '403' | '404' | '500'
}>()
const router = useRouter()
</script>

<template>
  <div class="flex h-screen overflow-hidden items-center justify-center">
    <div class="relative flex flex-1 flex-col overflow-y-auto overflow-x-hidden ">
      <main>
        <div class="mx-auto max-w-screen-2xl p-4 md:p-6 2xl:p-10">


          <div class="flex-col-center h-full flex flex-col items-center">
            <img
              v-if="type === '403'"
              src="@/assets/svg/error-403.svg"
              alt=""
              class="w-1/3"
            >
            <img
              v-if="type === '404'"
              src="@/assets/svg/error-404.svg"
              alt=""
              class="w-1/3"
            >
            <img
              v-if="type === '500'"
              src="@/assets/svg/error-500.svg"
              alt=""
              class="w-1/3"
            >
            <button
              class="text-center cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90"
              @click="router.push('/')"
            >
              Back to Homepage
            </button>
          </div>

        </div>
      </main>
    </div>
  </div>

</template>
