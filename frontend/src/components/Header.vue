<template>
  <header class="flex justify-between items-center p-4 bg-gray-800 text-white">
    <h1 class="text-xl">ChessOCR</h1>
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
import { store } from '../store';

const router = useRouter();
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
