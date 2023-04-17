<script setup>
import { RouterLink } from 'vue-router';

</script>


<template>
  <header class="absolute top-0 inset-x-0 w-full bg-gradient-to-b from-violet-500 " ref="headerRef">

    <nav class=" flex items-center font-extralight p-6 lg:px-5 space-x-3" aria-label="Global">
      <div class="flex "><img src="../../public/Pin_Totoro.webp" class="h-12" /></div>
      <RouterLink to="/"
        class="hover:bg-violet-400 hover:rounded p-2 hover:shadow-md hover:shadow-black hover:text-shadow-none">
        Home
      </RouterLink>
      <RouterLink to="/about" class="hover:bg-violet-400 hover:transition-all hover:rounded p-2 hover:text-shadow-none">
        About</RouterLink>
      <RouterLink to="/admin" class="hover:bg-violet-400 hover:transition-all hover:rounded p-2 hover:text-shadow-none">
        Log in</RouterLink>
    </nav>

  </header>
</template>
