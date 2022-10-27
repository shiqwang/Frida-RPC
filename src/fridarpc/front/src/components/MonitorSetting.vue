<template>
    <form class="m-5">
        <div class="form-group">
            <label>Channel select</label>
            <select class="form-control" v-model="channelId">
                <option value="dingding" selected>钉钉</option>
            </select>
        </div>
        <div class="form-group">
            <label for="exampleInputEmail1">Token</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
          </div>
    </form>
</template>

<script>
    export default {
        data() {
            return {
                channelId: 'dingding'
            }
        }
    }
</script>