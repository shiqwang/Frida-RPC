<script>
import DeviceList from './components/DeviceList.vue'
export default {
  components: { DeviceList }
}
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Frida-RPC</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
      aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-link active" href="#">Devices <span class="sr-only">(current)</span></a>
        <router-link class="nav-link" to="/rpc-list">RPC</router-link>
        <router-link class="nav-link" to="/apks">APK</router-link>
        <router-link class="nav-link" to="/hookjs">HookJS</router-link>
        <a class="nav-link" href="#">Bridge</a>
        <!-- <a class="nav-link" href="#">Api</a> -->
        <!-- <a class="nav-link" href="#">Cloud</a> -->
        <!-- <a class="nav-link" href="#">Debug</a> -->
        <!-- <a class="nav-link" href="#">Market</a> -->
        <a class="nav-link" href="#">Monitor</a>
        <!-- <a class="nav-link" href="#">Log</a> -->
        <a class="nav-link" href="#">Terminal</a>
        <!-- <a class="nav-link" href="#">Settings</a> -->
      </div>
    </div>
  </nav> 
  <router-view></router-view>
</template>