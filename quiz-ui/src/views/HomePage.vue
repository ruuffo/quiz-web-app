<template>
  <div class="justify-center flex">
    <div class="text-center">
      <h1 class=" text-2xl m-9">Home page</h1>

      <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date" class=" m-3 sm:text-xl lg:text-xl md:text-xl">
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}

      </div>
      <router-link to="/start-new-quiz-page" class="hover:bg-blue-400 scale-150 hover:text-gray-700 btn bg-purple-800 text-slate-50 "
        style="text-shadow: none;">Start
        quiz !</router-link>


    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import '../assets/main.css'

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    var quizInfo = await quizApiService.getQuizInfo();
    this.registeredScores = quizInfo.data.scores
  }
};
</script>
<style>
.bg-image-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-repeat: repeat;
}
</style>
