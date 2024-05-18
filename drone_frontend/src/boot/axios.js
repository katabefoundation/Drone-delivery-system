import { boot } from 'quasar/wrappers'
import axios from "axios";

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  withCredentials:true,
  timeout:5000,

});


function getCookie(name) {
  const value = ';' + document.cookie;
  const parts = value.split(';' + name + '=');
  if (parts.length === 2)
    return parts.pop().split(';').shift() || null;
  return null
}


export default boot(({app}) => {

  api.interceptors.request.use((config) => {
    if (
      config.method?.toLowerCase() === 'post' ||
      config.method?.toLowerCase() === 'put'
    ) {
      const csrfToken = getCookie('csrftoken');
      if (csrfToken) {
        config.headers['X-CSRFToken'] = csrfToken;
      }
    }
    return config;
  });

});
export {api };

// axios.defaults.withCredentials = true;

// function getCSRFToken() {
//   let csrfToken = null;
//   const cookies = document.cookie.split(';');
//   for (let i = 0; i < cookies.length; i++) {
//     const cookie = cookies[i].trim();
//     if (cookie.startsWith('csrftoken=')) {
//       csrfToken = cookie.substring('csrftoken='.length, cookie.length);
//       break;
//     }
//   }
//   return csrfToken;
// }

// axios.post('http://localhost:8000/api/', data, {
//   headers: {
//     'X-CSRFToken': getCSRFToken(),
//   },
// })
// .then(response => {
//   console.log(response.data);
// })
// .catch(error => {
//   console.error(error);
// });