<template>
  <div class=" justify-items-center grid  w-full">
    <h2 class="">Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h2>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
import QuestionDisplay from "./QuestionDisplay.vue";

export default {
  name: "QuestionsManager",

  data() {
    return {
      currentQuestion: {},
      currentQuestionPosition: 1,
      totalNumberOfQuestion: null,
      listAnswers: Array()
    };
  },
  async created() {
    console.log("Start created")
    let quizInfoPromise = quizApiService.getQuizInfo();
    let quizInfoResult = await quizInfoPromise;
    this.totalNumberOfQuestion = quizInfoResult.data.size;
    this.currentQuestion = await this.loadQuestionByposition();
    console.log(this.currentQuestion)
  },
  methods: {
    async loadQuestionByposition() {
      let questionPromise = quizApiService.getQuestion(this.currentQuestionPosition);
      let questionApiResult = await questionPromise;
      return questionApiResult.data
    },
    async answerClickedHandler(position) {
      this.listAnswers.push(position + 1)
      if (this.currentQuestionPosition >= this.totalNumberOfQuestion) {
        this.endQuiz()
      } else {
        this.currentQuestionPosition += 1
        this.currentQuestion = await this.loadQuestionByposition();
      }
    },
    async endQuiz() {
      console.log('playername : ' + participationStorageService.getPlayerName())
      console.log('listeanswer : ' + this.listAnswers)
      let playerName = await participationStorageService.getPlayerName()
      let quizSubmitPromise = quizApiService.postParticipation(
        playerName,
        this.listAnswers);
      let playerScore = await quizSubmitPromise

      let quizLocalPromise = participationStorageService.saveParticipationScore(playerScore)
      let quizLocalResult = await quizLocalPromise

      this.$router.push('/score');
    },
  },
  components: {
    QuestionDisplay
  }
};
</script>
