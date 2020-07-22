<template>
  <div class="modify">
    <nav-bar></nav-bar>
    <modify-form></modify-form>



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
    display: flex;
    align-items: center;
    justify-content: center;

  }

</style>
