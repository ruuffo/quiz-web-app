<script setup>
import { RouterLink, RouterView } from 'vue-router'
import './assets/main.css'
</script>

<template>
  <div style="text-shadow: 5px 5px 5px black, 0 0 0.2em black, 0 0 3em black; "
    class=" bg-gif h-screen bg-cover text-slate-200 font-body sm:text-sm md:text-md lg:text-lg xl:text-lg 2xl:text-lg flex">

    <header class="absolute top-0 inset-x-0 w-full bg-gradient-to-b from-violet-500 " ref="headerRef">

      <div class=" flex flex-shrink  ">

        <nav class=" flex items-center font-extralight p-6 lg:px-5 space-x-3" aria-label="Global">
          <div class="flex "><img src="../public/Pin_Totoro.webp" class="h-12" /></div>
          <RouterLink to="/" class="hover:bg-violet-400 hover:rounded p-2 hover:shadow-md hover:shadow-black hover:text-shadow-none">
            Home
          </RouterLink>
          <RouterLink to="/about" class="hover:bg-violet-400 hover:transition-all hover:rounded p-2 hover:text-shadow-none">
            About</RouterLink>
  <RouterLink to="/admin" class="hover:bg-violet-400 hover:transition-all hover:rounded p-2 hover:text-shadow-none">
            Admin</RouterLink>
        </nav>
      </div>
    </header>
    <div :style="{ marginTop: headerHeight + 'px' }" class="flex w-50 container justify-center">
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
