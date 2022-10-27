import { createApp } from 'vue'
import App from './App.vue'
import {createRouter, createWebHashHistory} from 'vue-router'

import DeviceList from './components/DeviceList.vue'

import DevicePropList from './components/DevicePropList.vue'
import AppList from './components/AppList.vue'
import RpcSettings from './components/RpcSettings.vue'
import MonitorSetting from './components/MonitorSetting.vue'
import RPCList from './components/RPCList.vue'
import HookJSList from './components/HookJSList.vue'
import ApkList from './components/ApkList.vue'

import axios from 'axios'

// import {BootstrapVue3} from 'bootstrap-vue-3'

import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

const Home = { template: '<div>Home</div>' }

// import './assets/main.css'

const routes = [
    {path: '/', component: DeviceList},
    {path: '/props', component: DevicePropList},
    {path: '/apps/:deviceId', name: 'apps', component: AppList},
    {path: '/rpc-settings/:deviceId', name: 'rpc-settings', component: RpcSettings},
    {path: '/monitor-settings/:deviceId', name: 'monitor-settings', component: MonitorSetting},
    {path: '/rpc-list/:deviceId*', name: 'rpc-list', component: RPCList},
    {path: '/hookjs', component: HookJSList},
    {path: '/apks', component: ApkList},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

const app = createApp(App)

app.config.globalProperties.$axios = axios

app.use(router)

// app.use(BootstrapVue3)

app.mount('#app')