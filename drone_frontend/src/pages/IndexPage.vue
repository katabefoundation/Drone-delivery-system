<template>
  <q-page>
    <VideoBackground/>
    <div class="container q-pt-md" >
      <LoginView></LoginView>
      <AboutView></AboutView>
    </div>
    <footer-comp/>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import VideoBackground from "components/VideoBackground.vue";
import AboutView from "components/AboutView.vue"
import FooterComp from 'components/User/FooterComp.vue';
import LoginView from 'components/LoginView.vue';
export default defineComponent({
  name: 'IndexPage',
  components: { VideoBackground, AboutView,
    FooterComp, LoginView
  }

})
</script>
<style>
.container{
  background-color: rgba(226, 226, 226, 0.932);
}
</style>
