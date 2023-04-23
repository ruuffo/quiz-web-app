<template>
  <div class="flex flex-row mt-2 w-full">
    <div class="basis-1/5"></div>
    <div class="basis-3/5">
      <RouterView />
    </div>
    <div class="basis-1/5 flex justify-end">
      <div class="grid grid-col-1 gap-2 w-min h-min">
        <button class="btn bg-slate-500 whitespace-nowrap" @click="signOut">
          Sign Out
        </button>
        <button
          class="btn bg-slate-500 whitespace-nowrap"
          v-if="shouldDisplayReturnButton"
          @click="goBack"
        >
          Cancel
        </button>
        <button
          class="btn bg-slate-500 whitespace-nowrap"
          v-if="shouldDisplayEditButton"
          @click="editQuestion"
        >
          Edit
        </button>
        <button
          v-if="shouldDisplayRemoveButton"
          @click="displayDialogBoxConfirmRemoveQuestion"
          class="bg-amber-800 p-1 rounded"
        >
          Remove
        </button>
      </div>
    </div>
  </div>
  <Dialog
    :show="this.dialogBoxConfirmRemoveQuestionIsVisible"
    :cancel="undisplayDialogBoxConfirmRemoveQuestion"
    :confirm="deleteQuestion"
    title="Warning !"
    description="Do you really want to delete this question?"
    confirmtext="Yes, delete it"
  />
</template>
<script>
import { RouterView } from "vue-router";
import "../assets/main.css";
import Dialog from "../components/Dialog.vue";
import QuizApiService from "../services/QuizApiService";
import ServiceAdminController from "../services/ServiceAdminController";
export default {
  data() {
    return {
      dialogBoxConfirmRemoveQuestionIsVisible: false,
    };
  },
  computed: {
    shouldDisplayReturnButton() {
      return (
        this.$route.name === "consultQuestion" ||
        this.$route.name === "editQuestion"
      );
    },
    shouldDisplayEditButton() {
      return this.$route.name === "consultQuestion";
    },
    shouldDisplayRemoveButton() {
      return this.$route.name === "consultQuestion";
    },
  },
  components: {
    Dialog,
  },
  methods: {
    signOut() {
      ServiceAdminController.signOut();
    },
    goBack() {
      this.$router.go(-1); 
    },
    editQuestion() {
      this.$router.push("editQuestion");
    },
    undisplayDialogBoxConfirmRemoveQuestion() {
      this.dialogBoxConfirmRemoveQuestionIsVisible = false;
    },
    displayDialogBoxConfirmRemoveQuestion() {
      this.dialogBoxConfirmRemoveQuestionIsVisible = true;
    },
    deleteQuestion() {
      console.log("removed");
      var id = ServiceAdminController.getCurrentQuestionId();

      QuizApiService.deleteQuestion(id);

      this.undisplayDialogBoxConfirmRemoveQuestion();
      this.goBack();
      this.$forceUpdate();
    },
  },
};
</script>
