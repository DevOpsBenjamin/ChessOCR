<template>
  <div class="max-w-sm mx-auto mt-10 space-y-2">
    <form @submit.prevent="submit" class="space-y-2">
      <input v-model="email" type="email" required class="border p-2 w-full" placeholder="Email" />
      <input v-model="password" type="password" required class="border p-2 w-full" placeholder="Password" />
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 w-full">Sign In</button>
    </form>
    <button @click="google" class="bg-red-500 text-white px-4 py-2 w-full">Sign in with Google</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '../store';

const email = ref('');
const password = ref('');
const router = useRouter();
const store = useUserStore();

async function submit() {
  const res = await fetch('/login', {
    headers: {
      'Authorization': 'Basic ' + btoa(email.value + ':' + password.value)
    }
  });
  if (res.ok) {
    store.user = email.value;
    router.push('/');
  } else {
    alert('Login failed');
  }
}

function google() {
  window.location.href = '/auth/google';
}
</script>
