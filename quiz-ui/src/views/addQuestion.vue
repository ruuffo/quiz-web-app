<template>
  <form @submit.prevent="addQuestion">
    <label for="questiontitle">Title</label>
    <input
      name="questiontitle"
      type="text"
      class="text-md text-black p-1 rounded shadow bg-slate-200 w-100 whitespace-normal"
      v-model="question.title"
      required
    />

    <label for="questiontext">Text</label>
    <input
      name="questiontext"
      type="text"
      class="text-md text-black p-1 rounded shadow bg-slate-200 w-100 whitespace-normal"
      v-model="question.text"
      required
    />

    <div>
      <img
        v-if="question.image"
        :src="question.image"
        class="m-3 xl:max-h-xl xl:max-w-xl md:max-h-md sm:max-h-sm rounded shadow-md shadow-black lg:max-w-lg md:max-w-md sm:max-w-sm lg:max-h-72"
      />
      <ImageUpload @file-change="imageFileChangedHandler" />
    </div>
    <h1 class="text-left text-lg justify-self-start">Possible Answers:</h1>
    <div class="grid grid-cols-2 gap-2 w-full">
      <div
        v-for="(possibleAnswer, index) in this.possibleAnswers"
        class="p-2 text-center btn bg-rose-500 opacity-90 hover:bg-rose-300 hover:transition-all flex flex-row gap-1"
        style="text-shadow: none"
      >
        <input
          type="radio"
          class="relative float-left rounded h-5 w-5"
          :checked="possibleAnswer.isCorrect"
          v-model="possibleAnswer.isCorrect"
          name="answers"
          required
        />
        <input
          type="text"
          class="text-md text-black p-1 rounded shadow bg-slate-200 w-100 whitespace-normal"
          v-model="possibleAnswer.text"
          required
        />
      </div>
    </div>
    <label for="position">position</label>
    <select
      name="position"
      class="text-black"
      v-model="question.position"
      required
    >
      <option v-for="i in this.nbQuestions + 1" :value="i">{{ i }}</option>
    </select>
    <input type="submit" class="btn text-white bg-blue-500" value="Save" />
  </form>
</template>

<script>
import ImageUpload from "../components/ImageUpload.vue";
import QuizApiService from "../services/QuizApiService";
import ServiceAdminController from "../services/ServiceAdminController";
export default {
  data() {
    return { question: {}, nbQuestions: 0, possibleAnswers: [{}, {}, {}, {}] };
  },
  components: { ImageUpload },
  async created() {
    this.nbQuestions = Number(ServiceAdminController.getNbQuestions());
  },
  methods: {
    addQuestion() {
      this.possibleAnswers.forEach((answer) => {
        if (answer.isCorrect === "on") {
          answer.isCorrect = true;
        } else {
          answer.isCorrect = false;
        }
      });
      this.question.possibleAnswers = this.possibleAnswers;
      this.question.image = "falseString";
      console.log(this.question);
      QuizApiService.addQuestion(JSON.stringify(this.question)).then(() => {
        this.$router.go(-1);
      });
    },
  },
};
</script>
