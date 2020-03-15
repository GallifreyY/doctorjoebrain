<template>
<div >
    <nav-bar></nav-bar>
    <device-table></device-table>
  </div>  
</template>

<script>
    import NavBar from "@/components/NavBar";
    import DeviceTable from "@/components/DeviceTable"
    export default {
        name: 'DeviceMatrix',
        components:{NavBar,DeviceTable},
        data() {
            return {
                
            }
        }
    }
</script>

<style lang="" scoped>

    
</style>