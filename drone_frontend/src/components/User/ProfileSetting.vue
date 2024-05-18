<template>

  <div class="">
    <div class="flex items-center justify-center">
       <q-card class="card ripple">
      <q-card-section class="text-center">
        <q-img src="~assets/profile.png"/>
      </q-card-section>
      <q-card-section >
        <h2 class="text-body1">Name: John Doe</h2>
        <h2 class="text-body1">Email: example@yahoo.com</h2>
        <h2 class="text-body1">Phone: +255673980239</h2>
        <h2 class="text-body1">category: Medical Assistant</h2>
        <h2 class="text-body1">Location: Dodoma</h2>
      </q-card-section>
      <q-card-section class="q-ma-lg row justify-center items-center">
        <q-btn label="Update" :style="{}"  @click="showEdit = true"/>
      </q-card-section>
    </q-card>
    </div>

      <!-- Persistent Modal -->
      <q-dialog v-model="showEdit" persistent>
      <q-card :style="{width:'400px'}">

        <q-card-section>
          <q-form>
           
            <q-input outlined v-model="form.pass" label="Old Password" class="q-mb-md" type="password" dense />
            <q-input outlined v-model="form.pass" label="New Password" class="q-mb-md" type="password" dense/>
            <q-input outlined v-model="form.pass" label="Confirm Password" class="q-mb-md" type="password" dense/>
            <div class="q-mt-md justify-between" dense>
              <q-btn label="Submit" type="submit" @click="handleSubmit" />
              <q-btn label="Close" type="reset" color="primary" flat class="q-ml-sm float-right" @click="showEdit = false" />
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  // name: 'ComponentName',
  setup () {
    return {
      showEdit: ref(false),
      form: {
        firstName: '',
        lastName: '',
        position: '',
        phone: '',
        domicile: '',
        image: ''
      }
    };

  },
  methods: {
    handleSubmit() {
      console.log(this.form);
      this.showEdit = false
    }
  }
}
</script>
<style>
.card{
  width: 300px;
}
.q-img{
  width: 100px;
}
</style>
