
<template>
  <div class="flex flex-row mt-2 w-full">
    <div class=" basis-1/5"></div>
    <div class="basis-3/5">
      <RouterView />
    </div>
    <div class="basis-1/5 flex justify-end">

      <div class="grid grid-col-1 gap-2 w-min h-min ">
        <button class="btn bg-slate-500 whitespace-nowrap" @click="signOut">Sign Out</button>
        <button class="btn bg-slate-500 whitespace-nowrap" v-if="shouldDisplayReturnButton"
          @click="goBack">Retour</button>
        <button class="btn bg-slate-500 whitespace-nowrap" v-if="shouldDisplayEditButton"
          @click="editQuestion">Edit</button>

      </div>
    </div>
  </div>
</template>
<script>
import { RouterView } from "vue-router";
import "../assets/main.css";
import ServiceAdminController from "../services/ServiceAdminController";
export default {
  computed: {
    shouldDisplayReturnButton() {
      return this.$route.name === "consultQuestion" || this.$route.name === "editQuestion";

    }
    , shouldDisplayEditButton() {
      return this.$route.name === "consultQuestion";

    }
  },
  methods: {
    signOut() {
      ServiceAdminController.signOut()
    },
    goBack() {
      this.$router.go(-1); // Go back one step in the router history
    }
    , editQuestion() {
      this.$router.push("editQuestion")
    }

  }
}
</script>
