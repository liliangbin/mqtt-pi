<template>
  <div>
    <el-container>
      <el-main>
        <el-form>
          <el-form-item label="窗帘控制">
            <el-switch
                v-model="window"
                active-color="#13ce66"
            >
            </el-switch>
          </el-form-item>
          <el-form-item label="红外监控">
            <el-switch
                v-model="person"
                active-color="#13ce66"
            >
            </el-switch>
          </el-form-item>
          <el-form-item label="燃气控制">
            <el-switch
                v-model="gas"
                active-color="#13ce66"
            >
            </el-switch>
          </el-form-item>

        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "control",
  data() {
    return {
      window: false,
      gas: false,
      person: false,
    }
  },
  watch: {
    window() {
      // 发现代码变化就用这个
      this.sockets.emit('publish', {
        topic: 'window',
        message: this.window
      })
    },
    gas() {
      this.sockets.emit('publish', {
        topic: 'gas',
        message: this.gas
      })
    },
    person() {
      this.$$sockets.emit('publish', {
        topic: 'person',
        message: this.person
      })
    }
  }


}
</script>

<style scoped>

</style>
