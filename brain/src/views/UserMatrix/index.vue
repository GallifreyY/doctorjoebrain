<template>
  <div class="step">
    <nav-bar style="margin-left: 15px"></nav-bar>
   <guide-user-matrix></guide-user-matrix>
    </div>
</template>

<script>
  import NavBar from "@/components/NavBar";
  import GuideUserMatrix from "../../components/GuideUserMatrix/index";
    export default {
        name: 'usermatrix',
      components:{GuideUserMatrix,NavBar},
    }
</script>

<style scoped>

</style>
