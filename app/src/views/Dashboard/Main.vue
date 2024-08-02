<script setup lang="ts">
import SiteLayout from '@/layouts/DashboardLayout.vue'
import { useAuthStore } from '@/store/auth';
const authStore = useAuthStore();
</script>

<template>
  <SiteLayout>
    <div class="mt-4 grid grid-cols-12 gap-4 md:mt-6 md:gap-6 2xl:mt-7.5 2xl:gap-7.5">
      {{ authStore.userData }}
    </div>
  </SiteLayout>
</template>