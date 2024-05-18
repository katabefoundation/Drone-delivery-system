<template>

  <div class="q-pa-md ">
    <q-table
      flat
      bordered
      :rows="rows"
      :columns="columns"
      row-key="id"
      :filter="filter">
      <!-- preventing overflow of myRequest Location -->
      <template v-slot:body-cell-myRequest="myRequest">
        <q-td :props="myRequest" class="truncate">
          <div class="myRequest-data" >
            {{ myRequest.row.myRequest }}
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
    <q-dialog v-model="showRowData"  persistent >
      <q-card class="text-center">
        <q-card-section >
          <div v-if="selectedRow">
            <div class="flex flex-center items-center justify-between">
              <div class="text-subtitle2">From: {{ selectedRow.sender }} </div>
            </div>
            <div  class="text-h5 text-center">{{ selectedRow.type }}</div>
            <p class="text-body2 text-justify">{{ selectedRow.myRequest }} </p>
          </div>
        </q-card-section>
        <q-card-section class="q-pa-md q-mb-md">
          <div class="text-weight-bold text-left">{{ selectedRow.date.slice(0,-27) }}</div>
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
          <p class="text-body2">{{ selectedRow.myRequest }} </p>
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
  {name: 'type',required: true,label: 'Type',align: 'left',field: row => row.type,format: val => `${val}`,sortable: true},
  { name: 'from', label: 'From', field: 'from',align:'left'  },
  { name: 'Location', label: 'Location', field: 'Location',align:'left'  },
  { name: 'myRequest', label: 'Requested', field: 'myRequest',align:'left'  },
  { name: 'date', label: 'Time', field: 'date',align:'left' },
  { name: 'actions', label: 'Action', align:'left'  }

]

const rows = [
  { id:1,
    type: 'Request',
    from: 'Hardfield Chris',
    sender:'Rev McDonald Hill',
    myRequest:'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aperiam, officia nemo! Dicta.',
    Location: 'Sabasaba sokoni',
    date: Date(),
  },
  { id:2,
    type: 'Update',
    from: 'John Doe',
    sender:'Mr Job James',
    Location: 'Nanenane Stendi',
    myRequest:'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Qui suscipit voluptatum vel quae enim assumenda nisi, eaque, et minus esse voluptate in nam quidem quas sequi culpa? Quo, quos at.',
    date: Date(),
  },
  { id:3,
    type: 'Delete',
    from: 'Montana McLeland',
    sender:'Faudhia Maulid',
    Location: 'Ngong\'ona',
    myRequest:'You have deleted all the notifications',
    date: Date(),
  },
  { id:4,
    type: 'Request',
    from: 'Montana McLeland',
    sender:'Faudhia Maulid',
    Location: 'Social Block 9',
    myRequest:'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aperiam, officia nemo! Dicta.',
    date: Date(),
  },
  { id:5,
    type: 'Request',
    from: 'Montana McLeland',
    sender:'Faudhia Maulid',
    Location: 'Cive block 4',
    myRequest:'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aperiam, officia nemo! Dicta.',
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

.myRequest-data{
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
