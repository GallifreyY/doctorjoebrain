<template>
  <div class="options">
    <nav-bar style="margin-left: 15px"></nav-bar>
    <install-step-for-linux></install-step-for-linux>
    </div>
</template>

<script>
  import NavBar from "@/components/NavBar";
  import InstallStep from "../../components/InstallStep/index";
  import InstallStepForLinux from "../../components/InstallStepForLinux/index";

    export default {
        name: 'step',
      components:{InstallStepForLinux, NavBar},
    }
</script>

<style scoped>

</style>
