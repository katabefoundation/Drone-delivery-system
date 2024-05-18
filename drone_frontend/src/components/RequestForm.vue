<template>
  <div>
    <q-card>
      <q-card-section horizontal>
        <q-card-section class="q-pt-xs col-7" >
          <div class="text-h5">Make your inquries</div>
          <div class="text-h5 q-mt-sm q-mb-xs">Send the Request</div>
          <div class="text-caption text-grey">
           All the enquries will be answered soon as the they will be sent to us
          </div>
        </q-card-section>
          <q-card-section class="col-5 flex flex-center">
          <q-img
            class="rounded-borders"
            src="~assets/statics/requests.jpg" height="0" img-style="cover"
          />
          </q-card-section>
      </q-card-section>
    </q-card>
    
    <!-- Trigger button -->
    <q-btn label="Open Form" @click="showModal = true" />

    <!-- Persistent Modal -->
    <q-dialog v-model="showModal" persistent>
      <q-card>
        <q-card-section>
          <q-form>
            <q-input
              outlined
              v-model="form.firstName"
              label="First Name"
              class="q-mb-md"
            />
            <q-input outlined v-model="form.lastName" label="Last Name" class="q-mb-md" />
            <q-input outlined v-model="form.position" label="Position" class="q-mb-md" />
            <q-input outlined v-model="form.phone" label="Phone" class="q-mb-md" />
            <q-input outlined v-model="form.domicile" label="Domicile" class="q-mb-md" />
            <q-input outlined v-model="form.job" label="Job" class="q-mb-md" />

            <div class="q-mt-md">
              <q-btn label="Submit" type="submit" @click="handleSubmit" />
              <q-btn
                label="Close"
                type="reset"
                color="primary"
                flat
                class="q-ml-sm"
                @click="showModal = false"
              />
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>
<script>
export default {
  setup() {
    return {
      showModal: false, // Controls the modal's visibility
      form: {
        firstName: "",
        lastName: "",
        position: "",
        phone: "",
        domicile: "",
        job: "",
      },
    };
  },
  methods: {
    handleSubmit() {
      // Handle the form data as needed
      console.log(this.form);

      // Close the modal after handling the form
      this.showModal = false;
    },
  },
};
</script>
