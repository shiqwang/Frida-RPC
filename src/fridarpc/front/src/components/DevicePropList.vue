<script>
export default {
    data() {
        return {
            data: []
        }
    },
    mounted() {
        this.$axios.get('http://192.168.200.49:5555/admin/devices_prop').then(res=>{
            console.log(res)
            this.data = res.data
        }).catch(err => {
            console.log(err)
        })
    }
}
</script>

<template>
    <table class="table">
        <thead>
          <tr>
            <th scope="col">key</th>
            <th scope="col">value</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(v, k) in data">
            <th scope="row">{{ k }}</th>
            <td>{{ v }}</td>
          </tr>
        </tbody>
      </table>
</template>