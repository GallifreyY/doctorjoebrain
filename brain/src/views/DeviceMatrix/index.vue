<template>
<div class="page">
    <nav-bar></nav-bar>
    <!-- <device-table></device-table> -->
    <Matrix></Matrix>
  </div>  
</template>

<script>
    import NavBar from "@/components/NavBar";
    import DeviceTable from "@/components/DeviceTable"
    import Matrix from  "@/components/Matrix"
    export default {
        name: 'DeviceMatrix',
        components:{NavBar,DeviceTable,Matrix},
        data() {
            return {
                
            }
        }
    }
</script>

<style lang="" scoped>

    
</style>