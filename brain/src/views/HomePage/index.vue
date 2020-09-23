<template>
  <div class="home-page">
    <nav-bar></nav-bar>
    <banner></banner>
     <description-contents></description-contents>
    <logo-contents style="margin-top: 40px;padding-bottom: 20px"></logo-contents>
<!--    <Divider style="height: 2px;margin-top: 100px;background-color:#DCDCDC"/>-->



  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import HomeIntro from "@/components/HomeIntro";
import DownloadButton from "@/components/DownloadButton"
import Banner from "@/components/Banner"
import LogoContents from "@/components/LogoContents"
import DescriptionContents from "@/components/DescriptionContents"

export default {
  name: "HomePage",
  components: {
    NavBar,
    HomeIntro,
    DownloadButton,
    Banner,
    LogoContents,
    DescriptionContents
  },
  data() {
    return {};
  }
};
</script>

<style scoped>

.home-page {
  background-image: url(../../assets/background.jpeg);
  /*background-color:#F5F5F5;*/
  background-size: 100%;
  background-repeat: repeat-y;
  /*height:100vh;*/
  margin-left: 15px;
  margin-right: 15px;
  z-index:0;
}

</style>
