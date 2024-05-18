<template>
  <div class="row q-col-gutter-md justify-between">
    <!-- total sent requests -->
    <q-card
      class="col-12 col-md-4 card q-ma-md q-pa-md"
      style="background: linear-gradient(to right, indigo, blue)"
    >
      <q-card-section class="row">
        <div class="text-h6">
          <q-icon name="description" :size="icon.size" />
        </div>
        <div class="text-h5 col text-right">
          <div>Total</div>
          <div>45</div>
        </div>
      </q-card-section>
    </q-card>
    <!-- pending -->
    <q-card
      class="col-12 col-md-4 q-ma-md q-pa-md card"
      style="background: linear-gradient(to right, orange, brown)"
    >
      <q-card-section class="row">
        <div class="text-h6">
          <q-icon name="schedule" :size="icon.size" />
        </div>
        <q-space />
        <div class="text-weight-bold text-body1 col text-right">
          <div>Pending Request</div>
          <div class="text-h5">{{ pending }}</div>
        </div>
      </q-card-section>
    </q-card>
    <!-- Request saved in draft  -->
    <q-card
      class="col-12 col-md-4 q-ma-md q-pa-md card"
      style="background: linear-gradient(to right, #ff1744, #f50057)"
    >
      <q-card-section class="row justify-between items-center q-pt-md q-pb-md">
        <div class="text-h6">
          <q-icon name="drafts" class="text-white" :size="icon.size" />
        </div>
        <div class="text-h5 col text-right">
          <div class="text-weight-bold text-body1">Draft Requests</div>
          <div>{{ drafts }}</div>
        </div>
      </q-card-section>
    </q-card>

    <!-- approved requests -->
    <q-card
      class="col-12 col-md-4 q-ma-md q-pa-md card"
      style="background: linear-gradient(to right, navy, blue)"
    >
      <q-card-section class="row">
        <div class="text-h6">
          <q-icon name="check" :size="icon.size" />
        </div>
        <div class="col text-right">
          <div class="text-weight-bold text-body1 col text-right">Aproved Request</div>
          <div>{{ approved }}</div>
        </div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { ref } from "vue";

const icon = { size: "50px" };
export default {
  components: {},
  setup() {
    return {
      Total: "50",
      approved: "40",
      pending: "5",
      drafts: ref("10"),
      icon,
    };
  },
};
</script>

<style scoped>
.card {
  color: #fff;
  height: 100px;
  width: 250px;
}
</style>
