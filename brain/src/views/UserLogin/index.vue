<template>
  <div class="step">
    <nav-bar style="margin-left: 15px"></nav-bar>
    <guide-user-login></guide-user-login>
    </div>
</template>

<script>
  import NavBar from "@/components/NavBar";
  import GuideUserLogin from "../../components/GuideUserLogin/index";
    export default {
        name: 'userlogin',
      components:{GuideUserLogin, NavBar},
    }
</script>

<style scoped>

</style>
