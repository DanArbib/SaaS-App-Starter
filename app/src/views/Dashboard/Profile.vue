<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import SiteLayout from '@/layouts/DashboardLayout.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import { useAuthStore } from '@/store/auth';
import { useAlertStore } from '@/store/alert';
import AlertSuccess from '@/components/Alerts/AlertSuccessDashboard.vue'
import { createAvatar, Result } from '@dicebear/core';
import { initials } from '@dicebear/collection';

const authStore = useAuthStore();
const pageTitle = ref('My Profile');
const alertStore = useAlertStore();
const alertMessage = computed(() => alertStore.alertMessage);

watch(alertMessage, (newValue) => {
  if (newValue) {
    setTimeout(() => {
      alertStore.clearAlertMessage();
    }, 10000);
  }
});


const generateAvatar = (seed: string): Result => {
  return createAvatar(initials, {
    backgroundColor: ["b6e3f4", "c0aede", "d1d4f9"],
    backgroundType: ["gradientLinear", "solid"],
    size: 150,
    scale: 100,
    seed,
  });
};

const avatar = ref<Result | null>(null);
const avatarDataUri = computed(() => {
  if (avatar.value) {
    return avatar.value.toDataUri() as string;
  }
  return undefined;
});

watch(() => authStore.userData.user, (newAvatar) => {
  if (newAvatar) {
    avatar.value = generateAvatar(newAvatar);
  } else {
    avatar.value = null;
  }
});

if (authStore.userData.avatar) {
  avatar.value = generateAvatar(authStore.userData.user);
}

</script>

<template>
  <SiteLayout>
              <!-- Show alert message if present -->
          <div v-if="alertMessage" class="alert alert-info">
            <AlertSuccess :message="alertMessage" />
          </div>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->
 <!-- ====== Profile Section Start -->
 <div
    class="overflow-hidden rounded-lg border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark"
  >
    <div class="relative z-20 h-35 md:h-65">

    </div>

    <div class="px-4 pb-6 text-center lg:pb-8 xl:pb-11.5">
      <div
        class="relative z-30 mx-auto -mt-22 h-30 w-full max-w-30 rounded-full bg-white/20 p-1 backdrop-blur sm:h-44 sm:max-w-44 sm:p-3"
      >
        <div class="relative drop-shadow-2">
          <img class="rounded-full" :src="avatarDataUri" alt="profile" />
          
        </div>
      </div>
      <div class="mt-4">
        <h3 class="mb-1.5 text-2xl font-medium text-black dark:text-white">{{ authStore.userData.user }}</h3>
        <p class="font-medium"></p>
        <div
          class="mx-auto mt-4.5 mb-5.5 grid max-w-94 grid-cols-3 rounded-md border border-stroke py-2.5 shadow-1 dark:border-strokedark dark:bg-[#37404F]"
        >
          <div
            class="flex flex-col items-center justify-center gap-1 border-r border-stroke px-4 dark:border-strokedark xsm:flex-row"
          >
            <span class="font-semibold text-black dark:text-white">259</span>
            <span class="text-sm">Posts</span>
          </div>
          <div
            class="flex flex-col items-center justify-center gap-1 border-r border-stroke px-4 dark:border-strokedark xsm:flex-row"
          >
            <span class="font-semibold text-black dark:text-white">129K</span>
            <span class="text-sm">Followers</span>
          </div>
          <div class="flex flex-col items-center justify-center gap-1 px-4 xsm:flex-row">
            <span class="font-semibold text-black dark:text-white">2K</span>
            <span class="text-sm">Following</span>
          </div>
        </div>

        <div class="mb-22 mx-auto max-w-180">
          <h4 class="font-medium text-black dark:text-white">About Me</h4>
          <p class="mt-4.5 text-sm font-normal">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque posuere fermentum
            urna, eu condimentum mauris tempus ut. Donec fermentum blandit aliquet. Etiam dictum
            dapibus ultricies. Sed vel aliquet libero. Nunc a augue fermentum, pharetra ligula sed,
            aliquam lacus.
          </p>
        </div>

      </div>
    </div>
  </div>
  <!-- ====== Profile Section End -->
  </SiteLayout>
</template>





