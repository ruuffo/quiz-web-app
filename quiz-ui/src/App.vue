<script setup>
import { RouterLink, RouterView } from 'vue-router'
import './assets/main.css'
</script>

<template>
  <div class=" bg-gif h-screen bg-cover flex justify-center items-center ">

    <header class="absolute inset-x-0 top-0 " ref="headerRef">

      <div class=" flex flex-shrink ">

        <nav class=" flex items-center justify-between p-6 lg:px-8 space-x-4" aria-label="Global">
          <RouterLink to="/"
            class=" text-slate-200  text-shadow shadow-indigo-500/50 hover:bg-violet-400 hover:transition-all hover:rounded p-2 " style="text-shadow: 5px 5px 5px black, 0 0 0.2em black, 0 0 3em black;">
            Home
          </RouterLink>
          <RouterLink to="/about"
            class=" text-slate-200 text-shadow shadow-indigo-500/50 hover:bg-violet-400 hover:transition-all hover:rounded p-2 "  style="text-shadow: 5px 5px 5px black, 0 0 0.2em black, 0 0 3em black;">
            About</RouterLink>
        </nav>
      </div>
    </header>
    <div :style="{ marginTop: headerHeight + 'px' }" class="flex justify-center items-center w-50">
      <RouterView />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      headerHeight: 0,
    };
  },
  mounted() {
    this.headerHeight = this.$refs.headerRef.offsetHeight;
  },
};

</script>
<!-- <style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.bg-image-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-repeat: repeat;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style> -->
