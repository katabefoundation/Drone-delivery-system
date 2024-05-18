<template>
  <div class="fullscreen bg-white text-black text-center q-pa-md flex flex-center">
    <div>
      <div style="font-size: 30vh; font-family: small-caption; color: teal;" >
        404
      </div>

      <div class="text-h2" style="opacity:.4">
        Oops. Nothing here...
      </div>

      <q-btn
        class="q-mt-xl"
        unelevated
        to="{{ back }}"
        label="Go Home"
        color="red"
        no-caps
        flat
        glossy
        
        icon="chevron_left"
      />
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ErrorNotFound'
})
</script>
