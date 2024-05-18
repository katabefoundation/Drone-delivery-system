import { defineStore } from "pinia";
import { api } from "boot/axios";
import { useRouter } from "vue-router";

// const LoginFormType = {
//   username: '',
//   password: '',
// };

// const UserType = {
//   id: 0,
//   username: '',
//   email: '',
//   first_name: '',
//   last_name: '',
//   permissions: [],
// }

// const AuthCheckType = {
//   isAuthenticated: Boolean,
//   user: UserType,
// }

// export const useAppAuthStore = defineStore('drone_frontend', {
//   state: () => ({
//     loggedOut: true,
//     error: "",
//     user: {
//       id: 0,
//       username: '',
//       email: '',
//       first_name: '',
//       last_name: '',
//       permissions: [],
//     },
//     loading: false,
//     authInterval: null,
//     isAuthenticated:false,

//   }),
//   getters: { },
//   actions: {

//     async login(credentails) {
//       this.loading = true;
//       try {
//         await api.post("login/", credentails);
//         await this.authCheck();

//       } catch (errors) {

//         console.error(errors.response.data);
//         this.error = errors.response.data.error;
//         this.loggedOut = true;
//         this.user = {
//           id: 0,
//           username: '',
//           email: '',
//           first_name: '',
//           last_name: '',
//           permissions: [],
//         };
//         this.loading = false;
//       }
//     },


//     async authCheck() {
//       this.loading = true;
//       this.error = ""
//       await api.get("auth_check/")
//         .then((response) => {
//           const data = response.AuthCheckType;
//           if (data.isAuthenticated && data.user) {
//             this.user = data.user;
//             this.error = "";
//             this.loggedOut = false;
//             this.loading = false;

//             if (!this.authInterval) {
//               this.authInterval = setInterval(() => {
//                 this.authCheck();
//               }, 1000 * 60 * 20) //20 minutes in milisecond
//             }
//           } else {
//             this.error = "";
//             this.loggedOut = true;
//             this.loading = false;
//             this.authInterval = null;
//           }
//         })
//         .catch((error) => {

//           console.error(error.response.data);
//           this.error = error;
//           this.loggedOut = true;
//           this.loading = false;
//         });
//     },

//     async logout() {
//       this.loading = true;
//       try {
//         await api.get('logout/');
//         await this.authCheck();
//       } catch (error) {
//         console.error(error.response.data);
//         this.error = error.response.data.error;
//         this.loading = false;
//       }
//     },

//   },
// });

const useAppAuthStore = defineStore("drones", {
  state: () => ({
    // loggedOut: true,
    error: "",
    user: null,
    loading: false,
    authInterval: null
  }),
  actions: {
    async login(credentails) {
      this.loading = true;
      try {
        await api.post("api1/login/", credentails);
        await this.authCheck();
        await this.getUser();
      } catch (e) {
        console.error(e.response.data);
        this.error = e.response.data.error;
        // this.loggedOut = true;
        this.user = null;
        // this.loading = false;
      }finally{
        this.loading = false
      }
    },
    async register(userData){
      this.loading = true;
      try {
        await api.post("api/register/",userData);
        await this.authCheck();

      } catch (e) {
        console.error(e.response.data);
        this.error = e.response.data.error;
        this.loggedOut = true;
        this.user = null;
        this.loading = false;
      }
    },
    async authCheck() {
      this.loading = true;
      try {
        const response = await api.get("api1/auth_check/");
        const data = response.data;

        if (data.isAuthenticated && data.user) {
          this.user = data.user;
          this.error = "";
          this.loggedOut = false;
          this.loading = false;

          if (this.authInterval) {
            this.authInterval = setInterval(() => {
              this.authCheck();
            }, 1000 * 60 * 21);
          }

          this.redirectUser(); //redirecting user to specific page

        } else {
          this.error = "";
          this.loggedOut = true;
          this.loading = false;
          clearInterval(this.authInterval);
          this.authInterval = null;
        }
      } catch (e) {
        console.error(e.response.data);
        this.error = e;
        this.loggedOut = true;
        this.loading = false;
      }
    },

    async logout() {
      this.loading = true;
      try {
        await api.get("api1/logout/");
        await this.authCheck();
        this.user = null;
      } catch (e) {
        console.error(e.response.data);
        this.error = e.response.data.error;
        this.loading = false;
      }
    },
    async getUser(){
      try {
        const response = await api.get('api/user/');
        this.user = response.data;
      } catch (e) {
        this.user = null;        
      }
    },

    redirectUser(){
      const router = useRouter();

      if (this.user && this.user.permissions.includes('admin')) {
        router.push({name:'AdminDashboard'});
      } else {
        router.push({name:'UserDashboard'})
      }
    },
  }
});
export { useAppAuthStore };

