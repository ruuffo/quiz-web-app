<script>
import "../assets/dialog.css";
export default {
  props: ["show", "description", "title", "confirmtext", "cancel", "confirm"],
};
</script>
,

<template>
  <div v-show="show" class="overlay">
    <div class="dialog" style="text-shadow: none">
      <div class="dialog__content">
        <h2 class="dialog__title" v-text="title"></h2>
        <p class="dialog__description" v-text="description"></p>
      </div>

      <hr />

      <div class="dialog__footer">
        <button @click="cancel" class="dialog__cancel">Cancel</button>
        <button
          @click="confirm"
          class="dialog__confirm"
          v-text="confirmtext"
        ></button>
      </div>
    </div>
  </div>
</template>
