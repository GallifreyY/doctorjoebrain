<template>
<div class="page">
    <nav-bar></nav-bar>
    <!-- <device-table></device-table> -->
    <Matrix></Matrix>
  </div>  
</template>

<script>
    import NavBar from "@/components/NavBar";
    import Matrix from  "@/components/Matrix"
    export default {
        name: 'DeviceMatrix',
        components:{NavBar,Matrix},
        data() {
            return {
                
            }
        }
    }
</script>

<style lang="" scoped>

    
</style>