<script>
export default {
  props: ['data']
}
</script>

<template>
  <a class="list-group-item list-group-item-action shadow-sm">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1"><span class="user-select-all">{{ data.name }}</span> - <span class="user-select-all">{{ data.id }}</span> <span class="badge badge-success" v-if="data.is_running">running</span></h5>
      <!-- <small>-</small> -->
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-expanded="false">
          Options
        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
          <router-link class="dropdown-item" :to="{name:'rpc-settings', params:{deviceId: data.id}}">RPC</router-link>
          <template v-if="data.is_running">
          <router-link class="dropdown-item" :to="{name:'rpc-list', params:{deviceId: data.id}}">API</router-link>
          </template>
          <router-link class="dropdown-item" :to="{name:'apps',params:{deviceId: data.id}}">Apps</router-link>
          <a class="dropdown-item" href="#">Props</a>
          <router-link class="dropdown-item" :to="{name:'monitor-settings', params:{deviceId: data.id}}">Monitor</router-link>
        </div>
      </div>
    </div>
    <p class="mb-1">
      <span class="badge badge-info">{{ data.type }}</span>
      <template v-if="data.is_running">
        &nbsp;<span class="badge badge-info">{{ data.app_id }}</span>
      </template>
      <template v-if="data.is_running">
        &nbsp;<span class="badge badge-info">{{ data.hook_js }}</span>
      </template>
      
    </p>
    <!-- <small>{{ data.type }}</small> -->
  </a>
</template>