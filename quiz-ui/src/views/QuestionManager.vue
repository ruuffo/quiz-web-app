<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
import QuestionDisplay from "./QuestionDisplay.vue";
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
  name: "QuestionsManager",
  components: {
    QuestionDisplay
  },
  data() {
    return {
      currentQuestion: {},
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 1,
      listAnswers: Array()
    };
  },
  async created() {
    let quizInfoPromise = quizApiService.getQuizInfo();
    let quizInfoResult = await quizInfoPromise;
    this.totalNumberOfQuestion = quizInfoResult.data.size
    this.currentQuestion = await this.loadQuestionByposition();
  },

  methods: {
    async loadQuestionByposition() {
      let questionPromise = quizApiService.getQuestion(this.currentQuestionPosition);
      let questionApiResult = await questionPromise;
      return questionApiResult.data
    },
    async answerClickedHandler(position) {
      this.listAnswers.push(position)
      if (this.currentQuestionPosition >= this.totalNumberOfQuestion) {
        this.endQuiz()
      } else {
        this.currentQuestionPosition += 1
        this.currentQuestion = await this.loadQuestionByposition();
      }
    },

    async endQuiz() {
      let quizSubmitPromise = quizApiService.postParticipation({
        "playerName": participationStorageService.getPlayerName(),
        "answers": this.listAnswers
      });
      let quizSubmitResult = await quizSubmitPromise
      this.$router.push('/');
    },
  }
};
</script>