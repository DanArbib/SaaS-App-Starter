<script setup lang="ts">
import { ref, onMounted} from 'vue';
import { useRouter } from 'vue-router';

const props = defineProps(['token'])

const token = ref(props.token)
const router = useRouter();

onMounted(() => {
      if (token.value) {
        localStorage.setItem('accessToken', token.value);
        router.push({ name: 'app' });
      }
    });

</script>

<template>
 
</template>