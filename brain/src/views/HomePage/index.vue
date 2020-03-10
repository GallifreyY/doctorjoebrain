<template>
  <div>
    <top-bar></top-bar>
    <Info></Info>
  </div>
</template>

<script>
import TopBar from "@/components/TopBar";
import Info from "@/components/Info";

export default {
  name: "HomePage",
  components: {
    TopBar,
    Info
  }
  // 数据入口
};
</script>

<style>
</style>