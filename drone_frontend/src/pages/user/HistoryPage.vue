<template>
  <q-page padding>
    <HistoryTable></HistoryTable>
  </q-page>
</template>

<script>
import HistoryTable from 'components/User/HistoryTable'
export default {
  components: { HistoryTable },
  name: 'HistoryPage',
}
</script>
