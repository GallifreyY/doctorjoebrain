<template>
    <div>
        <p>Test</p>
        <p>{{matrix}}</p>
    </div>
</template>

<script>
    import {fetchMatrix} from '@/api/matrix'
    export default {
        name: 'Test',
        data() {
            return {
                matrix : 'cannot get from server'
            }
        },
        methods:{
            fetchData(){
                fetchMatrix().then(response =>{
                    this.matrix = response.data;
                    //console.log('working');
                })
            } ,
            trydebug(){
                for(let i = 5;i<10;i++){
                    debugger
                    let j = i+3
                    debugger
                }

            }
        },
        created(){
            //this.fetchData();
            // console.log(process.env.NODE_ENV);
            // console.log(_TRY_);
            // console.log(process.env.PORT)
            this.trydebug();

        }
    }
</script>

<style lang="" scoped>
    
</style>