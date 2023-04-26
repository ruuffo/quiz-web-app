<script setup>
import "../assets/main.css";
import Dialog from "../components/Dialog.vue";
import QuizApiService from "../services/QuizApiService";
import "../services/ServiceAdminController";
import ServiceAdminController from "../services/ServiceAdminController";
</script>
<template>
  <h1 class="text-xl my-3">Liste des questions</h1>
  <div class="bg-slate-950 bg-opacity-40 p-2 card shadow rounded-lg">
    <div class="overflow-y-auto scroll-m-1 overflow-x-hidden max-h-96">
      <table class="table text-white w-full text-sm divide-slate-800">
        <thead class="sticky top-0">
          <tr
            class="border-b-2 border-slate-800 sticky top-0 z-10"
          >
            <th scope="col" class="text-lg">Position</th>
            <th scope="col" class="text-lg">Titre</th>
          </tr>
        </thead>
        <tbody class="overflow-y-auto scroll-m-1 overflow-x-hidden max-h-96">
          <tr>
            <td colspan="3">
              <div class="flex flex-row gap-2">
                <button @click="goToAddQuestion" class="bg-blue-500 btn">
                  Add question
                </button>
                <button
                  @click="displayDialogBoxConfirmRemoveAllQuestions"
                  class="bg-blue-500 btn"
                >
                  Remove all questions
                </button>
              </div>
            </td>
          </tr>
          <tr
            v-for="q in listQuestion"
            :key="q.id"
            v-if="listQuestion.length != 0"
          >
            <td class="font-bold font-question">{{ q.position }}</td>
            <td>{{ q.title }}</td>
            <td>
              <div class="flex flex-row gap-2">
                <button
                  @click.prevent="consultQuestion(q.position, q.id)"
                  class="bg-amber-800 p-1 rounded"
                >
                  Details
                </button>
              </div>
            </td>
          </tr>
          <tr v-else>
            <td colspan="3">
              <p class="text-center text-xl">
                There is no questions in the quiz yet.
              </p>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <Dialog
    :show="this.dialogBoxConfirmRemoveAllQuestionsIsVisible"
    :cancel="undisplayDialogBoxConfirmRemoveAllQuestions"
    title="Warning!"
    description="Do you really want to delete all questions?"
    confirmtext="Yes, remove all questions"
    :confirm="removeAllQuestions"
  />
</template>
<script>
export default {
  data() {
    return {
      listQuestion: [],
      dialogBoxConfirmRemoveAllQuestionsIsVisible: false,
    };
  },
  components: { Dialog },
  async created() {
    this.loadQuestionList();
  },
  async mounted() {
    this.loadQuestionList();
  },
  methods: {
    consultQuestion(position, id) {
      ServiceAdminController.setCurrentQuestionPosition(position);
      ServiceAdminController.setCurrentQuestionId(id);
      ServiceAdminController.saveNbQuestions(this.listQuestion.length);
      this.$router.push("/consultQuestion");
    },

    undisplayDialogBoxConfirmRemoveAllQuestions() {
      this.dialogBoxConfirmRemoveAllQuestionsIsVisible = false;
    },
    displayDialogBoxConfirmRemoveAllQuestions() {
      this.dialogBoxConfirmRemoveAllQuestionsIsVisible = true;
    },
    loadQuestionList() {
      QuizApiService.getAllQuestion().then((response) => {
        this.listQuestion = response.data.listAllQuestions.sort((a, b) =>
          a.position > b.position ? 1 : -1
        );
      });
    },
    removeAllQuestions() {
      QuizApiService.deleteAllQuestions();
      this.undisplayDialogBoxConfirmRemoveAllQuestions();
      this.loadQuestionList();
    },
    goToAddQuestion() {
      this.$router.push("/addQuestion");
    },
  },
};
</script>
