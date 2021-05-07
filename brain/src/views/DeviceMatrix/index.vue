<template>
<div class="page">
    <nav-bar style="margin-left: 15px"06></nav-bar>
  <iframe id="iframeId" src="https://marketplace.cloud.vmware.com/vmware-validated-peripherals" frameborder="0" class="pc iframe"  scrolling="auto"></iframe>
    <!-- <device-table></device-table> -->
<!--    <Matrix></Matrix>-->
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
.iframe {
    position: absolute;
    left: 15px;
    right: 10px;
    top: 0;
    bottom: 0;
    width: 99%;
    height: 100%;
    background: #fff;
    overflow-y: hidden;
    overflow-x: hidden;
}
</style>
