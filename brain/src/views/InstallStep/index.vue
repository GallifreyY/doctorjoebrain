<template>
  <div class="options">
    <nav-bar style="margin-left: 15px"></nav-bar>
    <install-step></install-step>
    </div>
</template>

<script>
  import NavBar from "@/components/NavBar";
  import InstallStep from "../../components/InstallStep/index";

    export default {
        name: 'step',
      components:{InstallStep, NavBar},
    }
</script>

<style scoped>

</style>
