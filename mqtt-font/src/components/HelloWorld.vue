<template>
  <div class="hello">
    <div>
      <el-container>
        <el-header>
          <h2>物联网控制面板</h2>
        </el-header>
        <status :temp="temp" :per="per" :fire="fire" :win="win"></status>
        <el-footer>
          <el-button @click="showControl" type="primary" size="small">修改状态</el-button>
        </el-footer>
      </el-container>
    </div>

    <el-drawer
        :visible.sync="drawer"
        :direction="direction"

    >
      <control ></control>
    </el-drawer>

  </div>
</template>

<script>
import Status from "@/components/status";
import Control from "@/components/control";

export default {
  name: 'HelloWorld',
  components: {Control, Status},
  props: {
    msg: String
  },
  data() {
    return {
      server_message: '',
      drawer: false,
      direction: 'rtl',
      activeName: 'first',
      temp: '',
      win: '',
      fire: '',
      per: '',
      total: ['temp', 'win', 'fire', 'per']
    }
  },
  mounted() {
    this.getMainMessage()
    this.total_subscribe()
  },
  methods: {
    getMainMessage() {
      this.$axios.get('/').then(res => {
        console.log('get message form server')
        this.server_message = res.data
      })
    },
    handleClick(tab, event) {
      console.log(tab, event);
    },
    showControl() {
      this.drawer = !this.drawer
    },
    subscribe_mqtt(topic) {
      this.$socket.emit('subscribe', {
        topic: topic
      })
    },
    total_subscribe() {
      for (let i = 0; i < this.total.length; i++) {
        this.subscribe_mqtt(this.total[i])
        console.log('subscribe to {}', this.total[i])
      }
    }
  },
  sockets: {
    connect: (res) => {
      console.log('connect to message ,', res)
    },
    mqtt_message: (res) => {
      let topic = res.topic
      let message = res.payload
      console.log('get message form topic ',topic,'  ',message)
      switch (topic) {
        case 'temp':
          this.temp = message;
          break
        case 'per':
          this.per = message
          break
        case 'win':
          this.win = message
          break
        case 'fire':
          this.fire = message
          break
        default:
          console.log('topic not found ,', topic)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
