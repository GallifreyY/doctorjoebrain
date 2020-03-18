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
                    console.log('working');
                })
            } 
        },
        created(){
            this.fetchData();
        }
    }
</script>

<style lang="" scoped>
    
</style>