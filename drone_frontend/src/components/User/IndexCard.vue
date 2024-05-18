<template>
  <q-carousel
    v-model="slide"
    animated
    navigation
    navigation-active-icon="category"
    control-color="orange"
    infinite
    :autoplay="autoplay"
    height="100vh"
    transition-prev="slide-right"
    transition-next="slide-left"
    @mouseenter="autoplay = false"
    @mouseleave="autoplay = true"
    class="bg-transparent"
    >
    <q-carousel-slide
        class="relative-position  text-orange bg-dark" style="opacity: 0.8;"
        :name="1" >
      <div class="animated-text-container  items-center justify-center">
        <h1 class="text-h1 text-bold text-white text-center  animated-text">
          Do you Know?
        </h1> 
        <h1 class="text-h3 text-center">
          We can save the live by dealing with emergencies
        </h1>
        <h1 class="text-body1 text-white text-center text-italic">
          <q>Almost 80% of injuries and accident lost their lives by lacking first aid
        </q>
      </h1>

      </div>
    </q-carousel-slide>
    <q-carousel-slide name="2" style="opacity: .7;" class="bg-black">
      <div class="animated-text-container ">
        <h1 class="text-h2 animated-text text-center">
          Join Us
        </h1> <br>
        <h1 class="text-h5 text-center q-py-md">Save the Population</h1>
          <br> <br>
        <h2 class="text-h6 text-center q-mb-none q-my-md">
          You can join us by contacting us through our social media  or contact our staffs now
        </h2>
      </div>

    </q-carousel-slide>

    <q-carousel-slide name="3" class="bg-black" style="opacity: .7;">
      <div class="animated-text-container">
        <h1 class="text-h3 animated-text q-pt-md text-center">
          We send Help! where it is needed
        </h1>
        <h1 class="text-h6 q-pa-md text-center bottom"><q>Sharing is Caring</q></h1>
      </div>
    </q-carousel-slide>


  </q-carousel>


</template>
<script>
import { ref } from 'vue';

export default {
  name: 'IndexCard',

  setup() {
    return {
      slide: ref(1),
      autoplay: ref(true),
      openLogin: false,  // Controls the modal's visibility
     form: {
      email: '',
      password: ''
    }
    }
  }
}
</script>
