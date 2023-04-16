<script setup>
import '../assets/main.css';
import QuizApiService from '../services/QuizApiService';
import '../services/ServiceAdminController';
import ServiceAdminController from '../services/ServiceAdminController';
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
        <tr v-for="question in listQuestion">
          <td class=" font-bold font-question"> {{ question.position }}</td>
          <td> {{ question.title }}</td>
          <td> <a :onClick="consultQuestion(question.position)"
              class="transititext-primary text-primary transition duration-150 ease-in-out hover:text-primary-600 focus:text-primary-600 cursor-pointer active:text-primary-700 dark:text-primary-400 dark:hover:text-primary-500 dark:focus:text-primary-500 dark:active:text-primary-600"
              data-te-toggle="tooltip" title="Consult"><svg class=" max-h-7" id="Layer_1"
                style="enable-background:new 0 0 512 512;" version="1.1" viewBox="0 0 512 512" xml:space="preserve"
                xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g>
                  <path
                    d="M447.1,256.2C401.8,204,339.2,144,256,144c-33.6,0-64.4,9.5-96.9,29.8C131.7,191,103.6,215.2,65,255l-1,1l6.7,6.9   C125.8,319.3,173.4,368,256,368c36.5,0,71.9-11.9,108.2-36.4c30.9-20.9,57.2-47.4,78.3-68.8l5.5-5.5L447.1,256.2z M256,336   c-44.1,0-80-35.9-80-80c0-44.1,35.9-80,80-80c44.1,0,80,35.9,80,80C336,300.1,300.1,336,256,336z" />
                  <path
                    d="M250.4,226.8c0-6.9,2-13.4,5.5-18.8c-26.5,0-47.9,21.6-47.9,48.2c0,26.6,21.5,48.1,47.9,48.1s48-21.5,48-48.1v0   c-5.4,3.5-11.9,5.5-18.8,5.5C266,261.6,250.4,246,250.4,226.8z" />
                  <title v-if="showConsultTip">{{ consultText }}</title>
                </g>
              </svg>
            </a>
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
      QuizApiService.getQuestion(position).then(response => {
        this.$router.push()
      });
    }
  }
}
</script>
