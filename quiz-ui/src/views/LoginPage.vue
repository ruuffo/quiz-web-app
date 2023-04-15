<script setup>
import { RouterLink, RouterView } from 'vue-router'
import ApiService from '@/services/QuizApiService'
import ParticipationStorageService from '../services/ParticipationStorageService';
import '../assets/main.css'
import QuizApiService from '../services/QuizApiService';
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <table class="table-auto text-center">
      <tr>
        <td class="py-2 ">
          <input type="text" placeholder="Username"
            class=" border rounded lg:text-lg sm:text-lg md:text-lg leading-tight appearance-none text-slate-900"
            v-model="username" />
        </td>
      </tr>
      <tr>
        <td class="py-2">
          <input type="password" class=" border rounded lg:text-lg sm:text-lg md:text-lg leading-tight appearance-none "
            placeholder="Password" v-model="password" />
        </td>
      </tr>
      <tr>
        <td class="py-2">
          <input type="submit"
            class=" hover:bg-blue-400 scale-150 bg-purple-800 hover:text-gray-700 btn text-slate-50 mt-4" value="Login" />
        </td>
      </tr>
    </table>
  </form>
</template>
<script>
export default {
  data() {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
    handleSubmit() {
      ;
      QuizApiService.login(this.username, this.password).then(response => {
        const token = response.data.token
        ParticipationStorageService.saveToken(token)
        this.$router.push('/admin')
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
