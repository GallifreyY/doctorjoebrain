<template>
  <div class="help" >
    <nav-bar style="margin-left: 15px"></nav-bar>
    <guide-content></guide-content>
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

</style>
