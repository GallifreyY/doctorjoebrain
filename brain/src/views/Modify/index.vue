<template>
  <div class="modify">
    <nav-bar style="margin-left: 15px"></nav-bar>
    <modify-form style="position: absolute;top: 200px;left: 0;right: 0;bottom: 0;margin: auto;width: 400px;"></modify-form>

  </div>
</template>

<script>
  import ModifyForm from "@/components/ModifyForm";
  import NavBar from "@/components/NavBar";
  import RearBar from "@/components/RearBar"
  export default {
    name: 'Modify',
    components: {ModifyForm, NavBar, RearBar},
    data() {
      return {}
    }
  }
</script>


<style lang="" scoped>

  .modify {
    height: 100vh;

    background: url(../../assets/background.jpeg);
    position: relative;
    /*display: flex;*/
    /*align-items: center;*/
    /*justify-content: center;*/

  }

</style>
