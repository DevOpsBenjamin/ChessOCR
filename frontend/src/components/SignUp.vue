<template>
  <div class="max-w-sm mx-auto mt-10">
    <form @submit.prevent="submit" class="space-y-2">
      <input v-model="username" required class="border p-2 w-full" placeholder="Username" />
      <input v-model="email" type="email" required class="border p-2 w-full" placeholder="Email" />
      <input v-model="password" type="password" required class="border p-2 w-full" placeholder="Password" />
      <button type="submit" class="bg-green-500 text-white px-4 py-2 w-full">Sign Up</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useUserStore } from '../store';

const username = ref('');
const email = ref('');
const password = ref('');
const router = useRouter();
const route = useRoute();
const store = useUserStore();
const refCode = route.query.ref || '';

async function submit() {
  const res = await fetch('/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: username.value,
      email: email.value,
      password: password.value,
      referral_code: refCode || null
    })
  });
  if (res.ok) {
    const loginRes = await fetch('/login', {
      headers: {
        'Authorization': 'Basic ' + btoa(email.value + ':' + password.value)
      }
    });
    if (loginRes.ok) {
      store.user = email.value;
      router.push('/');
    }
  } else {
    alert('Registration failed');
  }
}
</script>
