<template>
  <q-page padding>

    <!-- drone info, battery_alert, delivery info,drone controller-->

  <div class="q-gutter-md">
    <q-tabs
      v-model="drone_tabs"
      align="justify"
      inline-label
      no-caps
      narrow-indicator
      indicator-color="blue"
      active-color="deep-orange"
      outside-arrows
      class="bg-transparent">
      <q-tab name="delivery_info" icon="info" label="Delivery Info" class="text-capitalize"/>
      <q-tab name="drone_control" icon="flight_takeoff" label="Control" class="text-capitalize" @click="showCustom"/>
    </q-tabs>

    <q-tab-panels
      v-model="drone_tabs"
      animated
      transition-duration="5">
      <q-tab-panel name="delivery_info">This is info of the drone and how it perform its delivery</q-tab-panel>
      <q-tab-panel name="drone_control">
        <DroneView></DroneView>
      </q-tab-panel>

    </q-tab-panels>

    <q-btn color="purple" @click="showDefault" label="Default spinner" />
    <q-icon name="local_fire_department" size="52px" class="q-mr-md my-color" />
    <div class="q-pa-md">
    <q-btn color="purple" @click="showNotif" label="Show Notification" />
  </div>




    <!-- Buttons -->
    <!-- <div class="q-gutter-md">
      <div class="q-gutter-md">
        <q-btn label="Start" color="primary" @click="start"></q-btn>
        <q-btn label="Save" color="secondary" @click="save"></q-btn>
      </div>
    </div> -->
</div>
  </q-page>
</template>

<script>
import DroneView from 'components/admin/DroneView'
import { ref } from 'vue';
import { useQuasar, QSpinnerGears } from 'quasar'

export default {
  components: { DroneView },
  name: 'DroneManage',

  setup() {

    const $q = useQuasar()

    return {
      drone_tabs: ref('delivery_info'),
      showNotif () {
        $q.notify({
          spinner:QSpinnerGears,
          message: 'Loading ...',
          color: 'purple',
          position:'center'
        })
      },

    }
  }
}
</script>


