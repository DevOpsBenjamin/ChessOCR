<template>
  <div class="p-4">
    <h2 class="text-lg mb-2">Upload Scan</h2>
    <input type="file" accept="image/*" @change="onFileChange" />
    <div v-if="preview" class="mt-4">
      <img :src="preview" alt="Scan preview" class="max-w-full" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const preview = ref(null);

function onFileChange(event) {
  const file = event.target.files[0];
  if (file) {
    preview.value = URL.createObjectURL(file);
  }
}
</script>
