<template>
  <header class="flex justify-between items-center p-4 bg-gray-800 text-white">
    <h1 class="text-xl">ChessOCR</h1>
    <nav class="flex gap-4">
      <router-link to="/upload" class="text-blue-300">Upload</router-link>
      <router-link to="/review" class="text-blue-300">Review</router-link>
    </nav>
    <div v-if="store.user" class="relative">
      <button @click="toggle" class="px-2">{{ store.user }}</button>
      <div v-if="open" class="absolute right-0 mt-2 bg-white text-black rounded shadow">
        <button class="block px-4 py-2" @click="logout">Sign out</button>
      </div>
    </div>
    <router-link v-else to="/signin" class="text-blue-300">Sign In</router-link>
  </header>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '../store';

const router = useRouter();
const store = useUserStore();
const open = ref(false);
function toggle() {
  open.value = !open.value;
}
function logout() {
  store.user = null;
  open.value = false;
  router.push('/');
}
</script>
