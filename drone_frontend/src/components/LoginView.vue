<template>
  <div class="signin text-center">
    <!-- Trigger button -->
    <!-- <q-btn
      label="Sign in"
      @click="showLogin = true"
      class="text-capitalize"
      color="orange"
    /> -->

    <!-- Persistent Modal -->
    <!-- <q-dialog v-model="showLogin" persistent>
      <q-card class="q-pa-none shadow-55 q-col-gutter-md" :style="{ width: '400px' }">
        <q-card-section class="q-mb-md">
          <q-btn
            type="reset"
            color="red-10"
            flat
            dense
            class="q-ml-sm absolute-top-right"
            icon="close"
            @click="(showLogin = false), (error = '')"
          />
        </q-card-section>
        <q-card-section class="q-mt-none text-center error" v-if="error != ''">
          <div
            class="content-center items-center text-center text-negative"
            clearable
            v-if="error"
          >
            {{ error }}
          </div>
        </q-card-section>

        <q-card-section class="q-pa-md">
          <q-form @submit.prevent="logins" method="post">
            <q-input
              outlined
              dense
              v-model="formData.username"
              label="Enter your username"
              class="q-mb-md"
              type="text"
            />
            <q-input
              outlined
              dense
              v-model="formData.password"
              label="Enter password"
              class="q-mb-md"
              type="password"
            />

            <div class="q-mt-md text-center">
              <q-btn
                label="Login"
                type="submit"
                class="text-capitalize"
                color="orange-10"
              />
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog> -->
     <q-card class="q-pa-none shadow-55 q-col-gutter-md" :style="{ width: '400px'}">
        <q-card-section class="q-mb-md" avatar>

          <!-- <q-btn
            type="reset"
            color="red-10"
            flat
            dense
            class="q-ml-sm absolute-top-right"
            icon="close"
            @click="(showLogin = false), (error = '')"
          /> -->
          <q-img rounded>
            <img  src="~assets/logo.png" >
          </q-img>
        </q-card-section>
        <q-card-section class="q-mt-none text-center error" v-if="error != ''">
          <div
            class="content-center items-center text-center text-negative"
            clearable
            v-if="error"
          >
            {{ error }}
          </div>
        </q-card-section>

        <q-card-section class="q-pa-md">
          <q-form @submit.prevent="logins" method="post">
            <q-input
              outlined
              dense
              v-model="formData.username"
              label="Enter your username"
              class="q-mb-md"
              type="text"
            />
            <q-input
              outlined
              dense
              v-model="formData.password"
              label="Enter password"
              class="q-mb-md"
              type="password"
            />

            <div class="q-mt-md text-center">
              <q-btn
                label="Login"
                type="submit"
                class="text-capitalize"
                color="orange-10"
              />
            </div>
          </q-form>
        </q-card-section>
      </q-card>
  </div>
</template>
<script>
import { useQuasar } from "quasar";
import { useAppAuthStore } from "stores/useAppAuthStore";

import { ref } from "vue";

const appAuthStore = useAppAuthStore();
// const formData = ref({
//   username: "",
//   password: "",
// });
export default {
  setup() {
    const $q = useQuasar();

    return {
      showLogin: ref(false), // Controls the modal's visibility
      formData:ref({
        username:'',
        password:''
      }),
      error: ref(""),
      appAuthStore,
    };
  },

  methods: {
    logins() {
      this.error = "";
      if (this.formData.password != '' && this.formData.username != '') {
        appAuthStore.login(this.formData).then(()=>{
          if (appAuthStore.error == '') {
            this.formData = ''          
          }else{
            this.error = JSON.stringify(appAuthStore.error);
          }
        })
      } else {
        this.error = 'All Fields Are Required';        
      }
      // if (formData.value.username != "" && formData.value.password != "") {
      //   let username = this.formData.username.valueOf();
      //   console.log(username);
      //   appAuthStore.login(this.formData).then(() => {
      //     if (!appAuthStore.error === "") {
      //       formData.value = "";
      //     } else {
      //       console.error(appAuthStore.error);
      //       console.log(appAuthStore.error);
      //       this.error = JSON.stringify(appAuthStore.error);
      //       // this.error = appAuthStore.error.toString();
      //     }
      //   });
      // } else {
      //   this.error = "All fields are Required";
      // }
      return appAuthStore, this.logins;
    },
  },
};
</script>
<style scoped>
.error {
  background: rgba(248, 168, 168, 0.849);
}
.signin{
  margin: auto;
  height: 500px;
  display: flex;
  justify-content: center;
  align-content: center;
  align-items: center;
}

</style>
src/stores/authService
