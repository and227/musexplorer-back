import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

const event = new Event('click')
document.querySelector('#groups').dispatchEvent(event)

// const now = new Date()
// document.querySelector('#leftStuff').innerHTML = `${now}`
// axios
//   .get(
//     'http://api.timezonedb.com/v2.1/get-time-zone?key=YOUR_API_KEY&format=json&by=zone&zone=America/Chicago'
//   )
//   .then((response) => {
//     console.log(response)
//   })

new Vue({
  render: (h) => h(App),
}).$mount('#app')
