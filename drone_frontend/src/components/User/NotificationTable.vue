<template>

  <div class="q-pa-md ">
    <q-table
      flat
      bordered
      :rows="rows"
      :columns="columns"
      row-key="id"
      :filter="filter">
      <template v-slot:body-cell-content="content">
        <q-td :props="content" class="truncate">
          <div class="content-data" >
            {{ content.row.content }}
          </div>
        </q-td>
      </template>

      <template v-slot:top-left>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search" style="width: 100%;">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>

      <template v-slot:body-cell-actions="props">
        <q-td :props="props" >
          <q-btn icon="fa-solid fa-eye" color="info" flat @click="openRow(props.row)" size="10px"/>
          <q-btn icon="delete" color="red" flat @click="openDelete(props.row)"/>
        </q-td>
      </template>
    </q-table>

    <!-- dialog to read the table data -->
    <q-dialog v-model="showRowData" full-width persistent >
      <q-card class="text-center">
        <q-card-section >
          <div v-if="selectedRow">
            <div class="flex flex-center items-center justify-between">
              <div class="text-subtitle2">From: {{ selectedRow.sender }} </div>
              <div class="text-caption">{{ selectedRow.date.slice(0,-27) }}</div>
            </div>
            <div  class="text-h5 text-center">{{ selectedRow.message }}</div>
            <p class="text-body2">{{ selectedRow.content }} </p>
          </div>
        </q-card-section>
        <q-card-section class="q-pa-md q-mb-md">
          <q-btn ripple color="blue" label="OK" v-close-popup class="float-right q-mb-md text-weight-bolder"/>
        </q-card-section>
      </q-card>
    </q-dialog>

    <!-- delete the notification -->
    <q-dialog v-model="showDelete" persistent>
      <q-card>
        <q-card-section v-if="selectedRow">
          <div class="text-center">
            <q-icon name="warning" class="text-center" color="orange" size="70px"/>
          </div>
          <div  class="text-h5 text-center">Are you sure! <br>You want to delete this notification</div>
          <p class="text-body2">{{ selectedRow.content }} </p>
        </q-card-section>
        <q-card-section class="q-pa-md q-mb-md" >
          <q-btn ripple color="orange" icon="warning" label="Cancel" v-close-popup class="float-left q-mb-md"/>
          <q-btn ripple color="negative" icon="delete" label="Delete" v-close-popup class="float-right "/>
        </q-card-section>
      </q-card>
    </q-dialog>

  </div>
</template>

<script>
import { ref } from 'vue'

const columns = [
  {name: 'session',required: true,label: 'Session',align: 'left',field: row => row.session,format: val => `${val}`,sortable: true},
  { name: 'from', label: 'From', field: 'from',align:'left'  },
  { name: 'message', label: 'Message', field: 'message',align:'left'  },
  { name: 'content', label: 'Notification', field: 'content',align:'left'  },
  { name: 'date', label: 'Time', field: 'date',align:'left' },
  { name: 'actions', label: 'Action', align:'left'  }

]

const rows = [
  { id:1,
    session: 'Sunday 1st Service',
    from: 'Hardfield Chris',
    sender:'Rev McDonald Hill',
    content:'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aperiam, officia nemo! Dicta.',
    message: 'The Great Commission',
    date: Date(),
  },
  { id:2,
    session: 'Wednesday Service',
    from: 'John Doe',
    sender:'Mr Job James',
    message: 'Great Contraverse',
    content:'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Qui suscipit voluptatum vel quae enim assumenda nisi, eaque, et minus esse voluptate in nam quidem quas sequi culpa? Quo, quos at.',
    date: Date(),
  },
  { id:3,
    session: 'Friday Service',
    from: 'Montana McLeland',
    sender:'Faudhia Maulid',
    message: 'Church Life',
    content:'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aperiam, officia nemo! Dicta.',
    date: Date(),
  }
]


export default {
  // name: 'ComponentName',
  setup () {

    return {
      filter: ref(''),
      columns,
      rows,
      search:'',
      showRowData:ref(false),
      selectedRow: ref(null),
      showDelete:ref(false),
    };

  },
  methods:{
    openRow(row){
      this.selectedRow = row;
      this.showRowData = true
    },
    openDelete(row) {
      this.selectedRow = row;
      this.showDelete = true;
    }
  }
}
</script>

<style scoped>
.truncate{
  max-width: 200px;
}

.content-data{
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
