<template>
  <div class="step">
    <nav-bar style="margin-left: 15px"></nav-bar>
    <guide-step></guide-step>
    </div>
</template>

<script>
  import NavBar from "@/components/NavBar";
  import GuideStep from "../../components/GuideStep/index";
    export default {
        name: 'step',
      components:{GuideStep, NavBar},
    }
</script>

<style scoped>

</style>
