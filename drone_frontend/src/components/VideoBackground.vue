<template>
  <div class="video-background">
    <video autoplay muted loop playsinline>
      <source src="~assets/statics/background.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <div class="content">
     <IndexCard></IndexCard>
    </div>
  </div>
</template>

<script>
import IndexCard from './User/IndexCard.vue'
export default {
  components: { IndexCard },
  name: 'VideoBackground',
};
</script>

<style scoped>
.video-background {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.video-background video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.content {
  position: relative;
  z-index: 1;
  color: #fff; 
}
</style>
