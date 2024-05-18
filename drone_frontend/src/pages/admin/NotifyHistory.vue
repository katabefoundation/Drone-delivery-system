<template>
  <q-page padding>
       <q-tabs
      v-model="tab"
      no-caps
      inline-label
      class=" shadow-18" align="justify"
      narrow-indicator
      outside-arrows>
        <q-tab active-class="flat-active-tab" class="text-orange" name="notify" icon="notifications_active" label="Notifications"></q-tab>
        <q-tab name="history" icon="history" label="History"></q-tab>
      </q-tabs>


     <div class="q-gutter-y-sm">
      <q-tab-panels v-model="tab" animated transition-prev="fade" transition-next="fade" class="text-grey bg-transparent">

        <!-- department -->
        <q-tab-panel name="notify">
          Notifications huuuuu
        </q-tab-panel>
        <q-tab-panel name="history">
          Histories
        </q-tab-panel>
      </q-tab-panels>
     </div>
  </q-page>
</template>

<script>
import { ref } from 'vue';


export default {
  // name: 'PageName',
  setup() {
    return {
      tab:ref('notify'),
    }
  }
}
</script>
