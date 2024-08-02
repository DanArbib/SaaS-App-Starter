<template>
  <div id="app" class="h-full">
    <Board />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Board from '@/components/Board.vue';

export default defineComponent({
  name: 'App',
  components: { Board },
});
</script>

<style>
/* Global styles */
html, body, #app {
  height: 100%;
  margin: 0;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.smooth-dnd-container.horizontal {
  display: flex !important;
}
</style>
