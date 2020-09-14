<template>
  <div class="options">
    <nav-bar></nav-bar>
    <guide-options></guide-options>
    </div>
</template>

<script>
  import NavBar from "@/components/NavBar";
  import GuideOptions from "../../components/GuideOptions/index";
    export default {
        name: 'step',
      components:{GuideOptions, NavBar},
    }
</script>

<style scoped>

</style>
