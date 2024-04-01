<script setup>
import { ref } from "vue";
let showForm = ref(false);

const toggleAdminForm = () => {
  showForm.value = !showForm.value;
};
</script>

<template>
  <nav>
    <h1>&nbsp;class<span class="text-decoration">Ring</span>&nbsp;&nbsp;</h1>
    <i @click="toggleAdminForm" class="fa-solid fa-spinner"></i>
  </nav>
  <form v-if="showForm" action="#">
    <label for="loginForm">Admin</label>
    <input type="email" placeholder="Email..." name="email" />

    <input
      type="password"
      placeholder="Password..."
      name="password"
      v-model="password"
    />
    <input type="submit" value="Login" />
  </form>
</template>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 5%;

  background-color: var(--primary1);
  box-shadow: 0 8px 18px -4px rgba(0, 0, 0, 0.6);
  border-bottom: 2px solid var(--primary2);
}

h1 {
  text-decoration: underline;
}
i {
  font-size: 2rem;
  animation: rotate 4s infinite;
  transition: all 600ms linear;
  cursor: pointer;
}

@keyframes rotate {
  0% {
    transform: rotate(0);
    color: var(--textSecondary);
  }
  50% {
    color: var(--primary2);
  }
  100% {
    transform: rotate(-360deg);
    color: var(--secondary1);
  }
}

form {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5px;
  padding: 15px 0;

  background-color: var(--primary2);
}

form input:not([type="submit"]) {
  width: 25%;
  max-width: 150px;
}

input[type="submit"] {
  background-color: var(--primary1);
  color: var(--textSecondary);
  border: none;
  border-radius: 25px;
  padding: 5px 10px;

  font-weight: 600;
  font-family: inherit;
}
</style>
