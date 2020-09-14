<template>
  <div class="step">
    <nav-bar></nav-bar>
    <guide-tips></guide-tips>
    </div>
</template>

<script>
  import NavBar from "@/components/NavBar";
  import GuideTips from "../../components/GuideTips/index";
    export default {
        name: 'tips',
      components:{GuideTips,NavBar},
    }
</script>

<style scoped>

</style>
