<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import SiteLayout from '@/layouts/DashboardLayout.vue'
import DefaultCard from '@/components/Cards/DefaultCard.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import { Button } from '@/components/ui/button'
import DarkModeSwitcher from '@/components/Dashboard/Header/DarkModeSwitcher.vue'
import { useAuthStore } from '@/store/auth';
import { useRouter } from 'vue-router';

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


const router = useRouter();
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

const generateNewApiKey = async () => {
  try {
    const accessToken = localStorage.getItem('accessToken');
    if (!accessToken) {
      throw new Error('No access token found');
    }
    
    const currentKey = apiKey.value; // Get the current API key
    if (!currentKey) {
      throw new Error('No current API key found');
    }
    
    // Send request to generate new API key with current key
    const response = await axios.post('/api/v1/generate-api-key', { key: currentKey }, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });
    
    console.log('New API Key generated:', response.data); // Optional: log the response
    
    // Fetch the updated API key after generating
    await fetchApiKey();
  } catch (error) {
    console.error('Error generating new API key:', error);
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


const deleteAccount = async () => {
      try {
        const accessToken = localStorage.getItem('accessToken');
        const response = await axios.delete('/api/v1/user', {
          headers: {
            'Authorization': `Bearer ${accessToken}`,
          },
        });

        if (response.status === 200) {
          localStorage.removeItem('accessToken');
          router.push({ name: 'home' });
        } else {
          console.error('Failed to delete account:', response.data.message);
        }
      } catch (error) {
        console.error('Error deleting account:', error);
      }
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
        <DefaultCard cardTitle="Others">
          <div class="flex flex-col gap-5.5 p-6.5">
            <p @click="router.push('/logout')" class="cursor-pointer">Logout</p>
            <AlertDialog>
              <AlertDialogTrigger as-child>
            <p class="cursor-pointer text-red">Delete Account</p>
              </AlertDialogTrigger>
              <AlertDialogContent class="bg-white  dark:bg-boxdark">
                <AlertDialogHeader>
                  <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                  <AlertDialogDescription>
                    This action cannot be undone. This will permanently delete your
                    account and remove your data from our servers.
                  </AlertDialogDescription>
                </AlertDialogHeader>
                <AlertDialogFooter>
                  <AlertDialogCancel>Cancel</AlertDialogCancel>
                  <AlertDialogAction @click="deleteAccount">Delete Account</AlertDialogAction>
                </AlertDialogFooter>
              </AlertDialogContent>
            </AlertDialog>
          </div>
        </DefaultCard>
        <!-- Time and date input End -->

      </div>

      <div class="flex flex-col gap-9">
        <!-- Textarea Fields Start -->
        <DefaultCard cardTitle="API Key">
          <div class="flex flex-col gap-5.5 p-6.5">
            <div v-if="apiKey">
              <p class="mt-2">{{ isApiKeyVisible ? apiKey : getMaskedApiKey(apiKey) }}</p>
              <Button class="mt-4 min-w-22" variant="outline" @click="toggleApiKeyVisibility">
                {{ isApiKeyVisible ? 'Hide' : 'Show' }}
              </Button>
              <Button class="mt-4 ms-2" variant="outline" @click="generateNewApiKey">
                Generate New API Key
              </Button>
            </div>
            <div v-else>
              <p>Loading...</p>
            </div>
          </div>
        </DefaultCard>
        <!-- Textarea Fields End -->

        <!-- Checkbox and radio -->
        <DefaultCard cardTitle="Payments">
          <div class="flex flex-col gap-5.5 p-6.5">
            <p class="mt-2">Change password</p>
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





