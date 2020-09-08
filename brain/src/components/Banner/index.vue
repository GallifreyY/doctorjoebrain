<template>
  <div class="banner">
    <nav-bar></nav-bar>
    <div class="content">
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
  name: "Banner",
  components: {NavBar},
  data() {
    return {
      title: "Horizon Peripherals Intelligence",
      subtitle:
        "Online self diagnosis for Peripheral devices usages in Horizon environment."
    };
  }
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.banner {
  background-image: url(../../assets/background.jpeg);
  height: 300px;
  background-size:100% 100%;
  opacity:1;
  background-repeat:no-repeat;
}

.titles {
  color: white;
  text-align: center;
  padding-bottom: 9rem;
  /*margin-left: -700px;*/
  padding-top: 9rem;
}


.title {
  font-size: 2.5rem;
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

