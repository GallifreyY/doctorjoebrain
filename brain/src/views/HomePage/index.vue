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

export default {
  name: "HomePage",
  components: {
    TopBar,
    Info,
    RearBar
  }
  // 数据入口
};
</script>

<style>
</style>