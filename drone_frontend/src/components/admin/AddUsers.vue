<template>
  <div class="card q-pa-none shadow-20 q-col-gutter-md">
    <div class="col-md-8 absolute-top-right q-mr-md">
      <q-btn
        color="white"
        class="col-sm-6 text-orange on-right text-capitalize"
        icon="add_circle"
        label="Add user"
        @click="userAdd = true"
      />
    </div>

    <div>
      <q-dialog v-model="userAdd" transition-show="rotate" transition-hide="rotate">
        <q-card class="q-pa-none shadow-55 q-col-gutter-md" :style="{ width: '400px' }">
          <q-card-section class="text-center">
            <div class="text-h5">Add User</div>
          </q-card-section>
          <q-form @submit.prevent="signup">
            <q-card-section class="items-center q-mt-md">
              <q-input
                v-model="formUser.first_name"
                color="dark"
                bg-color="white"
                label="First Name"
                outlined
                dense
                standout
                type="text"
              />
              <q-input
                v-model="formUser.last_name"
                color="dark"
                bg-color="white"
                label="Last Name"
                outlined
                dense
                class="q-mt-sm"
                type="text"
              />
              <q-input
                v-model="formUser.username"
                color="dark"
                bg-color="white"
                label="Enter Username"
                outlined
                dense
                class="q-mt-sm"
                type="text"
              />

              <q-input
                v-model="formUser.email"
                color="dark"
                bg-color="white"
                label="Enter Email"
                outlined
                dense
                class="q-mt-sm"
                type="email"
              />
              <q-input
                v-model="formUser.password"
                color="dark"
                bg-color="white"
                label="Enter Password"
                outlined
                dense
                class="q-mt-sm"
                type="password"
              />
            </q-card-section>
            <q-card-section>
              <q-btn
                color="orange"
                class="text-capitalize text-subtitle1 text-bold fit"
                type="submit"
                label="Add"
              />
            </q-card-section>
          </q-form>
        </q-card>
      </q-dialog>
    </div>

    <!-- showing the response from server -->
    <div>
      <q-dialog v-model="alertModel" persistent>
        <q-card>
          <q-card-section>
            {{ alertMessage }}
          </q-card-section>
          <q-card-actions align="right">
            <q-btn label="OK" color="primary" @click="alertModel = false" />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>

    <q-markup-table
      separator="cell"
      class="bg-transparent shadow-4 q-my-md text-dark"
      flat
      bordered
    >
      <thead>
        <tr>
          <th class="text-left">#</th>
          <th class="text-justify">Image</th>
          <th class="text-justify">Username</th>
          <th class="text-justify">Phone</th>
          <th class="text-justify">Email</th>
          <th class="text-justify">Status</th>
          <th class="text-justify">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="official in officials" :key="official">
          <td class="text-left">{{ official.id }}</td>
          <td class="text-right">{{ official.first_name }}</td>
          <td class="text-center">
            {{ official.last_name }}
          </td>
          <q-td>{{ official.username }}</q-td>
          <td>{{ official.email }}</td>
          <td>assistant</td>

          <td class="text-right q-gutter-xs">
            <a class="text-orange" @click="editModel = true">
              <q-btn size="10px" round color="light-green-10" icon="edit" />
            </a>
            <a class="text-orange">
              <q-btn size="10px" round color="red" icon="delete" />
            </a>
          </td>
        </tr>
      </tbody>
    </q-markup-table>
  </div>
</template>

<script>
import { api } from "src/boot/axios";
import { ref } from "vue";

export default {
  name: "AddUser",
  setup() {
    return {
      userAdd: ref(false),
      officials: ref([]),
      formUser: ref({
        first_name: "",
        last_name: "",
        username: "",
        email: "",
        password: "",
      }),

      error: ref(""),
      alertModel: ref(false),
      alertMessage: ref(""),
    };
  },
  methods: {
    signup() {
      this.error = "";

      api
        .post("users/user/", this.formUser)
        .then((response) => {
          this.alertMessage = response.data.message;
          this.alertModel = true;
          this.formUser = "";
          setTimeout(() => {
            this.userAdd = false;
            this.alertModel = false;
          }, 5000);
          console.log(response.data);
        })
        .catch((error) => {
          this.alertMessage = error.response.data.error;
          this.alertModel = true;
          this.error = error.response.data.error || "An error Occured during signup";
        });
    },

    getOfficials() {
      api
        .get("user/", this.formUser)
        .then((response) => {
          // console.log(response.data);
          this.officials = response.data;
        })
        .catch((error) => {
          console.log(error.response.data.error);
        });
    },
  },
  created() {
    this.getOfficials();
  },
};
</script>
<style scoped></style>
