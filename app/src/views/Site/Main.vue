<script setup lang="ts">
import NavBar from '@/components/Site/Navbar.vue'
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion'
import WOW from "wow.js";
import '@/assets/css/animate.css';
const wow = new WOW({});
wow.init();

// FAQ 
const defaultValue = 'item-1'
const accordionItems = [
  { value: 'item-1', title: 'Is it accessible?', content: 'Yes. It adheres to the WAI-ARIA design pattern.' },
  { value: 'item-2', title: 'Is it unstyled?', content: 'Yes. It\'s unstyled by default, giving you freedom over the look and feel.' },
  { value: 'item-3', title: 'Can it be animated?', content: 'Yes! You can use the transition prop to configure the animation.' },
]

</script>

<template>
    <!-- ====== Navbar Section Start -->
    <div class="ud-header absolute left-0 top-0 z-40 flex w-full items-center bg-transparent">
      <NavBar></NavBar>
    </div>
    <!-- ====== Navbar Section End -->


    <!-- ====== Hero Section Start -->
    <div
      id="home"
      class="relative overflow-hidden bg-primary max-h-[95vh] pt-[120px] md:pt-[130px] lg:pt-[160px]"
    >
      <div class="container">
        <div class="-mx-4 flex flex-wrap items-center">
          <div class="w-full px-4">
            <div
              class="hero-content wow fadeInUp mx-auto max-w-[780px] text-center"
              data-wow-delay=".2s"
            >
              <h1
                class="mb-6 text-3xl font-bold leading-snug text-white sm:text-4xl sm:leading-snug lg:text-5xl lg:leading-[1.2]"
              >
                Starter Template for Building Microservices Based SaaS Applications
              </h1>
              <p
                class="mx-auto max-w-[600px] text-base font-medium text-white sm:text-lg sm:leading-[1.44]"
              >
                Multidisciplinary Template Built with
              </p>
              <p
                class="mx-auto mb-9 max-w-[600px] text-base font-medium text-white sm:text-lg sm:leading-[1.44]"
              >
                Vue.js, TypeScript, Tailwind, Python (Flask) and Postgres.
              </p>
              <ul
                class="mb-10 flex flex-wrap items-center justify-center gap-5"
              >
                <li>
                  <router-link
                  :to="{ name: 'auth' }"
                  class="inline-flex items-center justify-center rounded-md bg-white px-7 py-[14px] text-center text-base font-medium text-dark shadow-1 transition duration-300 ease-in-out hover:bg-gray-2 hover:text-body-color"
                >
                  Get Started Now
                </router-link>
                </li>
                <li>
                  <a
                    href="https://github.com/DanArbib/SaaS-App-Starter.git"
                    target="_blank"
                    class="flex items-center gap-4 rounded-md bg-white/[0.12] px-6 py-[14px] text-base font-medium text-white transition duration-300 ease-in-out hover:bg-white hover:text-dark"
                  >
                    <svg
                      class="fill-current"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <g clip-path="url(#clip0_2005_10818)">
                        <path
                          d="M12 0.674805C5.625 0.674805 0.375 5.8498 0.375 12.2998C0.375 17.3998 3.7125 21.7498 8.3625 23.3248C8.9625 23.4373 9.15 23.0623 9.15 22.7998C9.15 22.5373 9.15 21.7873 9.1125 20.7748C5.8875 21.5248 5.2125 19.1998 5.2125 19.1998C4.6875 17.8873 3.9 17.5123 3.9 17.5123C2.85 16.7623 3.9375 16.7623 3.9375 16.7623C5.1 16.7998 5.7375 17.9623 5.7375 17.9623C6.75 19.7623 8.475 19.2373 9.1125 18.8998C9.225 18.1498 9.525 17.6248 9.8625 17.3248C7.3125 17.0623 4.575 16.0498 4.575 11.6248C4.575 10.3498 5.0625 9.3373 5.775 8.5498C5.6625 8.2873 5.25 7.0873 5.8875 5.4748C5.8875 5.4748 6.9 5.1748 9.1125 6.6748C10.05 6.4123 11.025 6.2623 12.0375 6.2623C13.05 6.2623 14.0625 6.3748 14.9625 6.6748C17.175 5.2123 18.15 5.4748 18.15 5.4748C18.7875 7.0498 18.4125 8.2873 18.2625 8.5498C19.0125 9.3373 19.4625 10.3873 19.4625 11.6248C19.4625 16.0498 16.725 17.0623 14.175 17.3248C14.5875 17.6998 14.9625 18.4498 14.9625 19.4998C14.9625 21.0748 14.925 22.3123 14.925 22.6873C14.925 22.9873 15.15 23.3248 15.7125 23.2123C20.2875 21.6748 23.625 17.3623 23.625 12.2248C23.5875 5.8498 18.375 0.674805 12 0.674805Z"
                        />
                      </g>
                      <defs>
                        <clipPath id="clip0_2005_10818">
                          <rect width="24" height="24" fill="white" />
                        </clipPath>
                      </defs>
                    </svg>
                    Github
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <div class="w-full px-4">
            <div
              class="wow fadeInUp relative z-10 mx-auto max-w-[1000px]"
              data-wow-delay=".25s"
            >
              <div class="mt-16">
                <img
                  src="@/assets/img/main-hero-img.jpg"
                  alt="hero"
                  class="mx-auto max-w-full rounded-t-xl rounded-tr-xl"
                />
              </div>
              <div class="absolute -left-9 bottom-0 z-[-1]">
                <svg
                  width="134"
                  height="106"
                  viewBox="0 0 134 106"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <circle
                    cx="1.66667"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 1.66667 104)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 16.3333 104)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 31 104)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 45.6667 104)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 60.3333 104)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 88.6667 104)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 117.667 104)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 74.6667 104)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 103 104)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 132 104)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="89.3333"
                    r="1.66667"
                    transform="rotate(-90 1.66667 89.3333)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="89.3333"
                    r="1.66667"
                    transform="rotate(-90 16.3333 89.3333)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="89.3333"
                    r="1.66667"
                    transform="rotate(-90 31 89.3333)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="89.3333"
                    r="1.66667"
                    transform="rotate(-90 45.6667 89.3333)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 60.3333 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 88.6667 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 117.667 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 74.6667 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 103 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 132 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="74.6673"
                    r="1.66667"
                    transform="rotate(-90 1.66667 74.6673)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="31.0003"
                    r="1.66667"
                    transform="rotate(-90 1.66667 31.0003)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 16.3333 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="31.0003"
                    r="1.66667"
                    transform="rotate(-90 16.3333 31.0003)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 31 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="31.0003"
                    r="1.66667"
                    transform="rotate(-90 31 31.0003)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 45.6667 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="31.0003"
                    r="1.66667"
                    transform="rotate(-90 45.6667 31.0003)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 60.3333 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 60.3333 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 88.6667 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 88.6667 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 117.667 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 117.667 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 74.6667 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 74.6667 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 103 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 103 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 132 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 132 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 1.66667 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 1.66667 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 16.3333 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 16.3333 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 31 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 31 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 45.6667 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 45.6667 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 60.3333 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 60.3333 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 88.6667 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 88.6667 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 117.667 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 117.667 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 74.6667 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 74.6667 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 103 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 103 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 132 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 132 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="45.3336"
                    r="1.66667"
                    transform="rotate(-90 1.66667 45.3336)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="1.66683"
                    r="1.66667"
                    transform="rotate(-90 1.66667 1.66683)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="45.3336"
                    r="1.66667"
                    transform="rotate(-90 16.3333 45.3336)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="1.66683"
                    r="1.66667"
                    transform="rotate(-90 16.3333 1.66683)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="45.3336"
                    r="1.66667"
                    transform="rotate(-90 31 45.3336)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="1.66683"
                    r="1.66667"
                    transform="rotate(-90 31 1.66683)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="45.3336"
                    r="1.66667"
                    transform="rotate(-90 45.6667 45.3336)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="1.66683"
                    r="1.66667"
                    transform="rotate(-90 45.6667 1.66683)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 60.3333 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 60.3333 1.66707)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 88.6667 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 88.6667 1.66707)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 117.667 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 117.667 1.66707)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 74.6667 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 74.6667 1.66707)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 103 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 103 1.66707)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 132 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 132 1.66707)"
                    fill="white"
                  />
                </svg>
              </div>
              <div class="absolute -right-6 -top-6 z-[-1]">
                <svg
                  width="134"
                  height="106"
                  viewBox="0 0 134 106"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <circle
                    cx="1.66667"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 1.66667 104)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 16.3333 104)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 31 104)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 45.6667 104)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 60.3333 104)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 88.6667 104)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 117.667 104)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 74.6667 104)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 103 104)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="104"
                    r="1.66667"
                    transform="rotate(-90 132 104)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="89.3333"
                    r="1.66667"
                    transform="rotate(-90 1.66667 89.3333)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="89.3333"
                    r="1.66667"
                    transform="rotate(-90 16.3333 89.3333)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="89.3333"
                    r="1.66667"
                    transform="rotate(-90 31 89.3333)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="89.3333"
                    r="1.66667"
                    transform="rotate(-90 45.6667 89.3333)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 60.3333 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 88.6667 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 117.667 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 74.6667 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 103 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="89.3338"
                    r="1.66667"
                    transform="rotate(-90 132 89.3338)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="74.6673"
                    r="1.66667"
                    transform="rotate(-90 1.66667 74.6673)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="31.0003"
                    r="1.66667"
                    transform="rotate(-90 1.66667 31.0003)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 16.3333 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="31.0003"
                    r="1.66667"
                    transform="rotate(-90 16.3333 31.0003)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 31 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="31.0003"
                    r="1.66667"
                    transform="rotate(-90 31 31.0003)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 45.6667 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="31.0003"
                    r="1.66667"
                    transform="rotate(-90 45.6667 31.0003)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 60.3333 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 60.3333 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 88.6667 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 88.6667 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 117.667 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 117.667 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 74.6667 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 74.6667 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 103 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 103 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="74.6668"
                    r="1.66667"
                    transform="rotate(-90 132 74.6668)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="31.0001"
                    r="1.66667"
                    transform="rotate(-90 132 31.0001)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 1.66667 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 1.66667 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 16.3333 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 16.3333 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 31 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 31 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 45.6667 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 45.6667 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 60.3333 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 60.3333 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 88.6667 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 88.6667 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 117.667 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 117.667 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 74.6667 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 74.6667 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 103 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 103 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="60.0003"
                    r="1.66667"
                    transform="rotate(-90 132 60.0003)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="16.3336"
                    r="1.66667"
                    transform="rotate(-90 132 16.3336)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="45.3336"
                    r="1.66667"
                    transform="rotate(-90 1.66667 45.3336)"
                    fill="white"
                  />
                  <circle
                    cx="1.66667"
                    cy="1.66683"
                    r="1.66667"
                    transform="rotate(-90 1.66667 1.66683)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="45.3336"
                    r="1.66667"
                    transform="rotate(-90 16.3333 45.3336)"
                    fill="white"
                  />
                  <circle
                    cx="16.3333"
                    cy="1.66683"
                    r="1.66667"
                    transform="rotate(-90 16.3333 1.66683)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="45.3336"
                    r="1.66667"
                    transform="rotate(-90 31 45.3336)"
                    fill="white"
                  />
                  <circle
                    cx="31"
                    cy="1.66683"
                    r="1.66667"
                    transform="rotate(-90 31 1.66683)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="45.3336"
                    r="1.66667"
                    transform="rotate(-90 45.6667 45.3336)"
                    fill="white"
                  />
                  <circle
                    cx="45.6667"
                    cy="1.66683"
                    r="1.66667"
                    transform="rotate(-90 45.6667 1.66683)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 60.3333 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="60.3333"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 60.3333 1.66707)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 88.6667 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="88.6667"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 88.6667 1.66707)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 117.667 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="117.667"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 117.667 1.66707)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 74.6667 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="74.6667"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 74.6667 1.66707)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 103 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="103"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 103 1.66707)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="45.3338"
                    r="1.66667"
                    transform="rotate(-90 132 45.3338)"
                    fill="white"
                  />
                  <circle
                    cx="132"
                    cy="1.66707"
                    r="1.66667"
                    transform="rotate(-90 132 1.66707)"
                    fill="white"
                  />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ====== Hero Section End -->

    <!-- ====== Features Section Start -->
    <section id="features" class="pb-8 pt-20 dark:bg-dark lg:pb-[70px] lg:pt-[120px]" >
      
      <div class="container">
        <div class="-mx-4 flex flex-wrap">
          <div class="w-full px-4">
            <div class="mx-auto mb-12 max-w-[485px] text-center lg:mb-[70px]">
              <span class="mb-2 block text-lg font-semibold text-primary">
                Features
              </span>
              <h2
                class="mb-6 text-3xl font-bold text-dark dark:text-white sm:text-4xl md:text-[40px] md:leading-[1.2]"
              >
                Main Features
              </h2>
              <p class="text-base text-body-color dark:text-dark-6">
                There are many variations of passages of Lorem Ipsum available
                but the majority have suffered alteration in some form.
              </p>
            </div>
          </div>
        </div>
        <div class="-mx-4 flex flex-wrap">
          <div class="w-full px-4 md:w-1/2 lg:w-1/4">
            <div class="wow fadeInUp group mb-12" data-wow-delay=".1s">
              <div
                class="relative z-10 mb-10 flex h-[70px] w-[70px] items-center justify-center rounded-[14px] bg-primary"
              >
                <span
                  class="absolute left-0 top-0 -z-[1] mb-8 flex h-[70px] w-[70px] rotate-[25deg] items-center justify-center rounded-[14px] bg-primary bg-opacity-20 duration-300 group-hover:rotate-45"
                ></span>
                <svg
                  width="37"
                  height="37"
                  viewBox="0 0 37 37"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M30.5801 8.30514H27.9926C28.6113 7.85514 29.1176 7.34889 29.3426 6.73014C29.6801 5.88639 29.6801 4.48014 27.9363 2.84889C26.0801 1.04889 24.3926 1.04889 23.3238 1.33014C20.9051 1.94889 19.2738 4.76139 18.3738 6.78639C17.4738 4.76139 15.8426 2.00514 13.4238 1.33014C12.3551 1.04889 10.6676 1.10514 8.81133 2.84889C7.06758 4.53639 7.12383 5.88639 7.40508 6.73014C7.63008 7.34889 8.13633 7.85514 8.75508 8.30514H5.71758C4.08633 8.30514 2.73633 9.65514 2.73633 11.2864V14.9989C2.73633 16.5739 4.03008 17.8676 5.60508 17.9239V31.6489C5.60508 33.5614 7.18008 35.1926 9.14883 35.1926H27.5426C29.4551 35.1926 31.0863 33.6176 31.0863 31.6489V17.8676C32.4926 17.6426 33.5613 16.4051 33.5613 14.9426V11.2301C33.5613 9.59889 32.2113 8.30514 30.5801 8.30514ZM23.9426 3.69264C23.9988 3.69264 24.1676 3.63639 24.3363 3.63639C24.7301 3.63639 25.3488 3.80514 26.1926 4.59264C26.8676 5.21139 27.0363 5.66139 26.9801 5.77389C26.6988 6.56139 23.8863 7.40514 20.6801 7.74264C21.4676 5.99889 22.6488 4.03014 23.9426 3.69264ZM10.4988 4.64889C11.3426 3.86139 11.9613 3.69264 12.3551 3.69264C12.5238 3.69264 12.6363 3.74889 12.7488 3.74889C14.0426 4.08639 15.2801 5.99889 16.0676 7.79889C12.8613 7.46139 10.0488 6.61764 9.76758 5.83014C9.71133 5.66139 9.88008 5.26764 10.4988 4.64889ZM5.26758 14.9426V11.2301C5.26758 11.0051 5.43633 10.7801 5.71758 10.7801H30.5801C30.8051 10.7801 31.0301 10.9489 31.0301 11.2301V14.9426C31.0301 15.1676 30.8613 15.3926 30.5801 15.3926H5.71758C5.49258 15.3926 5.26758 15.2239 5.26758 14.9426ZM27.5426 32.6614H9.14883C8.58633 32.6614 8.13633 32.2114 8.13633 31.6489V17.9239H28.4988V31.6489C28.5551 32.2114 28.1051 32.6614 27.5426 32.6614Z"
                    fill="white"
                  />
                </svg>
              </div>
              <h4 class="mb-3 text-xl font-bold text-dark dark:text-white">
                Free and Open-Source
              </h4>
              <p class="mb-8 text-body-color dark:text-dark-6 lg:mb-9">
                Lorem Ipsum is simply dummy text of the printing and industry.
              </p>
              <a
                href="/"
                class="text-base font-medium text-dark hover:text-primary dark:text-white dark:hover:text-primary"
              >
                Learn More
              </a>
            </div>
          </div>
          <div class="w-full px-4 md:w-1/2 lg:w-1/4">
            <div class="wow fadeInUp group mb-12" data-wow-delay=".15s">
              <div
                class="relative z-10 mb-10 flex h-[70px] w-[70px] items-center justify-center rounded-[14px] bg-primary"
              >
                <span
                  class="absolute left-0 top-0 -z-[1] mb-8 flex h-[70px] w-[70px] rotate-[25deg] items-center justify-center rounded-[14px] bg-primary bg-opacity-20 duration-300 group-hover:rotate-45"
                ></span>
                <svg
                  width="36"
                  height="36"
                  viewBox="0 0 36 36"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M30.5998 1.01245H5.39981C2.98105 1.01245 0.956055 2.9812 0.956055 5.4562V30.6562C0.956055 33.075 2.9248 35.0437 5.39981 35.0437H30.5998C33.0186 35.0437 34.9873 33.075 34.9873 30.6562V5.39995C34.9873 2.9812 33.0186 1.01245 30.5998 1.01245ZM5.39981 3.48745H30.5998C31.6123 3.48745 32.4561 4.3312 32.4561 5.39995V11.1937H3.4873V5.39995C3.4873 4.38745 4.38731 3.48745 5.39981 3.48745ZM3.4873 30.6V13.725H23.0623V32.5125H5.39981C4.38731 32.5125 3.4873 31.6125 3.4873 30.6ZM30.5998 32.5125H25.5373V13.725H32.4561V30.6C32.5123 31.6125 31.6123 32.5125 30.5998 32.5125Z"
                    fill="white"
                  />
                </svg>
              </div>
              <h4 class="mb-3 text-xl font-bold text-dark dark:text-white">
                Multipurpose Template
              </h4>
              <p class="mb-8 text-body-color dark:text-dark-6 lg:mb-9">
                Lorem Ipsum is simply dummy text of the printing and industry.
              </p>
              <a
                href="/"
                class="text-base font-medium text-dark hover:text-primary dark:text-white dark:hover:text-primary"
              >
                Learn More
              </a>
            </div>
          </div>
          <div class="w-full px-4 md:w-1/2 lg:w-1/4">
            <div class="wow fadeInUp group mb-12" data-wow-delay=".2s">
              <div
                class="relative z-10 mb-10 flex h-[70px] w-[70px] items-center justify-center rounded-[14px] bg-primary"
              >
                <span
                  class="absolute left-0 top-0 -z-[1] mb-8 flex h-[70px] w-[70px] rotate-[25deg] items-center justify-center rounded-[14px] bg-primary bg-opacity-20 duration-300 group-hover:rotate-45"
                ></span>
                <svg
                  width="37"
                  height="37"
                  viewBox="0 0 37 37"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M33.5613 21.4677L31.3675 20.1177C30.805 19.7239 30.0175 19.9489 29.6238 20.5114C29.23 21.1302 29.455 21.8614 30.0175 22.2552L31.48 23.2114L18.1488 31.5927L4.76127 23.2114L6.22377 22.2552C6.84252 21.8614 7.01127 21.0739 6.61752 20.5114C6.22377 19.8927 5.43627 19.7239 4.87377 20.1177L2.68002 21.4677C2.11752 21.8614 1.72377 22.4802 1.72377 23.1552C1.72377 23.8302 2.06127 24.5052 2.68002 24.8427L17.08 33.8989C17.4175 34.1239 17.755 34.1802 18.1488 34.1802C18.5425 34.1802 18.88 34.0677 19.2175 33.8989L33.5613 24.8989C34.1238 24.5052 34.5175 23.8864 34.5175 23.2114C34.5175 22.5364 34.18 21.8614 33.5613 21.4677Z"
                    fill="white"
                  />
                  <path
                    d="M20.1175 20.4552L18.1488 21.6364L16.18 20.3989C15.5613 20.0052 14.83 20.2302 14.4363 20.7927C14.0425 21.4114 14.2675 22.1427 14.83 22.5364L17.4738 24.1677C17.6988 24.2802 17.9238 24.3364 18.1488 24.3364C18.3738 24.3364 18.5988 24.2802 18.8238 24.1677L21.4675 22.5364C22.0863 22.1427 22.255 21.3552 21.8613 20.7927C21.4675 20.2302 20.68 20.0614 20.1175 20.4552Z"
                    fill="white"
                  />
                  <path
                    d="M7.74252 18.0927L11.455 20.4552C11.68 20.5677 11.905 20.6239 12.13 20.6239C12.5238 20.6239 12.9738 20.3989 13.1988 20.0052C13.5925 19.3864 13.3675 18.6552 12.805 18.2614L9.09252 15.8989C8.47377 15.5052 7.74252 15.7302 7.34877 16.2927C6.95502 16.9677 7.12377 17.7552 7.74252 18.0927Z"
                    fill="white"
                  />
                  <path
                    d="M5.04252 16.1802C5.43627 16.1802 5.88627 15.9552 6.11127 15.5614C6.50502 14.9427 6.28002 14.2114 5.71752 13.8177L4.81752 13.2552L5.71752 12.6927C6.33627 12.2989 6.50502 11.5114 6.11127 10.9489C5.71752 10.3302 4.93002 10.1614 4.36752 10.5552L1.72377 12.1864C1.33002 12.4114 1.10502 12.8052 1.10502 13.2552C1.10502 13.7052 1.33002 14.0989 1.72377 14.3239L4.36752 15.9552C4.53627 16.1239 4.76127 16.1802 5.04252 16.1802Z"
                    fill="white"
                  />
                  <path
                    d="M8.41752 10.7239C8.64252 10.7239 8.86752 10.6677 9.09252 10.5552L12.805 8.1927C13.4238 7.79895 13.5925 7.01145 13.1988 6.44895C12.805 5.8302 12.0175 5.66145 11.455 6.0552L7.74252 8.4177C7.12377 8.81145 6.95502 9.59895 7.34877 10.1614C7.57377 10.4989 7.96752 10.7239 8.41752 10.7239Z"
                    fill="white"
                  />
                  <path
                    d="M16.18 6.05522L18.1488 4.81772L20.1175 6.05522C20.3425 6.16772 20.5675 6.22397 20.7925 6.22397C21.1863 6.22397 21.6363 5.99897 21.8613 5.60522C22.255 4.98647 22.03 4.25522 21.4675 3.86147L18.8238 2.23022C18.43 1.94897 17.8675 1.94897 17.4738 2.23022L14.83 3.86147C14.2113 4.25522 14.0425 5.04272 14.4363 5.60522C14.83 6.16772 15.6175 6.44897 16.18 6.05522Z"
                    fill="white"
                  />
                  <path
                    d="M23.4925 8.19267L27.205 10.5552C27.43 10.6677 27.655 10.7239 27.88 10.7239C28.2738 10.7239 28.7238 10.4989 28.9488 10.1052C29.3425 9.48642 29.1175 8.75517 28.555 8.36142L24.8425 5.99892C24.28 5.60517 23.4925 5.83017 23.0988 6.39267C22.705 7.01142 22.8738 7.79892 23.4925 8.19267Z"
                    fill="white"
                  />
                  <path
                    d="M34.5738 12.1864L31.93 10.5552C31.3675 10.1614 30.58 10.3864 30.1863 10.9489C29.7925 11.5677 30.0175 12.2989 30.58 12.6927L31.48 13.2552L30.58 13.8177C29.9613 14.2114 29.7925 14.9989 30.1863 15.5614C30.4113 15.9552 30.8613 16.1802 31.255 16.1802C31.48 16.1802 31.705 16.1239 31.93 16.0114L34.5738 14.3802C34.9675 14.1552 35.1925 13.7614 35.1925 13.3114C35.1925 12.8614 34.9675 12.4114 34.5738 12.1864Z"
                    fill="white"
                  />
                  <path
                    d="M24.1675 20.624C24.3925 20.624 24.6175 20.5677 24.8425 20.4552L28.555 18.0927C29.1738 17.699 29.3425 16.9115 28.9488 16.349C28.555 15.7302 27.7675 15.5615 27.205 15.9552L23.4925 18.3177C22.8738 18.7115 22.705 19.499 23.0988 20.0615C23.3238 20.4552 23.7175 20.624 24.1675 20.624Z"
                    fill="white"
                  />
                </svg>
              </div>
              <h4 class="mb-3 text-xl font-bold text-dark dark:text-white">
                High-quality Design
              </h4>
              <p class="mb-8 text-body-color dark:text-dark-6 lg:mb-9">
                Lorem Ipsum is simply dummy text of the printing and industry.
              </p>
              <a
                href="/"
                class="text-base font-medium text-dark hover:text-primary dark:text-white dark:hover:text-primary"
              >
                Learn More
              </a>
            </div>
          </div>
          <div class="w-full px-4 md:w-1/2 lg:w-1/4">
            <div class="wow fadeInUp group mb-12" data-wow-delay=".25s">
              <div
                class="relative z-10 mb-10 flex h-[70px] w-[70px] items-center justify-center rounded-[14px] bg-primary"
              >
                <span
                  class="absolute left-0 top-0 -z-[1] mb-8 flex h-[70px] w-[70px] rotate-[25deg] items-center justify-center rounded-[14px] bg-primary bg-opacity-20 duration-300 group-hover:rotate-45"
                ></span>
                <svg
                  width="37"
                  height="37"
                  viewBox="0 0 37 37"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M12.355 2.0614H5.21129C3.29879 2.0614 1.72379 3.6364 1.72379 5.5489V12.6927C1.72379 14.6052 3.29879 16.1802 5.21129 16.1802H12.355C14.2675 16.1802 15.8425 14.6052 15.8425 12.6927V5.60515C15.8988 3.6364 14.3238 2.0614 12.355 2.0614ZM13.3675 12.7489C13.3675 13.3114 12.9175 13.7614 12.355 13.7614H5.21129C4.64879 13.7614 4.19879 13.3114 4.19879 12.7489V5.60515C4.19879 5.04265 4.64879 4.59265 5.21129 4.59265H12.355C12.9175 4.59265 13.3675 5.04265 13.3675 5.60515V12.7489Z"
                    fill="white"
                  />
                  <path
                    d="M31.0863 2.0614H23.9425C22.03 2.0614 20.455 3.6364 20.455 5.5489V12.6927C20.455 14.6052 22.03 16.1802 23.9425 16.1802H31.0863C32.9988 16.1802 34.5738 14.6052 34.5738 12.6927V5.60515C34.5738 3.6364 32.9988 2.0614 31.0863 2.0614ZM32.0988 12.7489C32.0988 13.3114 31.6488 13.7614 31.0863 13.7614H23.9425C23.38 13.7614 22.93 13.3114 22.93 12.7489V5.60515C22.93 5.04265 23.38 4.59265 23.9425 4.59265H31.0863C31.6488 4.59265 32.0988 5.04265 32.0988 5.60515V12.7489Z"
                    fill="white"
                  />
                  <path
                    d="M12.355 20.0051H5.21129C3.29879 20.0051 1.72379 21.5801 1.72379 23.4926V30.6364C1.72379 32.5489 3.29879 34.1239 5.21129 34.1239H12.355C14.2675 34.1239 15.8425 32.5489 15.8425 30.6364V23.5489C15.8988 21.5801 14.3238 20.0051 12.355 20.0051ZM13.3675 30.6926C13.3675 31.2551 12.9175 31.7051 12.355 31.7051H5.21129C4.64879 31.7051 4.19879 31.2551 4.19879 30.6926V23.5489C4.19879 22.9864 4.64879 22.5364 5.21129 22.5364H12.355C12.9175 22.5364 13.3675 22.9864 13.3675 23.5489V30.6926Z"
                    fill="white"
                  />
                  <path
                    d="M31.0863 20.0051H23.9425C22.03 20.0051 20.455 21.5801 20.455 23.4926V30.6364C20.455 32.5489 22.03 34.1239 23.9425 34.1239H31.0863C32.9988 34.1239 34.5738 32.5489 34.5738 30.6364V23.5489C34.5738 21.5801 32.9988 20.0051 31.0863 20.0051ZM32.0988 30.6926C32.0988 31.2551 31.6488 31.7051 31.0863 31.7051H23.9425C23.38 31.7051 22.93 31.2551 22.93 30.6926V23.5489C22.93 22.9864 23.38 22.5364 23.9425 22.5364H31.0863C31.6488 22.5364 32.0988 22.9864 32.0988 23.5489V30.6926Z"
                    fill="white"
                  />
                </svg>
              </div>
              <h4 class="mb-3 text-xl font-bold text-dark dark:text-white">
                All Essential Elements
              </h4>
              <p class="mb-8 text-body-color dark:text-dark-6 lg:mb-9">
                Lorem Ipsum is simply dummy text of the printing and industry.
              </p>
              <a
                href="/"
                class="text-base font-medium text-dark hover:text-primary dark:text-white dark:hover:text-primary"
              >
                Learn More
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- ====== Features Section End -->


    <!-- ====== CTA Section Start -->
    <section
      class="relative z-10 overflow-hidden bg-primary py-20 lg:py-[115px]"
    >
      <div class="container mx-auto">
        <div class="relative overflow-hidden">
          <div class="-mx-4 flex flex-wrap items-stretch">
            <div class="w-full px-4">
              <div class="mx-auto max-w-[570px] text-center">
                <h2
                  class="mb-2.5 text-3xl font-bold text-white md:text-[38px] md:leading-[1.44]"
                >
                  <span>What Are You Waiting For?</span>
                  <span class="text-3xl font-normal md:text-[40px]">
                    Get Started Now
                  </span>
                </h2>
                <p
                  class="mx-auto mb-6 max-w-[515px] text-base leading-[1.5] text-white"
                >
                  There are many variations of passages of Lorem Ipsum but the
                  majority have suffered in some form.
                </p>
                <a
                  href="/"
                  class="inline-block rounded-md border border-transparent bg-white px-7 py-3 text-base font-medium text-dark transition hover:bg-gray-2 hover:text-body-color"
                >
                  Start using XXXXX
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <span class="absolute left-0 top-0">
          <svg
            width="495"
            height="470"
            viewBox="0 0 495 470"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <circle
              cx="55"
              cy="442"
              r="138"
              stroke="white"
              stroke-opacity="0.04"
              stroke-width="50"
            />
            <circle
              cx="446"
              r="39"
              stroke="white"
              stroke-opacity="0.04"
              stroke-width="20"
            />
            <path
              d="M245.406 137.609L233.985 94.9852L276.609 106.406L245.406 137.609Z"
              stroke="white"
              stroke-opacity="0.08"
              stroke-width="12"
            />
          </svg>
        </span>
        <span class="absolute bottom-0 right-0">
          <svg
            width="493"
            height="470"
            viewBox="0 0 493 470"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <circle
              cx="462"
              cy="5"
              r="138"
              stroke="white"
              stroke-opacity="0.04"
              stroke-width="50"
            />
            <circle
              cx="49"
              cy="470"
              r="39"
              stroke="white"
              stroke-opacity="0.04"
              stroke-width="20"
            />
            <path
              d="M222.393 226.701L272.808 213.192L259.299 263.607L222.393 226.701Z"
              stroke="white"
              stroke-opacity="0.06"
              stroke-width="13"
            />
          </svg>
        </span>
      </div>
    </section>
    <!-- ====== CTA Section End -->

    <!-- ====== Pricing Section Start -->
    <section
      id="pricing"
      class="relative z-20 overflow-hidden bg-white pb-12 pt-20 dark:bg-dark lg:pb-[90px] lg:pt-[120px]"
    >
      <div class="container mx-auto">
        <div class="-mx-4 flex flex-wrap">
          <div class="w-full px-4">
            <div class="mx-auto mb-[60px] max-w-[510px] text-center">
              <span class="mb-2 block text-lg font-semibold text-primary">
                Pricing
              </span>
              <h2
                class="mb-3 text-3xl font-bold text-dark dark:text-white sm:text-4xl md:text-[40px] md:leading-[1.2]"
              >
                Ready to grow your XXX?
              </h2>
              <p class="text-base text-body-color dark:text-dark-6">
                Select your power plan
              </p>
            </div>
          </div>
        </div>
        <div class="-mx-4 flex flex-wrap justify-center">
          <div class="w-full px-4 md:w-1/2 lg:w-1/3">
            <div
              class="relative z-10 mb-10 overflow-hidden rounded-xl bg-white px-8 py-10 shadow-pricing dark:bg-dark-2 sm:p-12 lg:px-6 lg:py-10 xl:p-14"
            >
              <span
                class="mb-5 block text-xl font-medium text-dark dark:text-white"
              >
                Starter
              </span>
              <h2
                class="mb-11 text-4xl font-semibold text-dark dark:text-white xl:text-[42px] xl:leading-[1.21]"
              >
                <span class="text-xl font-medium">$</span>
                <span class="-ml-1 -tracking-[2px]">25.00</span>
                <span
                  class="text-base font-normal text-body-color dark:text-dark-6"
                >
                  Per Month
                </span>
              </h2>
              <div class="mb-[50px]">
                <h5 class="mb-5 text-lg font-medium text-dark dark:text-white">
                  Features
                </h5>
                <div class="flex flex-col gap-[14px]">
                  <p class="text-base text-body-color dark:text-dark-6">
                    Up to 1 User
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    All UI components
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    Lifetime access
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    Free updates
                  </p>
                </div>
              </div>
              <a
                href="/"
                class="inline-block rounded-md bg-primary px-7 py-3 text-center text-base font-medium text-white transition hover:bg-blue-dark"
              >
                Purchase Now
              </a>
            </div>
          </div>
          <div class="w-full px-4 md:w-1/2 lg:w-1/3">
            <div
              class="relative z-10 mb-10 overflow-hidden rounded-xl bg-white px-8 py-10 shadow-pricing dark:bg-dark-2 sm:p-12 lg:px-6 lg:py-10 xl:p-14"
            >
              <p
                class="absolute right-[-50px] top-[60px] inline-block -rotate-90 rounded-bl-md rounded-tl-md bg-primary px-5 py-2 text-base font-medium text-white"
              >
                Recommended
              </p>
              <span
                class="mb-5 block text-xl font-medium text-dark dark:text-white"
              >
                Basic
              </span>
              <h2
                class="mb-11 text-4xl font-semibold text-dark dark:text-white xl:text-[42px] xl:leading-[1.21]"
              >
                <span class="text-xl font-medium">$</span>
                <span class="-ml-1 -tracking-[2px]">59.00</span>
                <span
                  class="text-base font-normal text-body-color dark:text-dark-6"
                >
                  Per Month
                </span>
              </h2>
              <div class="mb-[50px]">
                <h5 class="mb-5 text-lg font-medium text-dark dark:text-white">
                  Features
                </h5>
                <div class="flex flex-col gap-[14px]">
                  <p class="text-base text-body-color dark:text-dark-6">
                    Up to 1 User
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    All UI components
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    Lifetime access
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    Free updates
                  </p>
                </div>
              </div>
              <a
                href="/"
                class="inline-block rounded-md bg-primary px-7 py-3 text-center text-base font-medium text-white transition hover:bg-blue-dark"
              >
                Purchase Now
              </a>
            </div>
          </div>
          <div class="w-full px-4 md:w-1/2 lg:w-1/3">
            <div
              class="relative z-10 mb-10 overflow-hidden rounded-xl bg-white px-8 py-10 shadow-pricing dark:bg-dark-2 sm:p-12 lg:px-6 lg:py-10 xl:p-14"
            >
              <span
                class="mb-5 block text-xl font-medium text-dark dark:text-white"
              >
                Premium
              </span>
              <h2
                class="mb-11 text-4xl font-semibold text-dark dark:text-white xl:text-[42px] xl:leading-[1.21]"
              >
                <span class="text-xl font-medium">$</span>
                <span class="-ml-1 -tracking-[2px]">99.00</span>
                <span
                  class="text-base font-normal text-body-color dark:text-dark-6"
                >
                  Per Month
                </span>
              </h2>
              <div class="mb-[50px]">
                <h5 class="mb-5 text-lg font-medium text-dark dark:text-white">
                  Features
                </h5>
                <div class="flex flex-col gap-[14px]">
                  <p class="text-base text-body-color dark:text-dark-6">
                    Up to 1 User
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    All UI components
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    Lifetime access
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    Free updates
                  </p>
                </div>
              </div>
              <a
                href="/"
                class="inline-block rounded-md bg-primary px-7 py-3 text-center text-base font-medium text-white transition hover:bg-blue-dark"
              >
                Purchase Now
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- ====== Pricing Section End -->

    <!-- ====== Testimonial Section Start -->
    <section
      id="testimonials"
      class="overflow-hidden bg-gray-1 py-20 dark:bg-dark-2 md:py-[120px]"
    >
      <div class="container mx-auto">
        <div class="-mx-4 flex flex-wrap justify-center">
          <div class="w-full px-4">
            <div class="mx-auto mb-[60px] max-w-[485px] text-center">
              <span class="mb-2 block text-lg font-semibold text-primary">
                Our clients
              </span>
              <h2
                class="mb-3 text-3xl font-bold leading-[1.2] text-dark dark:text-white sm:text-4xl md:text-[40px]"
              >
              Join XXXXXX on the fast track to success
              </h2>
              <p class="text-base text-body-color dark:text-dark-6">
                Don't take our word for it. Here's what they have to say about XXXXXXX.
              </p>
            </div>
          </div>
        </div>
        <div class="box-border max-w-7xl mx-4 sm:columns-1 md:columns-2 lg:columns-3 xl:columns-3">


        </div>
      </div>
    </section>
    <!-- ====== Testimonial Section End -->

    <!-- ====== FAQ Section Start -->
    <section
      id="faq"
      class="relative z-20 overflow-hidden bg-white pb-30 pt-20 dark:bg-dark lg:pb-[100px] lg:pt-[120px] "
    >
      <div class="container mx-auto mb-[100px]">
        <div class="-mx-4 flex flex-wrap">
          <div class="w-full px-4">
            <div class="mx-auto mb-[60px] max-w-[520px] text-center">
              <span class="mb-2 block text-lg font-semibold text-primary">
                FAQ
              </span>
           
            </div>
          </div>
        </div>
        <div class="-mx-4 flex flex-wrap">
          <div class="w-full px-4 lg:w-1/2 px-6">

            <h2
                class="text-left mb-3 text-3xl font-bold leading-[1.2] text-dark dark:text-white sm:text-4xl md:text-[40px]"
              >
              Frequently Asked Questions
              </h2>
              <p class="max-w-[485px] text-base text-body-color dark:text-dark-6">
                Have another question? Contact us by <router-link to="/#contact" class="text-blue-500">email</router-link>.
              </p>
          </div>
          <div class="w-full px-4 lg:w-1/2">
            <Accordion type="single" class="w-full" collapsible :default-value="defaultValue">
              <AccordionItem v-for="item in accordionItems" :key="item.value" :value="item.value">
                <AccordionTrigger>{{ item.title }}</AccordionTrigger>
                <AccordionContent>
                  {{ item.content }}
                </AccordionContent>
              </AccordionItem>
            </Accordion>
          </div>
        </div>
      </div>

    </section>
    <!-- ====== FAQ Section End -->



    <!-- ====== Brands Section Start -->
    <section class="pb-20 dark:bg-dark">
      <div class="container px-4">
        <div
          class="-mx-4 flex flex-wrap items-center justify-center gap-8 xl:gap-11"
        >
          <a href="https://graygrids.com/">
            <img
              src="@/assets/images/brands/graygrids.svg"
              alt="graygrids"
              class="dark:hidden"
            />
            <img
              src="@/assets/images/brands/graygrids-white.svg"
              alt="graygrids"
              class="hidden dark:block"
            />
          </a>
          <a href="https://lineicons.com/">
            <img
              src="@/assets/images/brands/lineicons.svg"
              alt="lineicons"
              class="dark:hidden"
            />
            <img
              src="@/assets/images/brands/lineicons-white.svg"
              alt="graygrids"
              class="hidden dark:block"
            />
          </a>
          <a href="https://uideck.com/">
            <img
              src="@/assets/images/brands/uideck.svg"
              alt="uideck"
              class="dark:hidden"
            />
            <img
              src="@/assets/images/brands/uideck-white.svg"
              alt="graygrids"
              class="hidden dark:block"
            />
          </a>
          <a href="https://ayroui.com/">
            <img
              src="@/assets/images/brands/ayroui.svg"
              alt="ayroui"
              class="dark:hidden"
            />
            <img
              src="@/assets/images/brands/ayroui-white.svg"
              alt="graygrids"
              class="hidden dark:block"
            />
          </a>
          <a href="https://tailgrids.com/">
            <img
              src="@/assets/images/brands/tailgrids.svg"
              alt="tailgrids"
              class="dark:hidden"
            />
            <img
              src="@/assets/images/brands/tailgrids-white.svg"
              alt="graygrids"
              class="hidden dark:block"
            />
          </a>
        </div>
      </div>
    </section>
    <!-- ====== Brands Section End -->

    <!-- ====== Footer Section Start -->
    <footer
      class="wow fadeInUp relative z-10 bg-black-2 pt-20 lg:pt-[100px]"
      data-wow-delay=".15s"
    >
      <div class="container">
        <div class="-mx-4 flex flex-wrap">
          <div class="w-full px-4 sm:w-1/2 md:w-1/2 lg:w-4/12 xl:w-4/12">
            <div class="mb-10 w-full">
              <a
                href="/"
                class="mb-6 inline-block max-w-[160px]"
              >
                <img
                  src="@/assets/logo/logo-darkmode.png"
                  alt="logo"
                  class="max-w-full"
                />
              </a>
              <p class="mb-8 max-w-[270px] text-base text-gray-7">
                We create digital experiences for brands and companies by using
                technology.
              </p>
              <div class="-mx-3 flex items-center">
                <a
                  href="/"
                  class="px-3 text-gray-7 hover:text-white"
                >
                  <svg
                    width="22"
                    height="22"
                    viewBox="0 0 22 22"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    class="fill-current"
                  >
                    <path
                      d="M16.294 8.86875H14.369H13.6815V8.18125V6.05V5.3625H14.369H15.8128C16.1909 5.3625 16.5003 5.0875 16.5003 4.675V1.03125C16.5003 0.653125 16.2253 0.34375 15.8128 0.34375H13.3034C10.5878 0.34375 8.69714 2.26875 8.69714 5.12187V8.1125V8.8H8.00964H5.67214C5.19089 8.8 4.74402 9.17812 4.74402 9.72812V12.2031C4.74402 12.6844 5.12214 13.1313 5.67214 13.1313H7.94089H8.62839V13.8188V20.7281C8.62839 21.2094 9.00652 21.6562 9.55652 21.6562H12.7878C12.994 21.6562 13.1659 21.5531 13.3034 21.4156C13.4409 21.2781 13.544 21.0375 13.544 20.8312V13.8531V13.1656H14.2659H15.8128C16.2596 13.1656 16.6034 12.8906 16.6721 12.4781V12.4438V12.4094L17.1534 10.0375C17.1878 9.79688 17.1534 9.52187 16.9471 9.24687C16.8784 9.075 16.569 8.90312 16.294 8.86875Z"
                    />
                  </svg>
                </a>
                <a
                  href="/"
                  class="px-3 text-gray-7 hover:text-white"
                >
                  <svg
                    width="22"
                    height="22"
                    viewBox="0 0 22 22"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    class="fill-current"
                  >
                    <path
                      d="M20.1236 5.91236C20.2461 5.76952 20.0863 5.58286 19.905 5.64972C19.5004 5.79896 19.1306 5.8974 18.5837 5.95817C19.2564 5.58362 19.5693 5.04828 19.8237 4.39259C19.885 4.23443 19.7 4.09092 19.5406 4.16647C18.8931 4.47345 18.1945 4.70121 17.4599 4.83578C16.7338 4.11617 15.6988 3.6665 14.5539 3.6665C12.3554 3.6665 10.5725 5.32454 10.5725 7.36908C10.5725 7.65933 10.6081 7.94206 10.6752 8.21276C7.51486 8.06551 4.6968 6.71359 2.73896 4.64056C2.60477 4.49848 2.36128 4.51734 2.27772 4.69063C2.05482 5.15296 1.93056 5.66584 1.93056 6.20582C1.93056 7.49014 2.6332 8.62331 3.70132 9.28732C3.22241 9.27293 2.76441 9.17961 2.34234 9.02125C2.13684 8.94416 1.90127 9.07964 1.92888 9.28686C2.14084 10.8781 3.42915 12.1909 5.09205 12.5011C4.75811 12.586 4.40639 12.6311 4.04253 12.6311C3.95431 12.6311 3.86685 12.6284 3.78019 12.6231C3.55967 12.6094 3.38044 12.8067 3.47499 12.9954C4.09879 14.2404 5.44575 15.1096 7.0132 15.1367C5.65077 16.13 3.93418 16.7218 2.06882 16.7218C1.83882 16.7218 1.74015 17.0175 1.9442 17.1178C3.52016 17.8924 5.31487 18.3332 7.22182 18.3332C14.545 18.3332 18.549 12.6914 18.549 7.79843C18.549 7.63827 18.545 7.47811 18.5377 7.31945C19.1321 6.92012 19.6664 6.44528 20.1236 5.91236Z"
                    />
                  </svg>
                </a>
                <a
                  href="/"
                  class="px-3 text-gray-7 hover:text-white"
                >
                  <svg
                    width="22"
                    height="22"
                    viewBox="0 0 22 22"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    class="fill-current"
                  >
                    <path
                      d="M11.0297 14.4305C12.9241 14.4305 14.4598 12.8948 14.4598 11.0004C14.4598 9.10602 12.9241 7.57031 11.0297 7.57031C9.13529 7.57031 7.59958 9.10602 7.59958 11.0004C7.59958 12.8948 9.13529 14.4305 11.0297 14.4305Z"
                    />
                    <path
                      d="M14.7554 1.8335H7.24463C4.25807 1.8335 1.83334 4.25823 1.83334 7.24479V14.6964C1.83334 17.7421 4.25807 20.1668 7.24463 20.1668H14.6962C17.7419 20.1668 20.1667 17.7421 20.1667 14.7555V7.24479C20.1667 4.25823 17.7419 1.8335 14.7554 1.8335ZM11.0296 15.4948C8.51614 15.4948 6.53496 13.4545 6.53496 11.0002C6.53496 8.54586 8.54571 6.50554 11.0296 6.50554C13.4839 6.50554 15.4946 8.54586 15.4946 11.0002C15.4946 13.4545 13.5134 15.4948 11.0296 15.4948ZM17.2393 6.91952C16.9436 7.24479 16.5 7.42221 15.9973 7.42221C15.5538 7.42221 15.1102 7.24479 14.7554 6.91952C14.4301 6.59425 14.2527 6.18027 14.2527 5.67758C14.2527 5.17489 14.4301 4.79049 14.7554 4.43565C15.0807 4.08081 15.4946 3.90339 15.9973 3.90339C16.4409 3.90339 16.914 4.08081 17.2393 4.40608C17.535 4.79049 17.7419 5.23403 17.7419 5.70715C17.7124 6.18027 17.535 6.59425 17.2393 6.91952Z"
                    />
                    <path
                      d="M16.0276 4.96777C15.6432 4.96777 15.318 5.29304 15.318 5.67745C15.318 6.06186 15.6432 6.38713 16.0276 6.38713C16.412 6.38713 16.7373 6.06186 16.7373 5.67745C16.7373 5.29304 16.4416 4.96777 16.0276 4.96777Z"
                    />
                  </svg>
                </a>
                <a
                  href="/"
                  class="px-3 text-gray-7 hover:text-white"
                >
                  <svg
                    width="22"
                    height="22"
                    viewBox="0 0 22 22"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    class="fill-current"
                  >
                    <path
                      d="M18.8065 1.8335H3.16399C2.42474 1.8335 1.83334 2.42489 1.83334 3.16414V18.8362C1.83334 19.5459 2.42474 20.1668 3.16399 20.1668H18.7473C19.4866 20.1668 20.078 19.5754 20.078 18.8362V3.13457C20.1371 2.42489 19.5457 1.8335 18.8065 1.8335ZM7.24464 17.4168H4.55379V8.69371H7.24464V17.4168ZM5.88443 7.48135C4.99733 7.48135 4.31721 6.77167 4.31721 5.91414C4.31721 5.05661 5.0269 4.34694 5.88443 4.34694C6.74196 4.34694 7.45163 5.05661 7.45163 5.91414C7.45163 6.77167 6.8011 7.48135 5.88443 7.48135ZM17.4463 17.4168H14.7554V13.1883C14.7554 12.183 14.7258 10.8523 13.336 10.8523C11.9167 10.8523 11.7097 11.976 11.7097 13.0996V17.4168H9.01884V8.69371H11.6506V9.90608H11.6801C12.0645 9.1964 12.9221 8.48672 14.2527 8.48672C17.0027 8.48672 17.5054 10.2609 17.5054 12.6856V17.4168H17.4463Z"
                    />
                  </svg>
                </a>
              </div>
            </div>
          </div>
          <div class="w-full px-4 sm:w-1/2 md:w-1/2 lg:w-2/12 xl:w-2/12">
            <div class="mb-10 w-full">
              <h4 class="mb-9 text-lg font-semibold text-white">About Us</h4>
              <ul>
                <li>
                  <router-link
                    to="/"
                    class="mb-3 inline-block text-base text-gray-7 hover:text-primary"
                  >
                    Home
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/#features"
                    class="mb-3 inline-block text-base text-gray-7 hover:text-primary"
                  >
                    Features
                  </router-link>
                </li>
                <li>
                  <router-link
                    to="/about"
                    class="mb-3 inline-block text-base text-gray-7 hover:text-primary"
                  >
                    About
                  </router-link>
                </li>
              </ul>
            </div>
          </div>
          <div class="w-full px-4 sm:w-1/2 md:w-1/2 lg:w-3/12 xl:w-2/12">
            <div class="mb-10 w-full">
              <h4 class="mb-9 text-lg font-semibold text-white">Information</h4>
              <ul>
                <li>
                  <a
                    href="/"
                    class="mb-3 inline-block text-base text-gray-7 hover:text-primary"
                  >
                    Privacy policy
                  </a>
                </li>
                <li>
                  <a
                    href="/"
                    class="mb-3 inline-block text-base text-gray-7 hover:text-primary"
                  >
                    Terms of Service
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div class="w-full px-4 sm:w-1/2 md:w-1/2 lg:w-3/12 xl:w-2/12">
            <div class="mb-10 w-full">
              <h4 class="mb-9 text-lg font-semibold text-white">
                Features
              </h4>
              <ul>
                <li>
                  <a
                    href="/"
                    class="mb-3 inline-block text-base text-gray-7 hover:text-primary"
                  >
                    LineIcons
                  </a>
                </li>
                <li>
                  <a
                    href="/"
                    class="mb-3 inline-block text-base text-gray-7 hover:text-primary"
                  >
                    Ecommerce HTML
                  </a>
                </li>
                <li>
                  <a
                    href="/"
                    class="mb-3 inline-block text-base text-gray-7 hover:text-primary"
                  >
                    TailAdmin
                  </a>
                </li>
                <li>
                  <a
                    href="/"
                    class="mb-3 inline-block text-base text-gray-7 hover:text-primary"
                  >
                    PlainAdmin
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      
    </footer>
    <!-- ====== Footer Section End -->




</template>

<style scoped>

*,
::before,
::after {
  box-sizing: border-box;
  /* 1 */
  border-width: 0;
  /* 2 */
  border-style: solid;
  /* 2 */
  border-color: #e5e7eb;
  /* 2 */
}

::before,
::after {
  --tw-content: '';
}

/*
1. Use a consistent sensible line-height in all browsers.
2. Prevent adjustments of font size after orientation changes in iOS.
3. Use a more readable tab size.
4. Use the user's configured `sans` font-family by default.
5. Use the user's configured `sans` font-feature-settings by default.
6. Use the user's configured `sans` font-variation-settings by default.
*/

html {
  line-height: 1.5;
  /* 1 */
  -webkit-text-size-adjust: 100%;
  /* 2 */
  -moz-tab-size: 4;
  /* 3 */
  -o-tab-size: 4;
     tab-size: 4;
  /* 3 */
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  /* 4 */
  font-feature-settings: normal;
  /* 5 */
  font-variation-settings: normal;
  /* 6 */
}

/*
1. Remove the margin in all browsers.
2. Inherit line-height from `html` so users can set them as a class directly on the `html` element.
*/

body {
  margin: 0;
  /* 1 */
  line-height: inherit;
  /* 2 */
}

/*
1. Add the correct height in Firefox.
2. Correct the inheritance of border color in Firefox. (https://bugzilla.mozilla.org/show_bug.cgi?id=190655)
3. Ensure horizontal rules are visible by default.
*/

hr {
  height: 0;
  /* 1 */
  color: inherit;
  /* 2 */
  border-top-width: 1px;
  /* 3 */
}

/*
Add the correct text decoration in Chrome, Edge, and Safari.
*/

abbr:where([title]) {
  -webkit-text-decoration: underline dotted;
          text-decoration: underline dotted;
}

/*
Remove the default font size and weight for headings.
*/

h1,
h2,
h3,
h4,
h5,
h6 {
  font-size: inherit;
  font-weight: inherit;
}

/*
Reset links to optimize for opt-in styling instead of opt-out.
*/

a {
  color: inherit;
  text-decoration: inherit;
}

/*
Add the correct font weight in Edge and Safari.
*/

b,
strong {
  font-weight: bolder;
}

/*
1. Use the user's configured `mono` font family by default.
2. Correct the odd `em` font sizing in all browsers.
*/

code,
kbd,
samp,
pre {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  /* 1 */
  font-size: 1em;
  /* 2 */
}

/*
Add the correct font size in all browsers.
*/

small {
  font-size: 80%;
}

/*
Prevent `sub` and `sup` elements from affecting the line height in all browsers.
*/

sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sub {
  bottom: -0.25em;
}

sup {
  top: -0.5em;
}

/*
1. Remove text indentation from table contents in Chrome and Safari. (https://bugs.chromium.org/p/chromium/issues/detail?id=999088, https://bugs.webkit.org/show_bug.cgi?id=201297)
2. Correct table border color inheritance in all Chrome and Safari. (https://bugs.chromium.org/p/chromium/issues/detail?id=935729, https://bugs.webkit.org/show_bug.cgi?id=195016)
3. Remove gaps between table borders by default.
*/

table {
  text-indent: 0;
  /* 1 */
  border-color: inherit;
  /* 2 */
  border-collapse: collapse;
  /* 3 */
}

/*
1. Change the font styles in all browsers.
2. Remove the margin in Firefox and Safari.
3. Remove default padding in all browsers.
*/

button,
input,
optgroup,
select,
textarea {
  font-family: inherit;
  /* 1 */
  font-feature-settings: inherit;
  /* 1 */
  font-variation-settings: inherit;
  /* 1 */
  font-size: 100%;
  /* 1 */
  font-weight: inherit;
  /* 1 */
  line-height: inherit;
  /* 1 */
  color: inherit;
  /* 1 */
  margin: 0;
  /* 2 */
  padding: 0;
  /* 3 */
}

/*
Remove the inheritance of text transform in Edge and Firefox.
*/

button,
select {
  text-transform: none;
}

/*
1. Correct the inability to style clickable types in iOS and Safari.
2. Remove default button styles.
*/

button,
[type='button'],
[type='reset'],
[type='submit'] {
  -webkit-appearance: button;
  /* 1 */
  background-color: transparent;
  /* 2 */
  background-image: none;
  /* 2 */
}

/*
Use the modern Firefox focus style for all focusable elements.
*/

:-moz-focusring {
  outline: auto;
}

/*
Remove the additional `:invalid` styles in Firefox. (https://github.com/mozilla/gecko-dev/blob/2f9eacd9d3d995c937b4251a5557d95d494c9be1/layout/style/res/forms.css#L728-L737)
*/

:-moz-ui-invalid {
  box-shadow: none;
}

/*
Add the correct vertical alignment in Chrome and Firefox.
*/

progress {
  vertical-align: baseline;
}

/*
Correct the cursor style of increment and decrement buttons in Safari.
*/

::-webkit-inner-spin-button,
::-webkit-outer-spin-button {
  height: auto;
}

/*
1. Correct the odd appearance in Chrome and Safari.
2. Correct the outline style in Safari.
*/

[type='search'] {
  -webkit-appearance: textfield;
  /* 1 */
  outline-offset: -2px;
  /* 2 */
}

/*
Remove the inner padding in Chrome and Safari on macOS.
*/

::-webkit-search-decoration {
  -webkit-appearance: none;
}

/*
1. Correct the inability to style clickable types in iOS and Safari.
2. Change font properties to `inherit` in Safari.
*/

::-webkit-file-upload-button {
  -webkit-appearance: button;
  /* 1 */
  font: inherit;
  /* 2 */
}

/*
Add the correct display in Chrome and Safari.
*/

summary {
  display: list-item;
}

/*
Removes the default spacing and border for appropriate elements.
*/

blockquote,
dl,
dd,
h1,
h2,
h3,
h4,
h5,
h6,
hr,
figure,
p,
pre {
  margin: 0;
}

fieldset {
  margin: 0;
  padding: 0;
}

legend {
  padding: 0;
}

ol,
ul,
menu {
  list-style: none;
  margin: 0;
  padding: 0;
}

/*
Reset default styling for dialogs.
*/

dialog {
  padding: 0;
}

/*
Prevent resizing textareas horizontally by default.
*/

textarea {
  resize: vertical;
}

/*
1. Reset the default placeholder opacity in Firefox. (https://github.com/tailwindlabs/tailwindcss/issues/3300)
2. Set the default placeholder color to the user's configured gray 400 color.
*/

input::-moz-placeholder, textarea::-moz-placeholder {
  opacity: 1;
  /* 1 */
  color: #9ca3af;
  /* 2 */
}

input::placeholder,
textarea::placeholder {
  opacity: 1;
  /* 1 */
  color: #9ca3af;
  /* 2 */
}

/*
Set the default cursor for buttons.
*/

button,
[role="button"] {
  cursor: pointer;
}

/*
Make sure disabled buttons don't get the pointer cursor.
*/

:disabled {
  cursor: default;
}

/*
1. Make replaced elements `display: block` by default. (https://github.com/mozdevs/cssremedy/issues/14)
2. Add `vertical-align: middle` to align replaced elements more sensibly by default. (https://github.com/jensimmons/cssremedy/issues/14#issuecomment-634934210)
   This can trigger a poorly considered lint error in some tools but is included by design.
*/

img,
svg,
video,
canvas,
audio,
iframe,
embed,
object {
  display: block;
  /* 1 */
  vertical-align: middle;
  /* 2 */
}

/*
Constrain images and videos to the parent width and preserve their intrinsic aspect ratio. (https://github.com/mozdevs/cssremedy/issues/14)
*/

img,
video {
  max-width: 100%;
  height: auto;
}

/* Make elements with the HTML hidden attribute stay hidden by default */

[hidden] {
  display: none;
}

body {
  font-family: "Inter", sans-serif;
}

*, ::before, ::after{
  --tw-border-spacing-x: 0;
  --tw-border-spacing-y: 0;
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  --tw-pan-x:  ;
  --tw-pan-y:  ;
  --tw-pinch-zoom:  ;
  --tw-scroll-snap-strictness: proximity;
  --tw-gradient-from-position:  ;
  --tw-gradient-via-position:  ;
  --tw-gradient-to-position:  ;
  --tw-ordinal:  ;
  --tw-slashed-zero:  ;
  --tw-numeric-figure:  ;
  --tw-numeric-spacing:  ;
  --tw-numeric-fraction:  ;
  --tw-ring-inset:  ;
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgb(59 130 246 / 0.5);
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  --tw-blur:  ;
  --tw-brightness:  ;
  --tw-contrast:  ;
  --tw-grayscale:  ;
  --tw-hue-rotate:  ;
  --tw-invert:  ;
  --tw-saturate:  ;
  --tw-sepia:  ;
  --tw-drop-shadow:  ;
  --tw-backdrop-blur:  ;
  --tw-backdrop-brightness:  ;
  --tw-backdrop-contrast:  ;
  --tw-backdrop-grayscale:  ;
  --tw-backdrop-hue-rotate:  ;
  --tw-backdrop-invert:  ;
  --tw-backdrop-opacity:  ;
  --tw-backdrop-saturate:  ;
  --tw-backdrop-sepia:  ;
}

::backdrop{
  --tw-border-spacing-x: 0;
  --tw-border-spacing-y: 0;
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  --tw-pan-x:  ;
  --tw-pan-y:  ;
  --tw-pinch-zoom:  ;
  --tw-scroll-snap-strictness: proximity;
  --tw-gradient-from-position:  ;
  --tw-gradient-via-position:  ;
  --tw-gradient-to-position:  ;
  --tw-ordinal:  ;
  --tw-slashed-zero:  ;
  --tw-numeric-figure:  ;
  --tw-numeric-spacing:  ;
  --tw-numeric-fraction:  ;
  --tw-ring-inset:  ;
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgb(59 130 246 / 0.5);
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  --tw-blur:  ;
  --tw-brightness:  ;
  --tw-contrast:  ;
  --tw-grayscale:  ;
  --tw-hue-rotate:  ;
  --tw-invert:  ;
  --tw-saturate:  ;
  --tw-sepia:  ;
  --tw-drop-shadow:  ;
  --tw-backdrop-blur:  ;
  --tw-backdrop-brightness:  ;
  --tw-backdrop-contrast:  ;
  --tw-backdrop-grayscale:  ;
  --tw-backdrop-hue-rotate:  ;
  --tw-backdrop-invert:  ;
  --tw-backdrop-opacity:  ;
  --tw-backdrop-saturate:  ;
  --tw-backdrop-sepia:  ;
}

.container{
  width: 100%;
  margin-right: auto;
  margin-left: auto;
  padding-right: 16px;
  padding-left: 16px;
}

@media (min-width: 540px){
  .container{
    max-width: 540px;
  }
}

@media (min-width: 720px){
  .container{
    max-width: 720px;
  }
}

@media (min-width: 960px){
  .container{
    max-width: 960px;
  }
}

@media (min-width: 1140px){
  .container{
    max-width: 1140px;
  }
}

@media (min-width: 1320px){
  .container{
    max-width: 1320px;
  }
}

.sr-only{
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.visible{
  visibility: visible;
}

.static{
  position: static;
}

.fixed{
  position: fixed;
}

.absolute{
  position: absolute;
}

.relative{
  position: relative;
}

.sticky{
  position: sticky;
}

.-left-9{
  left: -2.25rem;
}

.-right-6{
  right: -1.5rem;
}

.-top-6{
  top: -1.5rem;
}

.bottom-0{
  bottom: 0px;
}

.bottom-1{
  bottom: 0.25rem;
}

.bottom-4{
  bottom: 1rem;
}

.bottom-8{
  bottom: 2rem;
}

.left-0{
  left: 0px;
}

.left-1{
  left: 0.25rem;
}

.left-4{
  left: 1rem;
}

.left-auto{
  left: auto;
}

.right-0{
  right: 0px;
}

.right-1{
  right: 0.25rem;
}

.right-4{
  right: 1rem;
}

.right-8{
  right: 2rem;
}

.right-\[-50px\]{
  right: -50px;
}

.top-0{
  top: 0px;
}

.top-1{
  top: 0.25rem;
}

.top-1\/2{
  top: 50%;
}

.top-4{
  top: 1rem;
}

.top-\[60px\]{
  top: 60px;
}

.top-full{
  top: 100%;
}

.-z-10{
  z-index: -10;
}

.-z-\[1\]{
  z-index: -1;
}

.z-10{
  z-index: 10;
}

.z-20{
  z-index: 20;
}

.z-40{
  z-index: 40;
}

.z-\[-1\]{
  z-index: -1;
}

.z-\[999\]{
  z-index: 999;
}

.-m-5{
  margin: -1.25rem;
}

.-mx-1{
  margin-left: -0.25rem;
  margin-right: -0.25rem;
}

.-mx-2{
  margin-left: -0.5rem;
  margin-right: -0.5rem;
}

.-mx-3{
  margin-left: -0.75rem;
  margin-right: -0.75rem;
}

.-mx-4{
  margin-left: -1rem;
  margin-right: -1rem;
}

.mx-8{
  margin-left: 2rem;
  margin-right: 2rem;
}

.mx-auto{
  margin-left: auto;
  margin-right: auto;
}

.my-1{
  margin-top: 0.25rem;
  margin-bottom: 0.25rem;
}

.my-\[6px\]{
  margin-top: 6px;
  margin-bottom: 6px;
}

.-ml-1{
  margin-left: -0.25rem;
}

.mb-0{
  margin-bottom: 0px;
}

.mb-1{
  margin-bottom: 0.25rem;
}

.mb-10{
  margin-bottom: 2.5rem;
}

.mb-11{
  margin-bottom: 2.75rem;
}

.mb-12{
  margin-bottom: 3rem;
}

.mb-2{
  margin-bottom: 0.5rem;
}

.mb-2\.5{
  margin-bottom: 0.625rem;
}

.mb-3{
  margin-bottom: 0.75rem;
}

.mb-4{
  margin-bottom: 1rem;
}

.mb-5{
  margin-bottom: 1.25rem;
}

.mb-6{
  margin-bottom: 1.5rem;
}

.mb-7{
  margin-bottom: 1.75rem;
}

.mb-8{
  margin-bottom: 2rem;
}

.mb-9{
  margin-bottom: 2.25rem;
}

.mb-\[14px\]{
  margin-bottom: 14px;
}

.mb-\[18px\]{
  margin-bottom: 18px;
}

.mb-\[22px\]{
  margin-bottom: 22px;
}

.mb-\[30px\]{
  margin-bottom: 30px;
}

.mb-\[50px\]{
  margin-bottom: 50px;
}

.mb-\[60px\]{
  margin-bottom: 60px;
}

.mb-\[6px\]{
  margin-bottom: 6px;
}

.ml-2{
  margin-left: 0.5rem;
}

.mr-3{
  margin-right: 0.75rem;
}

.mr-4{
  margin-right: 1rem;
}

.mr-5{
  margin-right: 1.25rem;
}

.mr-6{
  margin-right: 1.5rem;
}

.mt-0{
  margin-top: 0px;
}

.mt-0\.5{
  margin-top: 0.125rem;
}

.mt-1{
  margin-top: 0.25rem;
}

.mt-12{
  margin-top: 3rem;
}

.mt-14{
  margin-top: 3.5rem;
}

.mt-16{
  margin-top: 4rem;
}

.mt-8{
  margin-top: 2rem;
}

.mt-\[60px\]{
  margin-top: 60px;
}

.mt-\[6px\]{
  margin-top: 6px;
}

.block{
  display: block;
}

.inline-block{
  display: inline-block;
}

.flex{
  display: flex;
}

.inline-flex{
  display: inline-flex;
}

.grid{
  display: grid;
}

.hidden{
  display: none;
}

.h-1\/2{
  height: 50%;
}

.h-10{
  height: 2.5rem;
}

.h-11{
  height: 2.75rem;
}

.h-20{
  height: 5rem;
}

.h-3{
  height: 0.75rem;
}

.h-4{
  height: 1rem;
}

.h-\[120px\]{
  height: 120px;
}

.h-\[2px\]{
  height: 2px;
}

.h-\[300px\]{
  height: 300px;
}

.h-\[34px\]{
  height: 34px;
}

.h-\[50px\]{
  height: 50px;
}

.h-\[70px\]{
  height: 70px;
}

.h-full{
  height: 100%;
}

.h-px{
  height: 1px;
}

.w-10{
  width: 2.5rem;
}

.w-20{
  width: 5rem;
}

.w-3{
  width: 0.75rem;
}

.w-60{
  width: 15rem;
}

.w-\[120px\]{
  width: 120px;
}

.w-\[250px\]{
  width: 250px;
}

.w-\[30px\]{
  width: 30px;
}

.w-\[330px\]{
  width: 330px;
}

.w-\[34px\]{
  width: 34px;
}

.w-\[50px\]{
  width: 50px;
}

.w-\[70px\]{
  width: 70px;
}

.w-full{
  width: 100%;
}

.w-px{
  width: 1px;
}

.max-w-\[160px\]{
  max-width: 160px;
}

.max-w-\[180px\]{
  max-width: 180px;
}

.max-w-\[250px\]{
  max-width: 250px;
}

.max-w-\[260px\]{
  max-width: 260px;
}

.max-w-\[270px\]{
  max-width: 270px;
}

.max-w-\[370px\]{
  max-width: 370px;
}

.max-w-\[485px\]{
  max-width: 485px;
}

.max-w-\[50px\]{
  max-width: 50px;
}

.max-w-\[510px\]{
  max-width: 510px;
}

.max-w-\[515px\]{
  max-width: 515px;
}

.max-w-\[520px\]{
  max-width: 520px;
}

.max-w-\[525px\]{
  max-width: 525px;
}

.max-w-\[530px\]{
  max-width: 530px;
}

.max-w-\[540px\]{
  max-width: 540px;
}

.max-w-\[570px\]{
  max-width: 570px;
}

.max-w-\[600px\]{
  max-width: 600px;
}

.max-w-\[780px\]{
  max-width: 780px;
}

.max-w-\[80px\]{
  max-width: 80px;
}

.max-w-\[845px\]{
  max-width: 845px;
}

.max-w-\[88px\]{
  max-width: 88px;
}

.max-w-full{
  max-width: 100%;
}

.-translate-y-1\/2{
  --tw-translate-y: -50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.-rotate-90{
  --tw-rotate: -90deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-180{
  --tw-rotate: 180deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-45{
  --tw-rotate: 45deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.rotate-\[25deg\]{
  --tw-rotate: 25deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.transform{
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.cursor-pointer{
  cursor: pointer;
}

.resize-none{
  resize: none;
}

.resize{
  resize: both;
}

.flex-col{
  flex-direction: column;
}

.flex-wrap{
  flex-wrap: wrap;
}

.items-end{
  align-items: flex-end;
}

.items-center{
  align-items: center;
}

.items-stretch{
  align-items: stretch;
}

.justify-end{
  justify-content: flex-end;
}

.justify-center{
  justify-content: center;
}

.justify-between{
  justify-content: space-between;
}

.gap-1{
  gap: 0.25rem;
}

.gap-3{
  gap: 0.75rem;
}

.gap-4{
  gap: 1rem;
}

.gap-5{
  gap: 1.25rem;
}

.gap-8{
  gap: 2rem;
}

.gap-\[10px\]{
  gap: 10px;
}

.gap-\[14px\]{
  gap: 14px;
}

.gap-\[22px\]{
  gap: 22px;
}

.gap-\[2px\]{
  gap: 2px;
}

.overflow-hidden{
  overflow: hidden;
}

.scroll-smooth{
  scroll-behavior: smooth;
}

.rounded{
  border-radius: 0.25rem;
}

.rounded-\[10px\]{
  border-radius: 10px;
}

.rounded-\[14px\]{
  border-radius: 14px;
}

.rounded-\[5px\]{
  border-radius: 5px;
}

.rounded-full{
  border-radius: 9999px;
}

.rounded-lg{
  border-radius: 0.5rem;
}

.rounded-md{
  border-radius: 0.375rem;
}

.rounded-sm{
  border-radius: 0.125rem;
}

.rounded-xl{
  border-radius: 0.75rem;
}

.rounded-t-xl{
  border-top-left-radius: 0.75rem;
  border-top-right-radius: 0.75rem;
}

.rounded-bl-md{
  border-bottom-left-radius: 0.375rem;
}

.rounded-tl-md{
  border-top-left-radius: 0.375rem;
}

.rounded-tr-xl{
  border-top-right-radius: 0.75rem;
}

.border{
  border-width: 1px;
}

.border-0{
  border-width: 0px;
}

.border-b{
  border-bottom-width: 1px;
}

.border-l{
  border-left-width: 1px;
}

.border-t{
  border-top-width: 1px;
}

.border-\[\#8890A4\]{
  --tw-border-opacity: 1;
  border-color: rgb(136 144 164 / var(--tw-border-opacity));
}

.border-\[\#f1f1f1\]{
  --tw-border-opacity: 1;
  border-color: rgb(241 241 241 / var(--tw-border-opacity));
}

.border-primary{
  --tw-border-opacity: 1;
  border-color: rgb(55 88 249 / var(--tw-border-opacity));
}

.border-stroke{
  --tw-border-opacity: 1;
  border-color: rgb(223 228 234 / var(--tw-border-opacity));
}

.border-transparent{
  border-color: transparent;
}

.border-white{
  --tw-border-opacity: 1;
  border-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.border-opacity-40{
  --tw-border-opacity: 0.4;
}

.bg-\[\#090E34\]{
  --tw-bg-opacity: 1;
  background-color: rgb(9 14 52 / var(--tw-bg-opacity));
}

.bg-\[\#1C9CEA\]{
  --tw-bg-opacity: 1;
  background-color: rgb(28 156 234 / var(--tw-bg-opacity));
}

.bg-\[\#4064AC\]{
  --tw-bg-opacity: 1;
  background-color: rgb(64 100 172 / var(--tw-bg-opacity));
}

.bg-\[\#D64937\]{
  --tw-bg-opacity: 1;
  background-color: rgb(214 73 55 / var(--tw-bg-opacity));
}

.bg-\[\#E9F9FF\]{
  --tw-bg-opacity: 1;
  background-color: rgb(233 249 255 / var(--tw-bg-opacity));
}

.bg-\[\#F4F7FF\]{
  --tw-bg-opacity: 1;
  background-color: rgb(244 247 255 / var(--tw-bg-opacity));
}

.bg-dark{
  --tw-bg-opacity: 1;
  background-color: rgb(97 25 40 / var(--tw-bg-opacity));
}

.bg-gray-1{
  --tw-bg-opacity: 1;
  background-color: rgb(249 250 251 / var(--tw-bg-opacity));
}


.bg-stroke{
  --tw-bg-opacity: 1;
  background-color: rgb(223 228 234 / var(--tw-bg-opacity));
}

.bg-transparent{
  background-color: transparent;
}

.bg-white{
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}

.bg-white\/10{
  background-color: rgb(255 255 255 / 0.1);
}

.bg-white\/\[0\.12\]{
  background-color: rgb(255 255 255 / 0.12);
}

.bg-opacity-20{
  --tw-bg-opacity: 0.2;
}

.bg-gradient-to-r{
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}

.bg-gradient-to-t{
  background-image: linear-gradient(to top, var(--tw-gradient-stops));
}

.from-dark-700{
  --tw-gradient-from: #090e34b3 var(--tw-gradient-from-position);
  --tw-gradient-to: rgb(9 14 52 / 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}

.from-stroke\/0{
  --tw-gradient-from: rgb(223 228 234 / 0) var(--tw-gradient-from-position);
  --tw-gradient-to: rgb(223 228 234 / 0) var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}

.via-stroke{
  --tw-gradient-to: rgb(223 228 234 / 0)  var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), #DFE4EA var(--tw-gradient-via-position), var(--tw-gradient-to);
}

.to-stroke\/0{
  --tw-gradient-to: rgb(223 228 234 / 0) var(--tw-gradient-to-position);
}

.to-transparent{
  --tw-gradient-to: transparent var(--tw-gradient-to-position);
}

.fill-current{
  fill: currentColor;
}

.stroke-current{
  stroke: currentColor;
}

.object-cover{
  -o-object-fit: cover;
     object-fit: cover;
}

.object-center{
  -o-object-position: center;
     object-position: center;
}

.p-3{
  padding: 0.75rem;
}

.p-4{
  padding: 1rem;
}

.p-5{
  padding: 1.25rem;
}

.px-1{
  padding-left: 0.25rem;
  padding-right: 0.25rem;
}

.px-10{
  padding-left: 2.5rem;
  padding-right: 2.5rem;
}

.px-11{
  padding-left: 2.75rem;
  padding-right: 2.75rem;
}

.px-2{
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}

.px-3{
  padding-left: 0.75rem;
  padding-right: 0.75rem;
}

.px-4{
  padding-left: 1rem;
  padding-right: 1rem;
}

.px-5{
  padding-left: 1.25rem;
  padding-right: 1.25rem;
}

.px-6{
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}

.px-7{
  padding-left: 1.75rem;
  padding-right: 1.75rem;
}

.px-8{
  padding-left: 2rem;
  padding-right: 2rem;
}

.px-\[14px\]{
  padding-left: 14px;
  padding-right: 14px;
}

.px-\[22px\]{
  padding-left: 22px;
  padding-right: 22px;
}

.py-0{
  padding-top: 0px;
  padding-bottom: 0px;
}

.py-0\.5{
  padding-top: 0.125rem;
  padding-bottom: 0.125rem;
}

.py-10{
  padding-top: 2.5rem;
  padding-bottom: 2.5rem;
}

.py-12{
  padding-top: 3rem;
  padding-bottom: 3rem;
}

.py-14{
  padding-top: 3.5rem;
  padding-bottom: 3.5rem;
}

.py-2{
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.py-20{
  padding-top: 5rem;
  padding-bottom: 5rem;
}

.py-3{
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}

.py-5{
  padding-top: 1.25rem;
  padding-bottom: 1.25rem;
}

.py-8{
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.py-\[10px\]{
  padding-top: 10px;
  padding-bottom: 10px;
}

.py-\[14px\]{
  padding-top: 14px;
  padding-bottom: 14px;
}

.py-\[30px\]{
  padding-top: 30px;
  padding-bottom: 30px;
}

.py-\[5px\]{
  padding-top: 5px;
  padding-bottom: 5px;
}

.py-\[60px\]{
  padding-top: 60px;
  padding-bottom: 60px;
}

.py-\[6px\]{
  padding-top: 6px;
  padding-bottom: 6px;
}

.pb-10{
  padding-bottom: 2.5rem;
}

.pb-12{
  padding-bottom: 3rem;
}

.pb-20{
  padding-bottom: 5rem;
}

.pb-3{
  padding-bottom: 0.75rem;
}

.pb-4{
  padding-bottom: 1rem;
}

.pb-5{
  padding-bottom: 1.25rem;
}

.pb-8{
  padding-bottom: 2rem;
}

.pb-\[60px\]{
  padding-bottom: 60px;
}

.pr-16{
  padding-right: 4rem;
}

.pt-12{
  padding-top: 3rem;
}

.pt-20{
  padding-top: 5rem;
}

.pt-\[120px\]{
  padding-top: 120px;
}

.text-center{
  text-align: center;
}

.text-2xl{
  font-size: 1.5rem;
  line-height: 2rem;
}

.text-3xl{
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-4xl{
  font-size: 2.25rem;
  line-height: 2.5rem;
}

.text-5xl{
  font-size: 3rem;
  line-height: 1;
}

.text-\[28px\]{
  font-size: 28px;
}

.text-\[32px\]{
  font-size: 32px;
}

.text-\[35px\]{
  font-size: 35px;
}

.text-base{
  font-size: 1rem;
  line-height: 1.5rem;
}

.text-lg{
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-sm{
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.text-xl{
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.text-xs{
  font-size: 0.75rem;
  line-height: 1rem;
}

.font-bold{
  font-weight: 700;
}

.font-extrabold{
  font-weight: 800;
}

.font-medium{
  font-weight: 500;
}

.font-normal{
  font-weight: 400;
}

.font-semibold{
  font-weight: 600;
}

.italic{
  font-style: italic;
}

.leading-\[1\.14\]{
  line-height: 1.14;
}

.leading-\[1\.2\]{
  line-height: 1.2;
}

.leading-\[1\.5\]{
  line-height: 1.5;
}

.leading-\[28px\]{
  line-height: 28px;
}

.leading-\[40px\]{
  line-height: 40px;
}

.leading-loose{
  line-height: 2;
}

.leading-relaxed{
  line-height: 1.625;
}

.leading-snug{
  line-height: 1.375;
}

.leading-tight{
  line-height: 1.25;
}

.-tracking-\[2px\]{
  letter-spacing: -2px;
}

.text-body-color{
  --tw-text-opacity: 1;
  color: rgb(99 115 129 / var(--tw-text-opacity));
}

.text-body-secondary{
  --tw-text-opacity: 1;
  color: rgb(136 153 168 / var(--tw-text-opacity));
}

.text-dark{
  --tw-text-opacity: 1;
  color: rgb(17 25 40 / var(--tw-text-opacity));
}

.text-dark-3{
  --tw-text-opacity: 1;
  color: rgb(55 65 81 / var(--tw-text-opacity));
}

.text-dark-6{
  --tw-text-opacity: 1;
  color: rgb(156 163 175 / var(--tw-text-opacity));
}

.text-gray-1{
  --tw-text-opacity: 1;
  color: rgb(249 250 251 / var(--tw-text-opacity));
}

.text-gray-7{
  --tw-text-opacity: 1;
  color: rgb(206 212 218 / var(--tw-text-opacity));
}

.text-primary{
  --tw-text-opacity: 1;
  color: rgb(55 88 249 / var(--tw-text-opacity));
}

.text-white{
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

.text-white\/60{
  color: rgb(255 255 255 / 0.6);
}

.text-opacity-70{
  --tw-text-opacity: 0.7;
}

.opacity-0{
  opacity: 0;
}

.shadow{
  --tw-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  --tw-shadow-colored: 0 1px 3px 0 var(--tw-shadow-color), 0 1px 2px -1px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-1{
  --tw-shadow: 0px 1px 3px 0px rgba(166, 175, 195, 0.40);
  --tw-shadow-colored: 0px 1px 3px 0px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-2{
  --tw-shadow: 0px 5px 12px 0px rgba(0, 0, 0, 0.10);
  --tw-shadow-colored: 0px 5px 12px 0px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-form{
  --tw-shadow: 0px 1px 55px -11px rgba(0, 0, 0, 0.01);
  --tw-shadow-colored: 0px 1px 55px -11px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-lg{
  --tw-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-md{
  --tw-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-pricing{
  --tw-shadow: 0px 0px 40px 0px rgba(0, 0, 0, 0.08);
  --tw-shadow-colored: 0px 0px 40px 0px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.shadow-testimonial{
  --tw-shadow: 0px 10px 20px 0px rgba(92, 115, 160, 0.07);
  --tw-shadow-colored: 0px 10px 20px 0px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.outline-none{
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.ring-primary{
  --tw-ring-opacity: 1;
  --tw-ring-color: rgb(55 88 249 / var(--tw-ring-opacity));
}

.blur{
  --tw-blur: blur(8px);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.invert{
  --tw-invert: invert(100%);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.filter{
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.transition{
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter;
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.transition-\[top\]{
  transition-property: top;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.transition-all{
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.duration-300{
  transition-duration: 300ms;
}

.ease-in-out{
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

.sticky{
  position: fixed;
  z-index: 9999;
  background-color: rgb(255 255 255 / 0.8);
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter;
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

:is(.dark .sticky){
  background-color: rgb(17 25 40 / 0.8);
}

.sticky {
  -webkit-backdrop-filter: blur(5px);
          backdrop-filter: blur(5px);
  box-shadow: inset 0 -1px 0 0 rgba(0, 0, 0, 0.1);
}

.sticky .navbar-logo{
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.sticky #navbarToggler span{
  --tw-bg-opacity: 1;
  background-color: rgb(17 25 40 / var(--tw-bg-opacity));
}

:is(.dark .sticky #navbarToggler span){
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}

.sticky #navbarCollapse li > a{
  --tw-text-opacity: 1;
  color: rgb(17 25 40 / var(--tw-text-opacity));
}

.sticky #navbarCollapse li > a:hover{
  --tw-text-opacity: 1;
  color: rgb(55 88 249 / var(--tw-text-opacity));
  opacity: 1;
}

:is(.dark .sticky #navbarCollapse li > a){
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

:is(.dark .sticky #navbarCollapse li > a:hover){
  --tw-text-opacity: 1;
  color: rgb(55 88 249 / var(--tw-text-opacity));
}

#navbarCollapse li .ud-menu-scroll.active{
  opacity: 0.7;
}

.sticky #navbarCollapse li .ud-menu-scroll.active{
  --tw-text-opacity: 1;
  color: rgb(55 88 249 / var(--tw-text-opacity));
  opacity: 1;
}

.sticky .loginBtn{
  --tw-text-opacity: 1;
  color: rgb(17 25 40 / var(--tw-text-opacity));
}

.sticky .loginBtn:hover{
  --tw-text-opacity: 1;
  color: rgb(55 88 249 / var(--tw-text-opacity));
  opacity: 1;
}

:is(.dark .sticky .loginBtn){
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

:is(.dark .sticky .loginBtn:hover){
  --tw-text-opacity: 1;
  color: rgb(55 88 249 / var(--tw-text-opacity));
}

.sticky .signUpBtn{
  --tw-bg-opacity: 1;
  background-color: #3C50E0;
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

.sticky .signUpBtn:hover{
  --tw-bg-opacity: 1;
  background-color: rgb(27 68 200 / var(--tw-bg-opacity));
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

.sticky #themeSwitcher ~ span{
  --tw-text-opacity: 1;
  color: rgb(17 25 40 / var(--tw-text-opacity));
}

:is(.dark .sticky #themeSwitcher ~ span){
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

.navbarTogglerActive > span:nth-child(1){
  top: 7px;
  --tw-rotate: 45deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.navbarTogglerActive > span:nth-child(2){
  opacity: 0;
}

.navbarTogglerActive > span:nth-child(3){
  top: -8px;
  --tw-rotate: 135deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.common-carousel .swiper-button-next:after,
.common-carousel .swiper-button-prev:after{
  display: none;
}

.common-carousel .swiper-button-next,
.common-carousel .swiper-button-prev{
  position: static !important;
  margin: 0px;
  height: 3rem;
  width: 3rem;
  border-radius: 0.5rem;
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
  --tw-text-opacity: 1;
  color: rgb(17 25 40 / var(--tw-text-opacity));
  --tw-shadow: 0px 8px 15px 0px rgba(72, 72, 138, 0.08);
  --tw-shadow-colored: 0px 8px 15px 0px var(--tw-shadow-color);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  transition-duration: 200ms;
  transition-timing-function: cubic-bezier(0, 0, 0.2, 1);
}

.common-carousel .swiper-button-next:hover,
.common-carousel .swiper-button-prev:hover{
  --tw-bg-opacity: 1;
  background-color: rgb(55 88 249 / var(--tw-bg-opacity));
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

:is(.dark .common-carousel .swiper-button-next),:is(.dark 
.common-carousel .swiper-button-prev){
  --tw-bg-opacity: 1;
  background-color: rgb(17 25 40 / var(--tw-bg-opacity));
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

.common-carousel .swiper-button-next svg,
.common-carousel .swiper-button-prev svg{
  height: auto;
  width: auto;
}

.placeholder\:text-body-color\/60::-moz-placeholder{
  color: rgb(99 115 129 / 0.6);
}

.placeholder\:text-body-color\/60::placeholder{
  color: rgb(99 115 129 / 0.6);
}

.placeholder\:text-dark-6::-moz-placeholder{
  --tw-text-opacity: 1;
  color: rgb(156 163 175 / var(--tw-text-opacity));
}

.placeholder\:text-dark-6::placeholder{
  --tw-text-opacity: 1;
  color: rgb(156 163 175 / var(--tw-text-opacity));
}

.placeholder\:text-white\/60::-moz-placeholder{
  color: rgb(255 255 255 / 0.6);
}

.placeholder\:text-white\/60::placeholder{
  color: rgb(255 255 255 / 0.6);
}

.hover\:border-blue-dark:hover{
  --tw-border-opacity: 1;
  border-color: rgb(27 68 200 / var(--tw-border-opacity));
}

.hover\:border-primary:hover{
  --tw-border-opacity: 1;
  border-color: rgb(55 88 249 / var(--tw-border-opacity));
}

.hover\:bg-\[\#0BB489\]:hover{
  --tw-bg-opacity: 1;
  background-color: rgb(11 180 137 / var(--tw-bg-opacity));
}

.hover\:bg-blue-dark:hover{
  --tw-bg-opacity: 1;
  background-color: rgb(27 68 200 / var(--tw-bg-opacity));
}

.hover\:bg-dark:hover{
  --tw-bg-opacity: 1;
  background-color: rgb(17 25 40 / var(--tw-bg-opacity));
}

.hover\:bg-gray-2:hover{
  --tw-bg-opacity: 1;
  background-color: rgb(243 244 246 / var(--tw-bg-opacity));
}

.hover\:bg-primary:hover{
  --tw-bg-opacity: 1;
  background-color: rgb(55 88 249 / var(--tw-bg-opacity));
}

.hover\:bg-white:hover{
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}

.hover\:bg-opacity-100:hover{
  --tw-bg-opacity: 1;
}

.hover\:bg-opacity-90:hover{
  --tw-bg-opacity: 0.9;
}

.hover\:text-body-color:hover{
  --tw-text-opacity: 1;
  color: rgb(99 115 129 / var(--tw-text-opacity));
}

.hover\:text-dark:hover{
  --tw-text-opacity: 1;
  color: rgb(17 25 40 / var(--tw-text-opacity));
}

.hover\:text-primary:hover{
  --tw-text-opacity: 1;
  color: rgb(55 88 249 / var(--tw-text-opacity));
}

.hover\:text-white:hover{
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

.hover\:underline:hover{
  text-decoration-line: underline;
}

.hover\:opacity-70:hover{
  opacity: 0.7;
}

.focus\:border-primary:focus{
  --tw-border-opacity: 1;
  border-color: rgb(55 88 249 / var(--tw-border-opacity));
}

.focus\:border-white:focus{
  --tw-border-opacity: 1;
  border-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.focus\:outline-none:focus{
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus{
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

.focus-visible\:shadow-none:focus-visible{
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

.group:hover .group-hover\:rotate-45{
  --tw-rotate: 45deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.group:hover .group-hover\:rotate-6{
  --tw-rotate: 6deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.group:hover .group-hover\:scale-125{
  --tw-scale-x: 1.25;
  --tw-scale-y: 1.25;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.group:hover .group-hover\:text-primary{
  --tw-text-opacity: 1;
  color: rgb(55 88 249 / var(--tw-text-opacity));
}

.group:hover .group-hover\:text-white{
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

.group:hover .group-hover\:opacity-100{
  opacity: 1;
}

:is(.dark .dark\:block){
  display: block;
}

:is(.dark .dark\:hidden){
  display: none;
}

:is(.dark .dark\:border-dark-3){
  --tw-border-opacity: 1;
  border-color: rgb(55 65 81 / var(--tw-border-opacity));
}

:is(.dark .dark\:bg-dark){
  --tw-bg-opacity: 1;
  background-color: rgb(17 25 40 / var(--tw-bg-opacity));
}

:is(.dark .dark\:bg-dark-2){
  --tw-bg-opacity: 1;
  background-color: rgb(31 42 55 / var(--tw-bg-opacity));
}

:is(.dark .dark\:bg-dark-3){
  --tw-bg-opacity: 1;
  background-color: rgb(55 65 81 / var(--tw-bg-opacity));
}

:is(.dark .dark\:bg-dark-700){
  background-color: #090e34b3;
}

:is(.dark .dark\:bg-white){
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}

:is(.dark .dark\:via-dark-3){
  --tw-gradient-to: rgb(55 65 81 / 0)  var(--tw-gradient-to-position);
  --tw-gradient-stops: var(--tw-gradient-from), #374151 var(--tw-gradient-via-position), var(--tw-gradient-to);
}

:is(.dark .dark\:text-dark-6){
  --tw-text-opacity: 1;
  color: rgb(156 163 175 / var(--tw-text-opacity));
}

:is(.dark .dark\:text-white){
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

:is(.dark .dark\:shadow-none){
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}

:is(.dark .dark\:hover\:border-primary:hover){
  --tw-border-opacity: 1;
  border-color: rgb(55 88 249 / var(--tw-border-opacity));
}

:is(.dark .dark\:hover\:text-primary:hover){
  --tw-text-opacity: 1;
  color: rgb(55 88 249 / var(--tw-text-opacity));
}

:is(.dark .dark\:hover\:text-white:hover){
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

:is(.dark .dark\:focus\:border-primary:focus){
  --tw-border-opacity: 1;
  border-color: rgb(55 88 249 / var(--tw-border-opacity));
}

@media (min-width: 540px){
  .sm\:left-9{
    left: 2.25rem;
  }

  .sm\:-mx-4{
    margin-left: -1rem;
    margin-right: -1rem;
  }

  .sm\:mb-8{
    margin-bottom: 2rem;
  }

  .sm\:mr-6{
    margin-right: 1.5rem;
  }

  .sm\:flex{
    display: flex;
  }

  .sm\:h-\[160px\]{
    height: 160px;
  }

  .sm\:h-\[220px\]{
    height: 220px;
  }

  .sm\:h-\[400px\]{
    height: 400px;
  }

  .sm\:h-\[60px\]{
    height: 60px;
  }

  .sm\:w-1\/2{
    width: 50%;
  }

  .sm\:max-w-\[60px\]{
    max-width: 60px;
  }

  .sm\:p-10{
    padding: 2.5rem;
  }

  .sm\:p-12{
    padding: 3rem;
  }

  .sm\:p-5{
    padding: 1.25rem;
  }

  .sm\:px-10{
    padding-left: 2.5rem;
    padding-right: 2.5rem;
  }

  .sm\:px-12{
    padding-left: 3rem;
    padding-right: 3rem;
  }

  .sm\:px-4{
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .sm\:px-8{
    padding-left: 2rem;
    padding-right: 2rem;
  }

  .sm\:px-\[30px\]{
    padding-left: 30px;
    padding-right: 30px;
  }

  .sm\:py-12{
    padding-top: 3rem;
    padding-bottom: 3rem;
  }

  .sm\:text-2xl{
    font-size: 1.5rem;
    line-height: 2rem;
  }

  .sm\:text-3xl{
    font-size: 1.875rem;
    line-height: 2.25rem;
  }

  .sm\:text-4xl{
    font-size: 2.25rem;
    line-height: 2.5rem;
  }

  .sm\:text-\[28px\]{
    font-size: 28px;
  }

  .sm\:text-\[36px\]{
    font-size: 36px;
  }

  .sm\:text-\[40px\]{
    font-size: 40px;
  }

  .sm\:text-lg{
    font-size: 1.125rem;
    line-height: 1.75rem;
  }

  .sm\:leading-\[1\.2\]{
    line-height: 1.2;
  }

  .sm\:leading-\[1\.44\]{
    line-height: 1.44;
  }

  .sm\:leading-\[40px\]{
    line-height: 40px;
  }

  .sm\:leading-snug{
    line-height: 1.375;
  }
}

@media (min-width: 720px){
  .md\:mb-0{
    margin-bottom: 0px;
  }

  .md\:mr-10{
    margin-right: 2.5rem;
  }

  .md\:mr-6{
    margin-right: 1.5rem;
  }

  .md\:h-\[346px\]{
    height: 346px;
  }

  .md\:h-\[400px\]{
    height: 400px;
  }

  .md\:h-\[540px\]{
    height: 540px;
  }

  .md\:w-1\/2{
    width: 50%;
  }

  .md\:w-1\/3{
    width: 33.333333%;
  }

  .md\:w-2\/3{
    width: 66.666667%;
  }

  .md\:w-5\/12{
    width: 41.666667%;
  }

  .md\:w-7\/12{
    width: 58.333333%;
  }

  .md\:justify-start{
    justify-content: flex-start;
  }

  .md\:justify-end{
    justify-content: flex-end;
  }

  .md\:border-b{
    border-bottom-width: 1px;
  }

  .md\:p-\[60px\]{
    padding: 60px;
  }

  .md\:px-\[60px\]{
    padding-left: 60px;
    padding-right: 60px;
  }

  .md\:py-\[120px\]{
    padding-top: 120px;
    padding-bottom: 120px;
  }

  .md\:pt-\[130px\]{
    padding-top: 130px;
  }

  .md\:text-\[28px\]{
    font-size: 28px;
  }

  .md\:text-\[35px\]{
    font-size: 35px;
  }

  .md\:text-\[38px\]{
    font-size: 38px;
  }

  .md\:text-\[40px\]{
    font-size: 40px;
  }

  .md\:leading-\[1\.28\]{
    line-height: 1.28;
  }

  .md\:leading-\[1\.2\]{
    line-height: 1.2;
  }

  .md\:leading-\[1\.42\]{
    line-height: 1.42;
  }

  .md\:leading-\[1\.44\]{
    line-height: 1.44;
  }
}

@media (min-width: 960px){
  .lg\:invisible{
    visibility: hidden;
  }

  .lg\:static{
    position: static;
  }

  .lg\:absolute{
    position: absolute;
  }

  .lg\:top-\[110\%\]{
    top: 110%;
  }

  .lg\:-mx-2{
    margin-left: -0.5rem;
    margin-right: -0.5rem;
  }

  .lg\:mb-0{
    margin-bottom: 0px;
  }

  .lg\:mb-4{
    margin-bottom: 1rem;
  }

  .lg\:mb-9{
    margin-bottom: 2.25rem;
  }

  .lg\:mb-\[150px\]{
    margin-bottom: 150px;
  }

  .lg\:mb-\[70px\]{
    margin-bottom: 70px;
  }

  .lg\:ml-7{
    margin-left: 1.75rem;
  }

  .lg\:ml-8{
    margin-left: 2rem;
  }

  .lg\:mr-0{
    margin-right: 0px;
  }

  .lg\:mt-\[60px\]{
    margin-top: 60px;
  }

  .lg\:block{
    display: block;
  }

  .lg\:flex{
    display: flex;
  }

  .lg\:inline-flex{
    display: inline-flex;
  }

  .lg\:hidden{
    display: none;
  }

  .lg\:h-\[225px\]{
    height: 225px;
  }

  .lg\:h-\[400px\]{
    height: 400px;
  }

  .lg\:h-\[45\%\]{
    height: 45%;
  }

  .lg\:h-\[500px\]{
    height: 500px;
  }

  .lg\:w-1\/2{
    width: 50%;
  }

  .lg\:w-1\/3{
    width: 33.333333%;
  }

  .lg\:w-1\/4{
    width: 25%;
  }

  .lg\:w-2\/12{
    width: 16.666667%;
  }

  .lg\:w-3\/12{
    width: 25%;
  }

  .lg\:w-4\/12{
    width: 33.333333%;
  }

  .lg\:w-5\/12{
    width: 41.666667%;
  }

  .lg\:w-6\/12{
    width: 50%;
  }

  .lg\:w-7\/12{
    width: 58.333333%;
  }

  .lg\:w-8\/12{
    width: 66.666667%;
  }

  .lg\:w-full{
    width: 100%;
  }

  .lg\:max-w-full{
    max-width: 100%;
  }

  .lg\:border-0{
    border-width: 0px;
  }

  .lg\:bg-transparent{
    background-color: transparent;
  }

  .lg\:p-10{
    padding: 2.5rem;
  }

  .lg\:px-0{
    padding-left: 0px;
    padding-right: 0px;
  }

  .lg\:px-10{
    padding-left: 2.5rem;
    padding-right: 2.5rem;
  }

  .lg\:px-2{
    padding-left: 0.5rem;
    padding-right: 0.5rem;
  }

  .lg\:px-4{
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .lg\:px-6{
    padding-left: 1.5rem;
    padding-right: 1.5rem;
  }

  .lg\:px-8{
    padding-left: 2rem;
    padding-right: 2rem;
  }

  .lg\:py-0{
    padding-top: 0px;
    padding-bottom: 0px;
  }

  .lg\:py-10{
    padding-top: 2.5rem;
    padding-bottom: 2.5rem;
  }

  .lg\:py-12{
    padding-top: 3rem;
    padding-bottom: 3rem;
  }

  .lg\:py-20{
    padding-top: 5rem;
    padding-bottom: 5rem;
  }

  .lg\:py-6{
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
  }

  .lg\:py-\[110px\]{
    padding-top: 110px;
    padding-bottom: 110px;
  }

  .lg\:py-\[115px\]{
    padding-top: 115px;
    padding-bottom: 115px;
  }

  .lg\:py-\[90px\]{
    padding-top: 90px;
    padding-bottom: 90px;
  }

  .lg\:pb-20{
    padding-bottom: 5rem;
  }

  .lg\:pb-\[50px\]{
    padding-bottom: 50px;
  }

  .lg\:pb-\[70px\]{
    padding-bottom: 70px;
  }

  .lg\:pb-\[90px\]{
    padding-bottom: 90px;
  }

  .lg\:pl-0{
    padding-left: 0px;
  }

  .lg\:pr-0{
    padding-right: 0px;
  }

  .lg\:pr-4{
    padding-right: 1rem;
  }

  .lg\:pt-\[100px\]{
    padding-top: 100px;
  }

  .lg\:pt-\[120px\]{
    padding-top: 120px;
  }

  .lg\:pt-\[160px\]{
    padding-top: 160px;
  }

  .lg\:text-5xl{
    font-size: 3rem;
    line-height: 1;
  }

  .lg\:text-base{
    font-size: 1rem;
    line-height: 1.5rem;
  }

  .lg\:text-xl{
    font-size: 1.25rem;
    line-height: 1.75rem;
  }

  .lg\:leading-\[1\.2\]{
    line-height: 1.2;
  }

  .lg\:text-body-color{
    --tw-text-opacity: 1;
    color: rgb(99 115 129 / var(--tw-text-opacity));
  }

  .lg\:text-white{
    --tw-text-opacity: 1;
    color: rgb(255 255 255 / var(--tw-text-opacity));
  }

  .lg\:opacity-0{
    opacity: 0;
  }

  .lg\:shadow-lg{
    --tw-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  }

  .lg\:shadow-none{
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  }

  .group:hover .lg\:group-hover\:visible{
    visibility: visible;
  }

  .group:hover .lg\:group-hover\:top-full{
    top: 100%;
  }

  .group:hover .lg\:group-hover\:text-white{
    --tw-text-opacity: 1;
    color: rgb(255 255 255 / var(--tw-text-opacity));
  }

  .group:hover .lg\:group-hover\:opacity-70{
    opacity: 0.7;
  }

  :is(.dark .dark\:lg\:bg-transparent){
    background-color: transparent;
  }

  :is(.dark .dark\:lg\:text-dark-6){
    --tw-text-opacity: 1;
    color: rgb(156 163 175 / var(--tw-text-opacity));
  }
}

@media (min-width: 1140px){
  .xl\:-mx-4{
    margin-left: -1rem;
    margin-right: -1rem;
  }

  .xl\:mb-8{
    margin-bottom: 2rem;
  }

  .xl\:ml-10{
    margin-left: 2.5rem;
  }

  .xl\:h-1\/2{
    height: 50%;
  }

  .xl\:h-\[310px\]{
    height: 310px;
  }

  .xl\:h-\[500px\]{
    height: 500px;
  }

  .xl\:w-1\/4{
    width: 25%;
  }

  .xl\:w-2\/12{
    width: 16.666667%;
  }

  .xl\:w-3\/12{
    width: 25%;
  }

  .xl\:w-4\/12{
    width: 33.333333%;
  }

  .xl\:w-5\/12{
    width: 41.666667%;
  }

  .xl\:w-8\/12{
    width: 66.666667%;
  }

  .xl\:gap-11{
    gap: 2.75rem;
  }

  .xl\:p-14{
    padding: 3.5rem;
  }

  .xl\:px-4{
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .xl\:px-6{
    padding-left: 1.5rem;
    padding-right: 1.5rem;
  }

  .xl\:text-2xl{
    font-size: 1.5rem;
    line-height: 2rem;
  }

  .xl\:text-\[42px\]{
    font-size: 42px;
  }

  .xl\:text-lg{
    font-size: 1.125rem;
    line-height: 1.75rem;
  }

  .xl\:leading-\[1\.21\]{
    line-height: 1.21;
  }
}

@media (min-width: 1320px){
  .\32xl\:ml-20{
    margin-left: 5rem;
  }

  .\32xl\:p-\[60px\]{
    padding: 60px;
  }
}

</style>
