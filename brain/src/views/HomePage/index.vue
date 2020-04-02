<template>
  <div>
    <top-bar></top-bar>
    <Info></Info>
    <rear-bar></rear-bar>
  </div>
</template>

<script>
import TopBar from "@/components/TopBar";
import Info from "@/components/Info";
import RearBar from "@/components/RearBar";
// import { mapGetters } from "vuex";

export default {
  name: "HomePage",
  components: {
    TopBar,
    Info,
    RearBar
  },
  // computed: {
  //   ...mapGetters(["uuid"])
  // },
  // methods:{
  //   identify(){
  //     this.$store.dispatch("uuid/identify",this.$route.params.id) 
  //   }
  // },
  // created(){
  //   console.log(this.$route.params.id)

  // }
  // 数据入口
};
</script>
<style>
</style>