<template>
  <div class="max-w-sm mx-auto mt-10">
    <form @submit.prevent="submit" class="space-y-2">
      <input v-model="username" class="border p-2 w-full" placeholder="Username" />
      <input v-model="password" type="password" class="border p-2 w-full" placeholder="Password" />
      <button type="submit" class="bg-blue-500 text-white px-4 py-2">Sign In</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { store } from '../store';

const username = ref('');
const password = ref('');
const router = useRouter();

async function submit() {
  const res = await fetch('/login', {
    headers: {
      'Authorization': 'Basic ' + btoa(username.value + ':' + password.value)
    }
  });
  if (res.ok) {
    store.user = username.value;
    router.push('/');
  } else {
    alert('Login failed');
  }
}
</script>
