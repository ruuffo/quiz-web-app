<template>
  <div class="grid justify-items-center place-content-center">
    <h1
      class="font-question font-bold sm:text-sm md:text-md lg:text-lg xl:text-xl md:text-md"
    >
      {{ question.title }}
    </h1>
    <div class="lg:w-75 md:w-100 sm:w-100 sm:text-xl">
      <h3
        class="lg:text-3xl md:text-2xl font-question font-bold text-center xl:text-3xl"
      >
        {{ question.text }}
      </h3>
    </div>
    <div>
      <img
        v-if="question.image"
        :src="question.image"
        class="m-3 xl:max-h-xl xl:max-w-xl md:max-h-md sm:max-h-sm rounded shadow-md shadow-black lg:max-w-lg md:max-w-md sm:max-w-sm lg:max-h-72"
      />
    </div>

    <div class="grid grid-cols-2 gap-2 w-full">
      <div
        v-for="(possibleAnswer, index) in question.possibleAnswers"
        class="p-2 text-center btn bg-rose-500 opacity-90 hover:bg-rose-300 hover:transition-all"
        style="text-shadow: none"
      >
        <a
          @click="$emit('answer-selected', index)"
          class="font-bold w-full h-full sm:text-sm md:text-md lg:text-lg xl:text-xl inline-block font-question hover:no-underline hover:bg-transparent hover:text-current"
          >{{ possibleAnswer.text }}</a
        >
      </div>
    </div>
  </div>
</template>

<script>
import "../assets/main.css";
export default {
  mounted() {
    console.log("Question: ", this.question);
  },
  name: "QuestionDisplay",
  emits: ["answer-selected"],
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style>
.img-thumbnail {
  max-height: 250px;
  max-width: 500px;
}
</style>
