<template>
<div class="page">
    <nav-bar style="margin-left: 15px"></nav-bar>
  <iframe sandbox="allow-forms allow-same-origin allow-scripts" id="iframeId" src="https://marketplace.cloud.vmware.com/vmware-validated-peripherals" frameborder="0" class="pc iframe"  scrolling="auto"></iframe>
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
        },
        methods:{
          securityProtection(){
            if(window != window.top){
                window.top.location.href = "https://marketplace.cloud.vmware.com/vmware-validated-peripherals";
            }
            if (top.location.host != window.location.host) {
　　              top.location.href = window.location.href;
              }
          }
        },
        created(){
    this.securityProtection()


  }
    }
</script>

<style lang="" scoped>
.iframe {
    position: fixed;
    left: 15px;
    right: 10px;
    top: 67px;
    bottom: 0;
    width: 97.6%;
    height: 100%;
    background: #fff;
    overflow-y: hidden;
    overflow-x: hidden;
}
</style>
