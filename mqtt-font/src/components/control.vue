<template>
  <div>
    <el-container>
      <el-main>
        <el-form>
          <el-form-item label="窗帘控制">
            <el-switch
                v-model="windows"
                active-color="#13ce66"
            >
            </el-switch>
          </el-form-item>
          <el-form-item label="红外监控">
            <el-switch
                v-model="persons"
                active-color="#13ce66"
            >
            </el-switch>
          </el-form-item>
          <el-form-item label="燃气控制">
            <el-switch
                v-model="gass"
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
      windows: true,
      gass: true,
      persons: true
    }
  },
  watch: {
    windows() {
      // 发现代码变化就用这个
      console.log('window changed')
      this.$socket.emit('publish', {
        topic: 'windows',
        message: this.windows
      })
    },
    gass() {
      this.$socket.emit('publish', {
        topic: 'gass',
        message: this.gass
      })
    },
    persons() {
      this.$socket.emit('publish', {
        topic: 'persons',
        message: this.persons
      })
    }
  }


}
</script>

<style scoped>

</style>
