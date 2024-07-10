<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import axios from 'axios'
import SiteLayout from '@/layouts/DashboardLayout.vue'
import DefaultCard from '@/components/Cards/DefaultCard.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import { Button } from '@/components/ui/button'
import DarkModeSwitcher from '@/components/Dashboard/Header/DarkModeSwitcher.vue'
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
const pageTitle = ref('Account Settings');
const apiKey = ref<string | null>(null);
const isApiKeyVisible = ref(false);
const alertStore = useAlertStore();
const alertMessage = computed(() => alertStore.alertMessage);

watch(alertMessage, (newValue) => {
  if (newValue) {
    setTimeout(() => {
      alertStore.clearAlertMessage();
    }, 10000);
  }
});

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
  return key ? `**********************${key.slice(-4)}` : '';
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

const OldPassword = ref('');
const Password = ref('');
const RePassword = ref('');
const errormsg = ref('');
const dialogOpen = ref(false);

const resetPassword = async () => {
  console.log(OldPassword.value);
  console.log(Password.value);
  console.log(RePassword.value);

  const minLength = 6;
  if (Password.value.length < minLength || OldPassword.value.length < minLength) {
    errormsg.value = 'Password must be at least 6 characters long.';
    return;
  }

  if (Password.value !== RePassword.value) {
    errormsg.value = 'Passwords do not match.';
    return;
  }

  if (OldPassword.value == Password.value) {
    errormsg.value = 'New password cannot be the same as the old password.';
    return;
  }

  try {
    const accessToken = localStorage.getItem('accessToken');
    const response = await axios.post('/api/v1/reset-password-dashboard', {
      oldPassword: OldPassword.value,
      password: Password.value,
    }, {
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      },
    });

    console.log('Response from server:', response);

    if (response.status === 200) {
      alertStore.setAlertMessage("Your password has been changed.");
      window.scrollTo({ top: 0 });
      dialogOpen.value = false;
    } else {
      errormsg.value = response.data.message;
    }
  } catch (error) {
    console.error('Error logging in:', error);
    errormsg.value = "Password is incorrect.";
  }
};


const clearError = () => {
  errormsg.value = '';
};
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
        <!-- Input Fields Start -->
        <DefaultCard cardTitle="Subscription">
          <div class="flex flex-col gap-5.5 p-6.5">
            <div>
              <p>Subscription: {{ authStore.userData.subscription}}</p>
              <p>Remaining credits: {{ authStore.userData.credits}}</p>
              <Button as-child class="mt-4 text-white text-base">
                <a @click="router.push({ name: 'subscribe' })">
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
          <div class="flex flex-col items-left gap-5.5 p-6.5">

            <Dialog v-model:open="dialogOpen">
              <DialogTrigger>
                <p class="cursor-pointer text-left">Change Password</p>
              </DialogTrigger>
              <DialogContent class="bg-white  dark:bg-boxdark">
                <DialogHeader>
                  <DialogTitle>Change Password</DialogTitle>
                  <DialogDescription>

                    <!-- input -->
                    <div class="mb-10 mt-10" @click="clearError">
                      <label class="mb-2.5 block font-medium text-black dark:text-white">Old Password</label>
                      <div class="relative">
                        <input
                          v-model="OldPassword"
                          name="OldPassword"
                          type="Password"
                          placeholder="Password"
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
                      <label class="mb-2.5 block font-medium text-black dark:text-white">New Password</label>
                      <div class="relative">
                        <input
                          v-model="Password"
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
                      <label class="mb-2.5 block font-medium text-black dark:text-white">Confirm New Password</label>
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

                  </DialogDescription>
                </DialogHeader>
                <DialogFooter>
                  <Button type="submit" as-child class="mt-4 text-white text-base">
                    <a @click="resetPassword">
                      Change Password
                    </a>
                  </Button>
                </DialogFooter>
              </DialogContent>
            </Dialog>


            <p @click="router.push({ name: 'logout' })" class="cursor-pointer">Logout</p>
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
            <p>No payment has made yet</p>
          </div>
        </DefaultCard>
        <!-- Checkbox and radio -->

        <!-- Select input Start -->
        <DefaultCard cardTitle="Information">
          <div class="flex flex-col gap-5.5 p-6.5">
            <p @click="router.push('/#about')" class="cursor-pointer">About us</p>
            <p @click="router.push('/#pricing')" class="cursor-pointer">Pricing</p>
            <p @click="router.push({ name: 'privacy_policy' })" class="cursor-pointer">Privacy policy</p>
            <p @click="router.push({ name: 'terms_of_service' })" class="cursor-pointer">Terms of service</p>
            <p @click="router.push({ name: 'help' })" class="cursor-pointer">Help</p>
            <p @click="router.push({ name: 'contact_us' })" class="cursor-pointer">Contact Us</p>
          </div>
        </DefaultCard>
        <!-- Select input End -->
      </div>
    </div>
    <!-- ====== Form Elements Section End -->
  </SiteLayout>
</template>





