<script setup>
import '../assets/main.css';
import QuizApiService from '../services/QuizApiService';
import '../services/ServiceAdminController';
import ServiceAdminController from '../services/ServiceAdminController';
import QuestionDisplay from './QuestionDisplay.vue';
</script>

<template>
  <h1 class=" text-xl my-3">Liste des questions</h1>
  <div class=" bg-slate-800 bg-opacity-40 p-2 card shadow rounded-lg">
    <table class="table-auto table text-white w-full text-sm">
      <thead class=" border-b dark:border-neutral-600 sticky top-0 ">
        <tr>
          <th scope="col" class=" text-lg">Position</th>
          <th scope="col" class=" text-lg">Titre</th>
          <th scope="col" class=" text-lg">Actions disponibles</th>
        </tr>
      </thead>
      <tbody class="divide-y">
        <tr v-for="q in  listQuestion ">
          <td class=" font-bold font-question"> {{ q.position }}</td>
          <td> {{ q.title }}</td>
          <td>
            <button @click.prevent="consultQuestion(q.position)">Details</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      listQuestion: [],
      question: {}
    };
  },
  async created() {
    QuizApiService.getAllQuestion().then(response => {
      console.log(response)
      this.listQuestion = response.data.listAllQuestions
    });
  },
  methods: {
    signOut() {
      ServiceAdminController.signOut()
    },
    consultQuestion(position) {
      console.log("position consult question ? ", position)
      ServiceAdminController.setCurrentQuestionPosition(position)
      this.$router.push("/consultQuestion")
    }
  },
  components: {
    QuestionDisplay
  }
}
</script>
