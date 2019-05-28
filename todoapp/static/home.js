new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!'
  },
  methods: {
    pegarElemento(){
      document.getElementById("outer-modal").style.display="block"
      alert("ooooi")
    }
    
    }
})

