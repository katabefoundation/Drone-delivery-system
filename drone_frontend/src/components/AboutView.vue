<template>
  <div class="q-pt-md">
   <div class="text-grey-10 row justify-center items-center q-pa-md det1 ">
      <div class="text-h3 col-md-4 text-orange ">Did You Know?</div>
      <div class="text-body1  col-md-8 text-quote ">
        The most common challenge for many people in Tanzania Emergency as a part of any work, activities or any life situation there is possibilities of it to occur in some cases emergency could lead to loss of someone’s life specifically in health issues there by this is the most motive toward to solve the issue of suddenly requirement of medical services to the facilities with emergency requirement or community with unpleasant event like fire accident.
      </div>
    </div>

    <div class="row items-center justify-center q-pa-md q-ma-md">
      <div class="text-h3 text-orange col-md-4 ">
        Ready to help
      </div>
      <div class="text-body1 text-black col-md-12 q-py-md  text-justify">
        Drone for enhancing emergence medical services distribution with the interest to emergency services occur in health facilities or accidental areas that need immediately medicine and their related tools the use of vehicles including cars and motorcycles can’t achieve this situation timely due to high possibilities of traffic congestion, so the drone can be uses as alternative provided the situation is serious and suddenly there by distributing these required medicine and related things at a time.
      </div>

    </div>

    <div class="text-black row justify-center items-center q-pa-md ">
      <div class="text-h4 col-md-4 text-orange-9 q-mb-md">
        Our duty is to save lives
        <q-separator color="deep-orange" style="height: 2px; width: 200px; margin: 0px auto;" class="q-mb-md"/>
      </div>
      <div class="text-body1 text-weight-light text-italic col-md-8 ">
        <q-list  bordered padding class="list1" >
          <q-item v-ripple manual-focus>
            <q-item-section>
              Rapid response towards emergency issues, provide a faster response for the requirement of the suddenly medical equipment for treatment and
            </q-item-section>
          </q-item>
          <q-item>Remote access, in rural areas where the distribution of medical and related equipment can take few using the land transport but the use of drone can be more efficient in terms of time management.</q-item>
          <q-item>Cost-efficient, the project potentially reduces the overall costs associated with emergency medical logistics, making it financially viable solution.</q-item>
          <q-item>Resources optimization., Efficient drone deployment can optimize resources utilization enabling timely and targeted delivery of medical resources based on real-time demand and situational needs.</q-item>
        </q-list>


      </div>
    </div>

    <div class="row items-center justify-center q-pa-md">
      <div class="text-h3 text-orange col-md-6 ">
        What the system could help?
        <q-separator color="deep-orange" style="height: 2px; width: 200px; margin: 0px auto;"/>
      </div>
      <div class="text-body1 text-black col-md-12 q-pr-md text-justify">
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Maiores nulla consequatur quos tempora odio repudiandae error saepe officiis placeat doloribus voluptatem tempore itaque quidem sapiente enim ullam cupiditate officia dignissimos et assumenda, id temporibus sunt? Tenetur autem ipsam maxime illo molestias, eveniet nobis, suscipit dignissimos vel soluta perferendis sequi voluptatem recusandae sit exercitationem saepe, officia voluptatum molestiae minima. Dignissimos sequi quibusdam recusandae fugiat perferendis ducimus perspiciatis eligendi fuga, eos corporis ullam nihil rerum id tempora. Itaque unde eum tempore ipsum quidem deserunt est molestias magnam. Dolorum, similique voluptate, laborum commodi ipsam soluta officia corrupti error culpa consequuntur eum nihil quam minima aperiam. Dicta veritatis, atque in quis quasi est quibusdam odio totam temporibus corrupti nihil ullam quae asperiores vero amet quos illum vel cumque maxime necessitatibus sit deleniti enim deserunt. Ad suscipit ipsam impedit! Magnam, dicta? Repellat quae necessitatibus eius amet assumenda sequi non, dolores possimus explicabo iste, mollitia porro?
      </div>

    </div>

    <div class="text-center q-pa-md">
      <div class="text-h3 text-orange-9">
        Our Team
        <q-separator color="deep-orange" style="height: 2px; width: 120px; margin: 0px auto;"/>
      </div>
      <div class="q-carousel-container q-gutter-x-sm">
        <!-- for smartphone and small devices -->
        <q-carousel
          v-model="slide_team"
          v-if="isMobile"
          :slides-per-view="2"
          animated
          arrows
          :autoplay="autoplay"
          infinite
          @mouseenter="autoplay = false"
          @mouseleave="autoplay = true"
          class="shadow-4 rounded-borders bg-transparent"
          control-color="primary"
          padding
          swipeable
          transition-next="slide-left"
          transition-prev="slide-right"
        >
          <q-carousel-slide
            v-for="(teamMember, index) in teamMembers"
            :key="index"
            :name="'teamMember_'+index"
            class="no-wrap column">
            <div class=" q-relative-position fit q-gutter-xs q-col-gutter no-wrap">
              <q-img :src="teamMember.img"
                class="rounded-borders full-height q-mx-md cursor-pointer"
                :alt="'Team Member'+index"
                @mouseover="showName(index)"
                @mouseleave="hideName(index)">
              <div v-if="displayedName === index"
                  class="team-member-info text-white">
                  <span class="text-subtitle1 no-wrap text-left"> {{ teamMember.name }}</span> <q-separator/>
                  <span class="text-weight-light text-orange text-right">{{ teamMember.position }}</span>
                  <span class="absolute-bottom no-wrap text-italic ">{{ teamMember.phone }}</span>
              </div>
              </q-img>
            </div>
          </q-carousel-slide>
        </q-carousel>

        <!-- for tablet -->
        <q-carousel
          v-model="slide_team"
          v-else-if="isTablet"
          :slides-per-view="2"
          animated
          arrows
          :autoplay="autoplay"
          infinite
          @mouseenter="autoplay = false"
          @mouseleave="autoplay = true"
          class="shadow-4 rounded-borders bg-transparent"
          control-color="primary"
          padding
          swipeable
          transition-next="slide-left"
          transition-prev="slide-right"
        >
          <q-carousel-slide
            v-for="(teamMember, index) in teamMembers"
            :key="index"
            :name="'teamMember_'+index"
            class="no-wrap column">
            <div class=" q-relative-position fit q-gutter-xs q-col-gutter no-wrap">
              <q-img :src="teamMember.img"
                class="rounded-borders full-height q-mx-md cursor-pointer"
                :alt="'Team Member'+index"
                @mouseover="showName(index)"
                @mouseleave="hideName(index)">
              <div v-if="displayedName === index"
                  class="team-member-info text-white">
                  <span class="text-subtitle1 no-wrap text-left"> {{ teamMember.name }}</span> <q-separator/>
                  <span class="text-weight-light text-orange text-right">{{ teamMember.position }}</span>
                  <span class="absolute-bottom no-wrap text-italic ">{{ teamMember.phone }}</span>
              </div>
              </q-img>
            </div>
          </q-carousel-slide>
        </q-carousel>

        <!-- for computers -->
        <div v-else class="row no-wrap">
          <div  v-for="(teamMember, index) in teamMembers"
            :key="index" class="row fit justify-start items-center q-gutter-xs q-col-gutter no-wrap">
            <q-img :src="teamMember.img"
                class="rounded-borders full-height q-mx-md cursor-pointer"
                :alt="'Team Member'+index"
                @mouseover="showName(index)"
                @mouseleave="hideName(index)">
              <div v-if="displayedName === index"
                  class="team-member-info text-white">
                  <span class="text-subtitle1 no-wrap text-left"> {{ teamMember.name }}</span> <q-separator/>
                  <span class="text-weight-light text-orange text-right">{{ teamMember.position }}</span>
                  <span class="absolute-bottom no-wrap text-italic ">{{ teamMember.phone }}</span>
              </div>
              </q-img>
          </div>

        </div>
      </div>

    </div>
  </div>

</template>

<script>
import { ref } from 'vue';

const teamMember = [
  { id: '1', name: 'John Doe', img: require('assets/statics/img1.jpg'), position: 'CEO', phone:'+255 6202 123 490' },
  { id: '2', name: 'Micky Haller', img: require('assets/statics/img4.jpg'), position: 'Programmer', phone:'+255 7202 123 490' },
  { id: '3', name: 'Angela Mwaipaya', img: require('assets/statics/img5.jpg'), position: 'Secretary', phone:'+255 6502 123 490' },
  { id: '4', name: 'Annie Wilson', img: require('assets/statics/img3.jpg'), position: 'CTO', phone:'+255 7602 123 490' },
  { id: '5', name: 'Cuzo Pligotzing', img: require('assets/statics/img2.jpg'), position: 'Tester', phone:'+255 6102 123 490' }
]
export default {
  // name: 'ComponentName',
  setup () {
    return {
      openLogin: false,
      slide_team: ref(1),
      autoplay: ref(true),
      teamMembers: teamMember,
      hovering:ref({}),
      form: ref({
        email: '',
        password: ''
      }),
      displayedName:ref(null)
    }
  },
  methods: {
    showName(index) {
      this.displayedName = index;
    },
    hideName(index) {
      this.displayedName = null;
   }
  },
  computed: {
    isMobile() {
      return this.$q.screen.xs
    },
    isTablet() {
      return this.$q.screen.sm
    }
  }
}
</script>

<style scoped>

.list1{
  border-color: rgba(172, 164, 157, 0.452);
  border-end-end-radius: 95px;
  speak-as: auto;
  border-start-start-radius: 55px ;
}
.team-member-img{
  max-width: 100%;
  height: auto;
}
.team-member-info{
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  /* background-color: rgba(82, 82, 82, 0.61); */
}
.q-carousel-container{
  max-width: 100%;
  overflow: hidden;
}
</style>
