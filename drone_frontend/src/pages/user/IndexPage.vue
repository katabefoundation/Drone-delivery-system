<template>
  <q-page padding>
    <InfoCard/>
    <RequestForm/>
  </q-page>
</template>

<script>
import RequestForm from 'components/RequestForm.vue'
import InfoCard from 'components/InfoCard.vue'
export default {
  components: {
    RequestForm, InfoCard},
  name: 'UserDashboard',
}
</script>
