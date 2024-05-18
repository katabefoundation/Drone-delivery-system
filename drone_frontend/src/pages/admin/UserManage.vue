<template>
  <q-page padding>
    <q-tabs
      v-model="tab"
      no-caps
      active-color="green"
      inline-label
      class=" shadow-18" align="justify"
      narrow-indicator
      outside-arrows>
        <q-tab active-class="flat-active-tab"  name="active_user" icon="group" label="Active Users"></q-tab>
        <q-tab name="deactivate" icon="group_off" label="Deactivated Users"></q-tab>
        <q-tab label="Users" name="AllUsers" icon="groups"></q-tab>
      </q-tabs>


     <div class="q-gutter-y-sm">
      <q-tab-panels v-model="tab" animated transition-prev="fade" transition-next="fade" class="text-grey bg-transparent">

        <!-- department -->
        <q-tab-panel name="active_user">
          Active users table
        </q-tab-panel>
        <q-tab-panel name="deactivate">
          Deactivated users
        </q-tab-panel>
        <q-tab-panel name="AllUsers">
          All users
          <AddUsers></AddUsers>
        </q-tab-panel>
      </q-tab-panels>
     </div>
  </q-page>
</template>

<script>
import AddUsers from 'components/admin/AddUsers';
import { useQuasar } from 'quasar';
import { ref } from 'vue';


export default {
  components: { AddUsers },
   name: 'PageName',
  setup() {
    // const $q = useQuasar()

    return {
      tab:ref('active_user'),
    }
  }
}
</script>
