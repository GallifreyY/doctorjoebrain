<template>
  <div class="topBar">
    <nav-bar></nav-bar>
    <div class="topcontent">
      <div class="titles">
        <h1 class="title">{{title}}</h1>
        <h2 class="subtitle">{{subtitle}}</h2>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";

export default {
  name: "TopBar",
  components: {NavBar},
  data() {
    return {
     title: "Horizon Peripherals Intelligence",
      subtitle:
        "Device Intelligence Diagnosis Service for VMware Horizon."
    };
  }
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.topBar {
  background-image: url(../../assets/background.jpeg);
   background-size: 100%;
  background-repeat:no-repeat;
}

.titles {
  color: white;
  text-align: center;
  padding-bottom: 9rem;
  padding-top: 9rem;
}


.title {
  font-size: 2rem;
  font-weight: 600;
  line-height: 1.125;
  margin-bottom: 1.5rem;
}
.subtitle {
  font-size: 1.25rem;
  font-weight: 400;
  line-height: 1.25;
}
</style>

