<template>
  <div class="p-4">
    <h2 class="text-lg mb-2">Review Moves</h2>
    <ul>
      <li v-for="(move, index) in moves" :key="index" class="mb-1">
        {{ index + 1 }}. {{ move }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const moves = ref(['e4', 'e5', 'Nf3', 'Nc6']);
</script>
