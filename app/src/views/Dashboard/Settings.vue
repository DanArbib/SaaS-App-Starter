<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import SiteLayout from '@/layouts/DashboardLayout.vue'
import DefaultCard from '@/components/Cards/DefaultCard.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import { Button } from '@/components/ui/button'
import DarkModeSwitcher from '@/components/Dashboard/Header/DarkModeSwitcher.vue'
import { useAuthStore } from '@/store/auth';

const authStore = useAuthStore();
const pageTitle = ref('Account Settings');
const apiKey = ref<string | null>(null);
const isApiKeyVisible = ref(false);

const fetchApiKey = async () => {
  try {
    const accessToken = localStorage.getItem('accessToken');
    if (!accessToken) {
      throw new Error('No access token found');
    }
    
    const response = await axios.get('/api/v1/api-keys', {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });
    
    apiKey.value = response.data.api_keys[0] || null;
  } catch (error) {
    console.error('Error fetching API key:', error);
  }
};

const toggleApiKeyVisibility = () => {
  isApiKeyVisible.value = !isApiKeyVisible.value;
};

onMounted(() => {
  fetchApiKey();
});

const getMaskedApiKey = (key: string) => {
  return key ? `************${key.slice(-4)}` : '';
};
</script>

<template>
  <SiteLayout class="">
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->

    <!-- ====== Form Elements Section Start -->
    <div class=" grid grid-cols-1 gap-9 sm:grid-cols-2">
      <div class="flex flex-col gap-9">
        <!-- Input Fields Start -->
        <DefaultCard cardTitle="Subscription">
          <div class="flex flex-col gap-5.5 p-6.5">
            <div>
              <p>Subscription: {{ authStore.userData.subscription}}</p>
              <p>Remaining credits: {{ authStore.userData.credits}}</p>
              <Button as-child class="mt-4">
                <a href="/login">
                  Purchase Credits
                </a>
              </Button>
            </div>
          </div>
        </DefaultCard>
        <!-- Input Fields End -->

        <!-- Toggle switch input Start -->
        <DefaultCard cardTitle="Theme">
          <div class="flex flex-col gap-5.5 p-6.5">
            <p>Enable dark mode</p>
             <!-- Dark Mode Toggler -->
                <DarkModeSwitcher />
            <!-- Dark Mode Toggler -->
          </div>
        </DefaultCard>
        <!-- Toggle switch input End -->

        <!-- Time and date input Start -->
        <DefaultCard cardTitle="Account">
          <div class="flex flex-col gap-5.5 p-6.5">
            <p class="">Logout</p>
            <p class="text-red">Delete Account</p>
          </div>
        </DefaultCard>
        <!-- Time and date input End -->

      </div>

      <div class="flex flex-col gap-9">
        <!-- Textarea Fields Start -->
        <DefaultCard cardTitle="API Key">
          <div class="flex flex-col gap-5.5 p-6.5">
            <div v-if="apiKey">
              <p class="mt-2">API key: {{ isApiKeyVisible ? apiKey : getMaskedApiKey(apiKey) }}</p>
              <Button class="mt-4" variant="outline" @click="toggleApiKeyVisibility">
                {{ isApiKeyVisible ? 'Hide' : 'Show' }}
              </Button>
            </div>
            <div v-else>
              <p>Loading...</p>
            </div>
          </div>
        </DefaultCard>
        <!-- Textarea Fields End -->

        <!-- Checkbox and radio -->
        <DefaultCard cardTitle="Checkbox and radio">
          <div class="flex flex-col gap-5.5 p-6.5">

          </div>
        </DefaultCard>
        <!-- Checkbox and radio -->

        <!-- Select input Start -->
        <DefaultCard cardTitle="Information">
          <div class="flex flex-col gap-5.5 p-6.5">
            <p class="">About us</p>
            <p class="">Pricing</p>
            <p class="">Privacy policy</p>
            <p class="">Terms of service</p>
            <p class="">Help</p>
            <p class="">Contact Us</p>
          </div>
        </DefaultCard>
        <!-- Select input End -->
      </div>
    </div>
    <!-- ====== Form Elements Section End -->
  </SiteLayout>
</template>





