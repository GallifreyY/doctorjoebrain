<template>
  <div class="home-page">
    <nav-bar></nav-bar>
    <banner></banner>
    <logo-contents></logo-contents>
    <Divider style="height: 2px;margin-top: 100px;background-color:#DCDCDC"/>
    <description-contents></description-contents>
    <home-footer></home-footer>

  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import HomeIntro from "@/components/HomeIntro";
import DownloadButton from "@/components/DownloadButton"
import Banner from "@/components/Banner"
import LogoContents from "@/components/LogoContents"
import DescriptionContents from "@/components/DescriptionContents"
import HomeFooter from "@/components/HomeFooter"
export default {
  name: "HomePage",
  components: {
    NavBar,
    HomeIntro,
    DownloadButton,
    Banner,
    LogoContents,
    DescriptionContents,
    HomeFooter
  },
  data() {
    return {};
  }
};
</script>

<style scoped>

.home-page {
  /*background-image: url(../../assets/background.jpeg);*/
  background-color:#F5F5F5;
  background-size: 100%;
  background-repeat: no-repeat;
  /*height:100vh;*/
  margin: 15px;
  z-index:0;
}

</style>
