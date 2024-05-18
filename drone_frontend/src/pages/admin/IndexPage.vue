<template>
  <q-page padding>
    <div class="q-pq-md q-col-gutter-md">
      <q-toolbar>
        <q-space />
        <q-btn text-color="black" color="white" icon="fas fa-moon" @click="toggleBg" />
      </q-toolbar>
      <q-toolbar>
        <h6 class="text-weight-bold">Dashboard</h6>
        <q-space></q-space>
        <q-icon name="fas fa-calendar-minus" class="q-mr-sm" />
        <div class="text-overline">Wednesday 03 April 2024</div>
      </q-toolbar>
      <div class="row q-col-gutter-md top">
        <div class="col-md-3 col-sm-4">
          <q-card class="q-mx-md col-3">
            <div class="flex flex-center column">
              <q-circular-progress
                show-value
                font-size="12px"
                :value="75"
                size="100px"
                :thickness="0.1"
                color="teal-7"
                track-color="teal-2"
                class="q-ma-md"
              >
                79 Requests
              </q-circular-progress>
              <div>
                <q-badge color="teal-2" rounded class="q-mr-sm" /> On progress 25%
              </div>
              <div><q-badge color="teal-7" rounded class="q-mr-sm" /> Responded 75%</div>
            </div>
          </q-card>
        </div>
        <div class="col-md-3 col-sm-3">
          <q-card class="q-mx-md q-pa-md">
            <div class="text-overline">New Requests</div>
            <div class="flex flex-center row">
              <div class="text-h4 text-weight-bolder q-mr-md">30</div>
              <q-chip color="teal-1" text-color="teal-5" icon="fas fa-chevron-up"
                >30%</q-chip
              >
            </div>
          </q-card>
          <q-card class="q-mx-md q-pa-md q-mt-md">
            <div class="text-overline">Failed Requests</div>
            <div class="flex flex-center row">
              <div class="text-h4 text-weight-bolder q-mr-md">21</div>
              <q-chip color="pink-1" text-color="pink-5" icon="fas fa-chevron-down"
                >30%</q-chip
              >
            </div>
          </q-card>
        </div>
        <div class="col-md-6 col-sm-4">
          <q-card class="q-mx-md q-pa-md drones">
            <div class="text-overline text-center">Statistics</div>
            <div>
              <q-carousel
                v-model="slide"
                vertical
                thumbnails
                transition-prev="slide-down"
                transition-next="slide-up"
                swipeable
                animated
                autoplay
                navigation-active-icon="radio_button_checked"
                control-color="teal-7"
                navigation-icon="radio_button_unchecked"
                navigation
                padding
                arrows
                height="160px"
                class="text-black shadow-1 rounded-borders"
              >
                <q-carousel-slide name="info1" class="column no-wrap flex-center">
                  <q-icon name="style" size="35px" />
                  <div class="q-mt-md text-center">
                    {{ lorem }}
                  </div>
                </q-carousel-slide>
                <q-carousel-slide name="info2" class="column no-wrap flex-center">
                  <q-icon name="style" size="35px" />
                  <div class="q-mt-md text-center">
                    {{ lorem }}
                  </div>
                </q-carousel-slide>
                <q-carousel-slide name="info3" class="column no-wrap flex-center">
                  <q-icon name="style" size="35px" />
                  <div class="q-mt-md text-center">
                    {{ lorem }}
                  </div>
                </q-carousel-slide>
              </q-carousel>
            </div>
          </q-card>
        </div>
      </div>
      <q-toolbar>
        <div class="text-overline">Events</div>
        <q-space />
        <div class="text-overline">Today's Request</div>

        <!--make this router-link thus when clicked it goes to requests  -->
        <div class="text-caption text-teal q-ml-md cursor-pointer" to="/">
          All Request
        </div>
        <q-icon name="chevron_right" size="18px" color="teal" class="cursor-pointer" />
      </q-toolbar>
      <div class="row q-col-gutter-md q-pa-md">
        <div class="col-md-6 col-sm-6 col-xs-12">
          <q-card class="card1 q-mx-md q-pa-sm" bordered>
            <div class="row q-col-gutter-md">
              <div class="col-6">
                <div class="text-caption">Team Meeting</div>
                <div class="text-caption text-grey-5">10:00 - 14:00</div>
                <div>
                  <q-avatar
                    v-for="index in 5"
                    :key="index"
                    size="40px"
                    class="overlapping"
                    :style="`left: ${index * 25}px`"
                  >
                    <img :src="require(`assets/statics/img${index}.jpg`)" />
                  </q-avatar>
                </div>
              </div>
              <div class="col-6">
                <div class="flex justify-end row">
                  <q-toggle color="teal" val="toggle1" v-model="selection" />
                </div>

                <div class="flex justify-end row">
                  <q-btn round icon="edit" size="10px" color="black" class="q-mr-sm" />
                  <q-btn
                    round
                    icon="chevron_right"
                    size="10px"
                    color="teal"
                    class="float-end"
                  />
                </div>
              </div>
            </div>
          </q-card>

          <q-card class="card1 q-mx-md q-pa-sm q-my-md" bordered>
            <div class="row q-col-gutter-md">
              <div class="col-6">
                <div class="text-caption">Prizes</div>
                <div class="text-caption text-grey-5">10:00 - 14:00</div>
                <div>
                  <q-avatar
                    v-for="index in 5"
                    :key="index"
                    size="40px"
                    class="overlapping"
                    :style="`left: ${index * 25}px`"
                  >
                    <img :src="require(`assets/statics/img${index}.jpg`)" />
                  </q-avatar>
                </div>
              </div>
              <div class="col-6">
                <div class="flex justify-end row">
                  <q-toggle color="teal" val="blue" v-model="selection1" />
                </div>

                <div class="flex justify-end row">
                  <q-btn round icon="edit" size="10px" color="black" class="q-mr-sm" />
                  <q-btn
                    round
                    icon="chevron_right"
                    size="10px"
                    color="teal"
                    class="float-end"
                  />
                </div>
              </div>
            </div>
          </q-card>
        </div>

        <div class="col-6 col-md-6 col-sm-6 col-xs-12">
          <q-card class="q-mx-md q-pa-sm">
            <div class="row q-col-gutter-md">
              <div class="col-3">
                <div class="text-caption text-weight-bolder q-mt-lg">10:00 am</div>
              </div>
              <div class="col-9">
                <q-card class="q-px-sm colorCard shadows-30">
                  <q-item>
                    <q-item-section avatar>
                      <q-avatar>
                        <img src="~assets/statics/img1.jpg" alt="" />
                      </q-avatar>
                    </q-item-section>
                    <q-item-section>
                      <q-item-label>Donatello</q-item-label>
                      <q-item-label caption
                        >Ye who have sayeth thy will cometh unto you...</q-item-label
                      >
                    </q-item-section>
                    <q-item-section side>
                      <q-icon name="more_vert" />
                      <!-- fas fa-ellipsis-vertical -->
                    </q-item-section>
                  </q-item>
                </q-card>
              </div>
            </div>

            <div class="row q-col-gutter-md q-my-xs">
              <div class="col-3">
                <div class="text-caption text-weight-bolder q-mt-lg">10:00 am</div>
              </div>
              <div class="col-9">
                <q-card class="q-px-sm colorCard shadows-30">
                  <q-item>
                    <q-item-section avatar>
                      <q-avatar>
                        <img src="~assets/statics/img6.jpg" alt="" />
                      </q-avatar>
                    </q-item-section>
                    <q-item-section>
                      <q-item-label>Patricia</q-item-label>
                      <q-item-label caption
                        >Ye who have sayeth thy will cometh unto you...</q-item-label
                      >
                    </q-item-section>
                    <q-item-section side>
                      <!-- <q-icon name="more_vert"/> -->
                      <q-btn icon="more_vert" flat dense v class="absolute-right" />
                      <!-- fas fa-ellipsis-vertical -->
                    </q-item-section>
                  </q-item>
                </q-card>
              </div>
            </div>
          </q-card>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { useQuasar } from "quasar";
import { ref } from "vue";

export default {
  components: {},
  name: "AdminDashboard",
  
  setup() {
    const $q = useQuasar();
    return {
      slide: ref("info1"),
      lorem: ref(
        "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ducimus laboriosam voluptatum cupiditate omnis! Illum, praesentium."
      ),
      selection: ref(true),
      selection1: ref(false),
    };
  },
  methods: {
    toggleBg() {
      // this.$q.dark.set(true);
      this.$q.dark.toggle();
    },
  },
};
</script>
<style>
.drones {
  height: 220px;
}
.overlapping {
  border: 2px solid white;
  position: absolute;
  margin-left: -20px;
}
.card1 {
  height: 100px;
}
.top {
  margin-top: -40px;
}
.colorCard {
  background: #f8f8f8;
}
</style>
