
import AdminPage from './AdminPage.vue';

<template>
  <div class="flex flex-row mt-2 w-full">
    <div class=" basis-1/5"></div>
    <div class="basis-3/5">
      <AdminPage />
    </div>
    <div class="grid basis-1/5">
      <div class="justify-self-end">
        <button class="btn bg-slate-500" @click="signOut">Sign Out</button>
      </div>
    </div>
  </div>
</template>
<script>
import "../assets/main.css";
import ServiceAdminController from "../services/ServiceAdminController";
import AdminPage from './AdminPage.vue';
export default {
  components: {
    AdminPage
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
