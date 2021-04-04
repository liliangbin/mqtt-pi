<template>
  <div>
    <el-container>

      <el-main>
        <el-form>
          <el-form-item label="当前室内温、湿度">
            <el-input v-model="temp"></el-input>
          </el-form-item>
          <el-form-item label="窗口状态">
            <el-input v-model="win"></el-input>
          </el-form-item>
          <el-form-item label="燃气状态">
            <el-input v-model="fire"></el-input>
          </el-form-item>
          <el-form-item label="是否有人闯入">
            <el-input v-model="per"></el-input>
          </el-form-item>
        </el-form>

      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "status",
  props: {
    temp: {
      type: String,
      default: '25,75%'
    },
    win: {
      type: String,
      default: '窗户运行正常'
    },
    fire: {
      type: String,
      default: '燃气状态完好'
    },
    per: {
      type: String,
      default: '无人闯入'
    },
  }
}
</script>

<style scoped>

</style>
