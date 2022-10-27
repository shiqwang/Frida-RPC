<template>

    <div class="mt-2 small">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item active">
                <RouterLink to="/">Devices</RouterLink>
            </li>
            <li class="breadcrumb-item active">RpcSetting</li>
            <li class="breadcrumb-item active">{{ deviceId }}</li>
          </ol>
        </nav>
      </div>

    <form>
        <div class="form-group">
            <label>App select</label>
            <select class="form-control" v-model="appId" required>
                <option v-for="app in apps" :value="app.name">{{app.pid}} - {{app.id}} - {{app.name}}</option>
            </select>
        </div>
        <div class="form-group">
            <label>HookJS select</label>
            <select class="form-control" v-model="hookJs" required>
                <option v-for="r in hookjs" :value="r">{{r}}</option>
            </select>
        </div>
        <template v-if="!isRunning">
            <button type="button" class="btn btn-primary btn-lg btn-block" disabled v-if="isLoading">
                <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                Starting
            </button>
            <button type="button" class="btn btn-primary btn-lg btn-block" v-if="!isLoading" @click="startRPC">
                Start
            </button>
        </template>
        <template v-if="isRunning">
            <button type="button" class="btn btn-danger btn-lg btn-block" @click="stopRPC">
                <!-- <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> -->
                Stop
            </button>
        </template>

    </form>


    <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-delay="2000" style="position:absolute;top:1rem;right:1rem">
        <div class="toast-header">
            <!-- <img src="..." class="rounded mr-2" alt="..."> -->
            <strong class="mr-auto">Frida-RPC</strong>
            <small>1 second ago</small>
            <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="toast-body">
            Hello, world! This is a toast message.
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            apps: [],
            hookjs: [],
            isLoading: false,
            appId: null,
            hookJs: null,
            isRunning: false,
            deviceId: ''
        }
    },
    methods: {
        startRPC() {
            $('.toast').toast('show')

            this.isLoading = true
            this.$axios.get('http://127.0.0.1:5555/admin/start', {
                params: {
                    device_id: this.$route.params.deviceId,
                    hook_js: this.hookJs,
                    app_id: this.appId
                }
            }).then(res => {
                if (res.data.code == 0) {
                    this.isRunning = true
                }

            }).catch(err => {
                console.log(err)
            })

        },
        stopRPC() {
            this.$axios.get('http://127.0.0.1:5555/admin/stop', {
                params: {
                    device_id: this.$route.params.deviceId
                }
            }).then(res => {
                if (res.data.code == 0) {
                    this.isRunning = false
                }

            }).catch(err => {
                console.log(err)
            })
        },
        getRPCStatus(deviceId) {
            this.$axios.get('http://127.0.0.1:5555/admin/device_rpc', {
                params: { 'device_id': this.$route.params.deviceId }
            }).then(res => {
                if (res.data.code == 0) {
                    this.appId = res.data.data.app_id
                    this.hookJs = res.data.data.hook_js
                    this.isRunning = true
                }

            }).catch(err => {
                console.log(err)
            })
        },
        getApps(deviceId) {
            this.$axios.get('http://127.0.0.1:5555/admin/apps', {
                params: { 'device_id': this.$route.params.deviceId }
            }).then(res => {
                this.apps = res.data
            }).catch(err => {
                console.log(err)
            })
        },
        getHookJsList() {
            this.$axios.get('http://127.0.0.1:5555/admin/hookjs').then(res => {
                this.hookjs = res.data
            }).catch(err => {
                console.log(err)
            })
        }
    },
    mounted() {
        this.deviceId = this.$route.params.deviceId
        this.getApps()
        this.getHookJsList()
        this.getRPCStatus()
    }
}
</script>