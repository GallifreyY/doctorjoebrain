<template>
  <div class="step">
    <nav-bar style="margin-left: 15px"></nav-bar>
   <guide-user-process></guide-user-process>
    </div>
</template>

<script>
  import NavBar from "@/components/NavBar";
  import GuideUserProcess from "../../components/GuideUserProcess/index";
    export default {
        name: 'userprocess',
      components:{GuideUserProcess, NavBar},
    }
</script>

<style scoped>

</style>
