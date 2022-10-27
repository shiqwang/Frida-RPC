<template>

    <div class="mt-2 small">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item active">
                    <RouterLink to="/">Devices</RouterLink>
                </li>
                <li class="breadcrumb-item active">API</li>
            </ol>
        </nav>
    </div>




    <div class="card" v-for="(item, key) in data">
        <div class="card-header">
            {{key}}
        </div>
        <div class="card-body p-0">
            <ul class="list-group list-group-flush">
                <li class="list-group-item" v-for="r in item">
                    {{r}}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    created() {
        console.log(this.$route.params.deviceId)
        this.deviceId = this.$route.params.deviceId
        this.$axios.get('http://127.0.0.1:5555/admin/rpc_list', {
            params: {
                device_id: this.$route.params.deviceId
            }
        }).then(res => {
            console.log(res.data)
            this.data = res.data
        }).catch(err => {

        })
    },
    data() {
        return {
            deviceId: '',
            data: []
        }
    }
}
</script>