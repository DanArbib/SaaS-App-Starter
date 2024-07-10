<script setup lang="ts">
import { useAlertStore } from '@/store/alert';
import AlertSuccess from '@/components/Alerts/AlertSuccess.vue'
import { computed, onMounted } from 'vue';
const alertStore = useAlertStore();
const alertMessage = computed(() => alertStore.alertMessage);

onMounted(() => {
  if (alertMessage.value) {
    setTimeout(() => {
      alertStore.clearAlertMessage();
    }, 10000); 
  }
});
</script>

<template>
  <div class="flex h-screen overflow-hidden items-center justify-center tpl">
    <div class="relative flex flex-1 flex-col overflow-y-auto overflow-x-hidden">
      <main>
        <div class="mx-auto max-w-screen-2xl p-4 md:p-6 2xl:p-10">
          <!-- Show alert message if present -->
          <div v-if="alertMessage" class="alert alert-info">
            <AlertSuccess :message="alertMessage" />
          </div>

          <slot></slot>
        </div>
      </main>
    </div>
  </div>
</template>

<style scoped>
.tpl {
  /* background: url("@/assets/img/bg.webp"); */
  background-color: rgb(55 88 249 / 1);
  /* background: linear-gradient(12deg, rgb(155, 81, 224) 0%, rgba(7, 146, 227, 0.58) 100%, rgba(156, 82, 225, 0) 100%); */
}
</style>
