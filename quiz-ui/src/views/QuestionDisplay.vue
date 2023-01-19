<template>
  <div class="questionDisplay">
    <div>
      <div>
        <img v-if="question.image" :src="question.image" />
      </div>
      <div>
        <h1>{{ question.title }}</h1>
        <h3>{{ question.text }}</h3>
      </div>
      <div v-for="(possibleAnswer, index) in question.possibleAnswers">
        <a @click="$emit('answer-selected', index)">{{ possibleAnswer.text }}</a>
      </div>
    </div>
  </div>
</template>
<script>

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
@media (min-width: 1024px) {
  .questionDisplay {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>