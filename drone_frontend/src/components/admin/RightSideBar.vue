<template>
  <q-drawer
    show-if-above
    side="right"
    bordered
    v-model="rightBar"
    :width="300">

    <q-toolbar class="q-mt-lg">
      <q-space/>
      <q-btn color="blue-5" icon="notifications"  round dense  >
        <q-badge rounded floating color="teal" text-color="smoke" :label="90"/>
      </q-btn>
    </q-toolbar>
    <div class="flex flex-center column" style="margin-top: -30px;">
      <q-avatar >
        <img src="~assets/statics/img5.jpg" alt="">
      </q-avatar>
      <q-item-label caption class="q-my-md">
        Your Activity Today
      </q-item-label>
      <div class="text-h5"><strong>86%</strong></div>
    </div>
    <q-card class="q-mx-md">
      <q-toolbar>
        <div class=" text-capitalize">all activity</div>
        <q-space/>
        <q-btn  rounded flat icon="chevron_right" size="10px" color="pink-14"/>
      </q-toolbar>
    </q-card>
    <q-card class="q-mx-md q-mt-lg">
      <q-toolbar>
        <div class="text-overline text-weight-bolder">Support Chat</div>
        <q-space/>
        <q-avatar size="25px">
          <img src="~assets/statics/canvas.png" alt="" class="bg-primary">
        </q-avatar>
        <div class="text-overline q-ml-sm">John Doe</div>
      </q-toolbar>
      <q-separator/>
      <div class="q-pa-md row justify-center">
        <div style="width: 100%; max-width: 400px;">
          <q-chat-message name="me" avatar="~assets/statics/drive-slider3.jpg" :text="['Hey, Mickky']" sent stamp="7 minutes ago" bg-color="deep-orange-1"  />
          <q-chat-message name="Mickky" avatar="~assets/statics/drive-slider3.jpg" :text="['Yup, Bro! Is everything alright']" bg-color="teal-2" stamp="3 minutes ago"/>
        </div>
      </div>
      <q-input outlined rounded dense bottom-slots v-model="text" label="Type your message"  class="q-t-sm" type="text" >
        <template v-slot:append>
          <QBtn flat dense round icon="fas fa-paper-plane"/>
        </template>
      </q-input>

    </q-card>
  </q-drawer>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'RightSideBar',
  setup () {
    return {
      text:ref(''),
      rightBar:false
    }
  }
}
</script>
<style>
.q-item__section--main.none{
  flex: none;
}
.top{
  margin-top: -10px;
}
</style>
