import Vue from 'vue'
import App from './App.vue'
import './plugin/element'
import axios from 'axios'
import VueSocketIO from 'vue-socket.io'

Vue.prototype.$axios = axios
// 临时使用
axios.defaults.baseURL = process.env.NODE_ENV !== 'production' ? '/api' : 'http://big.forcebing.top:8083';
Vue.config.productionTip = false
Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://big.forcebing.top:8083/test'
}))
Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')
