<template>

    <div class="mt-2 small">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item active"><RouterLink to="/">Devices</RouterLink></li>
                <li class="breadcrumb-item active">APKS</li>
            </ol>
        </nav>
    </div>

    <ul class="list-group">
        <li class="list-group-item" v-for="item in data">
            {{item}}
        </li>
    </ul>
</template>

<script>
export default {
    mounted() {
        console.log(this.$route.params.deviceId)
        this.deviceId = this.$route.params.deviceId
        this.getApps()
    },
    data() {
        return {
            data: [],
            deviceId: '',
        }
    },
    methods: {
        getApps(deviceId) {
            this.$axios.get('http://127.0.0.1:5555/admin/apks').then(res => {
                this.data = res.data
            }).catch(err => {
                console.log(err)
            })
        }
    }
}
</script>