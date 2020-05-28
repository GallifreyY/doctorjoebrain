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
        <home-intro></home-intro>
        <home-intro></home-intro>
        <home-intro></home-intro>
        <home-intro></home-intro>
      </div>
      <!-- <Button shape="circle" ghost size="large">Download</Button> -->
      <download-button ></download-button>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import HomeIntro from "@/components/HomeIntro";
import DownloadButton from "@/components/DownloadButton"

export default {
  name: "HomePage",
  components: {
    NavBar,
    HomeIntro,
    DownloadButton
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
  height:100vh;
  border: 1px solid red;
  z-index:0;
}
.titles {
  color: white;
  text-align: center;
  padding-bottom: 5rem;
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
  /* border: 2px solid white; */
  width: 80vw;
  /* height:30vh; */
  margin : auto;
  margin-top:0vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}
</style>