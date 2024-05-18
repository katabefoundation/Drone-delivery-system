import { store } from 'quasar/wrappers'
import { createPinia } from 'pinia'
import { useRouter } from 'vue-router'



export default store((/* { ssrContext } */) => {
  const pinia = createPinia()
  const router = useRouter();
  // You can add Pinia plugins here
  // pinia.use(SomePiniaPlugin)
  pinia.use(()=>{
    pinia.router = router
  })

  return pinia
})
