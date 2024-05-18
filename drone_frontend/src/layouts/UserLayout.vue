<template>
  <q-layout view="hHh lpr fff">
    <q-header bordered class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" class="q-mr-sm" />
        <q-toolbar-title>
          <q-avatar>
            <q-icon name="food_bank" />
          </q-avatar>
          {{ owners }}
        </q-toolbar-title>

        <!-- profile details -->
        <q-space />

        <div class="q-px-md">
          <div
            icon="notifications"
            @click.stop="showNotifications = !showNotifications"
            class="cursor-pointer q-mr-md relative-position"
          >
            <q-icon name="notifications" size="2.6em" />
            <q-badge floating rounded color="red" v-if="unreadNotifications > 0">{{
              unreadNotifications
            }}</q-badge>
          </div>

          <!-- Notification Dropdown -->
          <q-menu v-model="showNotifications" anchor="bottom right" self="top right">
            <q-list
              style="width: 300px"
              dense
              class="bg-grey-8 clear"
              v-for="(notification, index) in notifications"
              :key="notification.id"
            >
              <q-item clickable>
                <!-- sender's img -->
                <q-item-section avatar>
                  <q-avatar>
                    <img src="~assets/profile.png" :alt="notification.senderName" />
                  </q-avatar>
                </q-item-section>

                <q-item-section>
                  <q-item-label class="text-white">
                    {{ notification.senderName }}
                  </q-item-label>
                  <q-item-label
                    caption
                    style="
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                      max-width: 90%;
                    "
                  >
                    {{ notification.text }}
                  </q-item-label>
                </q-item-section>

                <q-item-section
                  side
                  style="font-size: 10px; margin-right: -10px; width: 24%"
                >
                  <span class="flex-end text-grey-5 text-weight-bold">
                    {{ notification.time }}
                  </span>
                </q-item-section>
              </q-item>
              <q-separator v-if="index !== notification" color="orange" dark />
            </q-list>
          </q-menu>
        </div>

        <!-- profile details -->
        <div class="q-px-md">
          <div flat @click.stop="showMenu = !showMenu" class="cursor-pointer float-right">
            <q-avatar>
              <img src="~assets/profile.png" alt="profile" />
            </q-avatar>
          </div>
          <q-menu v-model="showMenu" anchor="bottom right" self="top right">
            <!-- dropdown options -->
            <q-list class="clear bg-teal text-white">
              <q-item
                clickable
                v-close-popup
                @click="goToProfile"
                class="items-center justify-between"
              >
                <q-icon name="edit" />
                <q-item-section> Profile </q-item-section>
              </q-item>
              <q-item
                clickable
                v-close-popup
                @click="logout"
                class="items-center justify-between"
              >
                <q-icon name="logout" />
                <q-item-section>Logout</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </div>
      </q-toolbar>
    </q-header>

    <!-- A left Drawer  -->

    <q-drawer v-model="leftDrawerOpen" side="left" bordered>
      <q-list>
        <q-item-label header class="text-secondary">
          {{ owners }}
        </q-item-label>

        <!-- a drawer left -->
        <div v-for="(link1, index) in essentialLinks" :key="index">
          <!-- without dropdown -->
          <q-item v-if="!link1.dropdown" :to="link1.link">
            <q-item-section avatar>
              <q-icon :name="link1.icon" />
            </q-item-section>
            <q-item-section>
              {{ link1.title }}
            </q-item-section>
          </q-item>

          <!-- with dropdown -->
          <q-expansion-item v-if="link1.dropdown" :label="link1.title" :icon="link1.icon">
            <q-item
              v-for="(dropdownLink, dIndex) in link1.dropdown"
              :key="dIndex"
              clickable
              :to="dropdownLink.link"
            >
              &nbsp; &nbsp; &nbsp;
              <q-item-section avatar>
                <q-icon :name="dropdownLink.icon" />
              </q-item-section>
              <q-item-section>
                {{ dropdownLink.title }}
              </q-item-section>
            </q-item>
          </q-expansion-item>
        </div>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <!-- back to top -->
    <q-fab
      v-if="showScrollToTop"
      vertical-align="bottom"
      horizontal-align="right"
      class="fixed-bottom-right q-ma-md"
      icon="arrow_upward"
      translate="yes"
      color="orange-2"
      text-color="secondary"
      @click="scrollToTop"
      style="z-index: 5"
    />
  </q-layout>
</template>

<script>
import { defineAsyncComponent, ref } from "vue";
import { useQuasar, QSpinnerGears } from "quasar";

const linksList = [
  {
    title: "Dashboard",
    icon: "home",
    link: "/user/dashboard",
  },
  {
    title: "Notification",
    icon: "notifications",
    link: "/user/notification",
  },

  {
    title: "History",
    icon: "history",
    link: "/user/history",
  },
  {
    title: "Help",
    icon: "help",
    link: "/user/help",
  },
  {
    title: "Privacy and Policy",
    icon: "shield",
    link: "/user/policy",
  },
  {
    title: "Profile Setting",
    icon: "manage_accounts",
    link: "/user/edit_profile",
  },
];

const Notification = [
  {
    id: 1,
    text: "Notification 1",
    senderImg: "image1",
    senderName: "Miguel Samuel",
    time: "24 may 23",
  },
  {
    id: 2,
    text: "Changed his profile and 1",
    senderImg: "image1",
    senderName: "Zwangendaba muthwale",
    time: "Yesterday",
  },
  {
    id: 3,
    text: "Notification 2 lorem is genius",
    senderImg: "image2",
    senderName: "Joel Smith",
    time: "09:00 AM",
  },
];

export default {
  setup() {
    const $q = useQuasar();
    const leftDrawerOpen = ref(false);
    const showScrollToTop = ref(false);
    const checkScroll = () => {
      if (window.pageYOffset > 300) {
        showScrollToTop.value = true;
      } else {
        showScrollToTop.value = false;
      }
    };

    window.addEventListener("scroll", checkScroll);
    const scrollToTop = () => {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    };

    return {
      leftDrawerOpen,
      essentialLinks: linksList,
      owners: "HIS3",
      showScrollToTop,
      showMenu: ref(false),
      showNotifications: ref(false),
      notifications: Notification,
      scrollToTop,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },

  beforeUnmount() {
    window.removeEventListener("scroll", this.checkScroll);
  },
  computed: {
    unreadNotifications() {
      return this.notifications.length;
    },
  },
  methods: {
    goToProfile() {
      alert("going to profile");
    },
    logout() {
      // alert("Loging out ....")
      $q.notify({
        spinner: QSpinnerGears,
        message: "Logiging out ....",
        position: "center",
        color: "dark",
      });
    },
  },
};
</script>

<style scoped>
.text-break {
  word-break: break-all;
}
.overflow-wrap {
  overflow-wrap: break-word;
}
</style>
