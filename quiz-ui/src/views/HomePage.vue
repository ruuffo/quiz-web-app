<template>
  <div class="justify-center flex">
    <div class="text-center">
      <h1 class=" text-2xl m-2">Scores</h1>
      <div class="flex flex-col m-3">
        <div class=" box-border card rounded-lg sm:px-6 lg:px-8 bg-slate-800 bg-opacity-90 w-4/5 justi inline-block ">
          <div class="overflow-y-auto scroll-m-1 overflow-x-hidden max-h-96">
            <table class="table-fixed p-5 min-w-full w-full text-left ">
              <thead class=" border-b dark:border-neutral-900 sticky top-0 bg-slate-800">
                <tr>
                  <th scope="col" class="px-6 pt-4 pb-2 tracking-wider">Name</th>
                  <th scope="col" class="px-6 pt-4 pb-2 tracking-wider">Score</th>
                </tr>
              </thead>

              <tbody class="divide-y dark:border-neutral-900">

                <tr v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
                  <td class="whitespace-nowrap px-6 py-2"> {{ scoreEntry.playerName }} </td>
                  <td class="whitespace-nowrap px-6 py-2"> {{ scoreEntry.score }} </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <router-link to="/start-new-quiz-page"
        class="hover:bg-blue-400 scale-150 hover:text-gray-700 btn bg-purple-800 text-slate-50 mt-4"
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
