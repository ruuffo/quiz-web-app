<template>
  <div class="grid justify-items-center place-content-center">

    <h1 class=" font-question font-bold text-xl">{{ question.title }}</h1>
    <div class="w-75">
      <h3 class=" text-3xl font-question font-bold text-center">{{ question.text }}</h3>
    </div>
    <div>

      <img v-if="question.image" :src="question.image" class=" m-3 max-h-md rounded shadow-md shadow-black max-w-md lg:max-h-72" />
    </div>

    <div class="grid grid-cols-2 gap-2 w-full">
      <div v-for="(possibleAnswer, index) in question.possibleAnswers"
        class="p-2 text-center btn bg-rose-500 opacity-90 hover:bg-rose-300 hover:transition-all"
        style="text-shadow: none;">

        <a @click="$emit('answer-selected', index)"
          class=" font-bold text-lg w-full h-full inline-block font-question hover:no-underline hover:bg-transparent hover:text-current">{{
            possibleAnswer.text }}</a>

      </div>
    </div>
  </div>
</template>

<script>
import "../assets/main.css"
export default {
  name: "QuestionDisplay",
  emits: ["answer-selected"],
  props: {
    question: {
      type: Object
    }
  }
};
</script>


<style>
.img-thumbnail {
  max-height: 250px;
  max-width: 500px;
}
</style>
