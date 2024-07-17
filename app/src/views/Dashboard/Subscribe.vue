<template>
  <div class="goal-page">
    <form @submit.prevent="addGoal">
      <input v-model="newGoalText" type="text" placeholder="Enter your goal" required />
      <input v-model.number="newGoalDuration" type="number" placeholder="Duration (seconds)" required />
      <button type="submit">Add Goal</button>
    </form>
    <div class="goal-container">
      <GoalComponent v-for="(goal, index) in goals" :key="index" :goal="goal" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import GoalComponent from './GoalComponent.vue';

export default defineComponent({
  name: 'GoalPage',
  components: {
    GoalComponent,
  },
  setup() {
    const newGoalText = ref('');
    const newGoalDuration = ref(60);
    const goals = ref<{ text: string; duration: number }[]>([]);

    const addGoal = () => {
      goals.value.push({
        text: newGoalText.value,
        duration: newGoalDuration.value,
      });
      newGoalText.value = '';
      newGoalDuration.value = 60;
    };

    return { newGoalText, newGoalDuration, goals, addGoal };
  },
});
</script>

<style scoped>
.goal-page {
  padding: 20px;
}
.goal-container {
  position: relative;
  height: 100vh;
  overflow: hidden;
}
form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}
input, button {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
