<template>
  <q-page padding>
   <div class="text-center text-h3">Drone Request Form</div>

   <q-form @submit="RequestSubmit">
    <q-input v-model="medication" label="Medication" type="text" required></q-input>
    <q-btn label="Send" class="bg-primary" @click="RequestSubmit"></q-btn>
  </q-form>
  <div v-if="erroMessage">
    <p class="error">{{ errorMessage }}</p>
  </div>
  </q-page>
</template>

<script>
import { ref } from 'vue';

export default {
  // name: 'PageName',
  setup() {
    return {
      medication: ref(''),
      erroMessage:ref('')
    }
  },
  methods: {
    async RequestSubmit() {
      console.log("hello");
      if (!this.medication) {
        this.erroMessage = 'Please specify the medication content';
        return;
      }
      try {
        const location = await navigator.geolocation.getCurrentPosition();
        const latitude = location.coords.latitude;
        const longitude = location.coords.longitude;

        const data = {
          medication: this.medication,
          latitude,
          longitude
        }
        console.log(data);
      } catch (error) {
        console.error('Error during request', error);
        this.erroMessage = 'An error occured, Please try again'
      }
    }
  }
}
</script>
