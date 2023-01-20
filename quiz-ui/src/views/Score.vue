<template>
  <h3>{{ playerName }}, your score is {{ lastScore }} / {{ totalNumberOfQuestion }}</h3>




</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
  name: "Score",
  data() {
    return {
      lastScore: 0,
      playerName: '',
      totalNumberOfQuestion: 1
    };
  },
  async created() {

    this.lastScore = participationStorageService.getParticipationScore();
    this.playerName = participationStorageService.getPlayerName();
    const quizInfo = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestion = quizInfo["data"]["size"];
  },
};
</script>