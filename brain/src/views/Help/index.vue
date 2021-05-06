<template>
  <div class="help" style="overflow-y: hidden;overflow-x: hidden">
    <nav-bar style="margin-left: 15px"></nav-bar>
    <iframe id="iframeId" src="https://marketplace.cloud.vmware.com/vmware-validated-peripherals" frameborder="0" class="pc iframe"  scrolling="auto"></iframe>
<!--    <guide-content></guide-content>-->
    </div>
</template>

<script>
  import NavBar from "@/components/NavBar";
  import GuideContent from "../../components/GuideContent/index";
    export default {
        name: 'help',
      components:{GuideContent, NavBar},
    }
</script>

<style scoped>
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
