import Vue from 'vue'
import 'lib-flexible'
import Vant from 'vant';
import 'vant/lib/index.css';
Vue.use(Vant);

import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

Vue.filter("ztb", function (v) {
  if (v == "") {
    return '--';
  }
  return Math.floor(v/10000000000000.0)/100.0
});

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
