<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import axios from 'axios'
import SiteLayout from '@/layouts/DashboardLayout.vue'
import DefaultCard from '@/components/Cards/DefaultCard.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import { Button } from '@/components/ui/button'
import { useAuthStore } from '@/store/auth';
import { useRouter } from 'vue-router';
import { useAlertStore } from '@/store/alert';
import AlertSuccess from '@/components/Alerts/AlertSuccessDashboard.vue'
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from '@/components/ui/alert-dialog'

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog'

const router = useRouter();
const authStore = useAuthStore();
const pageTitle = ref('Subscribe');
const alertStore = useAlertStore();
const alertMessage = computed(() => alertStore.alertMessage);

watch(alertMessage, (newValue) => {
  if (newValue) {
    setTimeout(() => {
      alertStore.clearAlertMessage();
    }, 10000);
  }
});

</script>

<template>
  <SiteLayout class="">
              <!-- Show alert message if present -->
          <div v-if="alertMessage" class="alert alert-info">
            <AlertSuccess :message="alertMessage" />
          </div>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->

    <!-- ====== Form Elements Section Start -->
    <div class=" grid grid-cols-1 gap-9 sm:grid-cols-2">
      <div class="flex flex-col gap-9">
 
      </div>
    </div>
    <!-- ====== Form Elements Section End -->
  </SiteLayout>
</template>





