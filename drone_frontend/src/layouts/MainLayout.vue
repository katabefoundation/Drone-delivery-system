<template>
  <q-layout view="hHh Lpr fFf">
    <q-page-container class="content">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from "vue";

export default {
  name: "HomeLayout",

  setup() {
    return {

   }
  },
};
</script>

<style lang="scss" scoped>

</style>
