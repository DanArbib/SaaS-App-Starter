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
          {{}}
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
  background: url("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3MweG9tZ3U5bDJ0bHp2ZGs2NzFzcGF1M3I5YmRmOTBsbGZsb2hudiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZEHkGB5qlzjOo7Yxjt/giphy.webp");
}
</style>
