<template>
  <div class="grid justify-items-center w-full">
    <form class="w-full max-w-sm">
      <div class="md:flex md:items-center mb-6">
        <div class="md:w-1/3 mx-2">
          <label class=" md:text-right" for="inline-full-name">
            Votre nom
          </label>
        </div>
        <div class="md:w-2/3 mx-2">
          <input
            class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"
            id="name" type="text" v-model="username" />
        </div>
        <div class="mx-2">
          <input type="button" @click="launchNewQuiz"
            class="hover:bg-blue-400 hover:text-gray-700 btn bg-purple-600 text-slate-50" value="Save">
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";
import "../assets/main.css"
export default {
  name: "NewQuizPage",
  data() {
    let username = participationStorageService.getPlayerName();
    return {
      username
    };
  },
  methods: {
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/questions');
    },
  }
};
</script>
