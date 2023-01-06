<template>
  <h1>New Quiz Page</h1>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    registeredScores = quizApiService.getQuizInfo().answers;
    console.log("Composant Home page 'created'");
  }
};
</script>