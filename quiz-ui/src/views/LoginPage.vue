<script setup>
import '../assets/main.css';
import QuizApiService from '../services/QuizApiService';
import ServiceAdminController from '../services/ServiceAdminController';
</script>

<template>
  <div class="grid justify-items-center w-full">
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
            <input type="password"
              class=" border rounded lg:text-lg sm:text-lg md:text-lg leading-tight text-slate-900 appearance-none "
              placeholder="Password" v-model="password" />
          </td>
        </tr>
        <tr v-if="errorMessage">
          <td>
            <div class="bg-red-950 text-white card text-sm p-1 text-left"><span>&#x2715; &nbsp;{{ errorMessage }}</span>
            </div>
          </td>
        </tr>
        <tr>
          <td class="py-2">
            <input type="submit"
              class=" hover:bg-blue-400 scale-150 bg-purple-800 hover:text-gray-700 btn text-slate-50 mt-4"
              value="Login" />
          </td>
        </tr>
      </table>
    </form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage: ""
    }
  },
  methods: {
    handleSubmit() {
      ;
      QuizApiService.login(this.username, this.password).then(response => {
        const token = response.data.token
        ServiceAdminController.saveToken(token)
        this.$router.push('/admin')
      }).catch(error => {
        console.log(error)
        this.errorMessage = "Mot de passe invalide"
      })
    }
  }
}
</script>
