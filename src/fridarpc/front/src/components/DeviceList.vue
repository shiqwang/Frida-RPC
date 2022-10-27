<script>
import DeviceListItem from './DeviceListItem.vue'

export default {
    data() {
        return {
            items: [],
            loading: true,
            timer1: null,
            isLeave: false
        };
    },
    methods: {
        getDeviceList() {
            this.$axios.get("http://127.0.0.1:5555/admin/devices").then(res => {
                this.items = res.data;
                console.log(res.data);
                this.loading = false
                if (!this.isLeave) {
                    setTimeout(this.getDeviceList, 3000)
                }
            }).catch(err => {
                console.log(err)
            });
        }
    },
    beforeRouteLeave() {
        this.isLeave = true
        // clearInterval(this.timer1)
        // console.log('clear timer')
    },
    mounted() {
        this.getDeviceList()
        // this.timer1 = setInterval(this.getDeviceList, 3000)
    },
    components: { DeviceListItem }
}
</script>

<template>

    <div class="mt-2 small">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item active">Devices</li>
            </ol>
        </nav>
    </div>

    <div class="d-flex justify-content-center" v-if="loading">
        <div class="spinner-border" role="status">
            <span class="sr-only">Loading...</span>
        </div>
    </div>
    <ul class="list-group" v-if="!loading">
        <!-- <li class="list-group-item" v-for="item in items">{{ item.name }}</li> -->
        <DeviceListItem v-for="item in items" :data=item />
    </ul>

</template>