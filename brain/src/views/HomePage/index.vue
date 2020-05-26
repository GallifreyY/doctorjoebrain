<template>
  <div class="home-page">
    <nav-bar></nav-bar>
    <div class="content">
      <div class="titles">
        <h1 class="title">Peripheral devices Cloud Doctor</h1>
        <h2
          class="subtitle"
        >Test:Online self diagnosis for Peripheral devices usages in Horizon environment</h2>
      </div>
      <div class="home-icons">
        <h1
          class="title"
        >home page here. Put 4 icons and according description:printer, usb disk, scanner and powermic, other..</h1>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";

export default {
  name: "HomePage",
  components: {
    NavBar
  },
  data() {
    return {};
  }
};
</script>

<style scoped>

.home-page {
  background-image: url(../../assets/background.jpeg);
  background-size: 100%;
  background-repeat: no-repeat;
  height:100%;
  border: 1px solid red;
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
.home-icons{
    /* padding:50%; */

}
</style>