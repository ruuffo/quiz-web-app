<template>
  <h1>New Quiz Page</h1>
  <div>
    <label for="name" class="form-label">Saisissez votre nom :</label>
    <input type="text" v-model="username" id="name" class="form-control" placeholder="Username" aria-label="Username">
    <input type="button" @click="launchNewQuiz" class="btn btn-success" value="Save">
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

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