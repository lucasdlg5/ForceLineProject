Vue.use(VueMaterial.default)

        new Vue({
            el: '#app',
            data: {              
                    
                    nome: "",
                    desc: "",
                    teste: [],
                    count: 0
                
            },
            methods: {
                pegarElemento() {
                    document.getElementById("outer-modal").style.display = "block"                    
                },
                cancelarElemento(){
                    document.getElementById("outer-modal").style.display = "none"                    
                },
                increment(){
                    this.counter();
                    this.teste.push({
                        'id': this.count,
                        'nome': this.nome,
                        'desc': this.desc
                    })                    
                },
                counter(){
                    this.count ++;
                },
                removerRegistro(e){
                    var index = this.teste.indexOf(e);
                    this.teste.splice(index,1);
                }
                
            }
        })