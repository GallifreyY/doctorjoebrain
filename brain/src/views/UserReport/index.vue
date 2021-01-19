<template>
  <div>
    <diagnose-info></diagnose-info>
  </div>
</template>

<script>

import DiagnoseInfo from "../../components/DiagnoseInfo/index";
import {getLanguageInfo} from "@/api/diagnosis";

export default {
  name: "Report",
  components: {
    DiagnoseInfo


  },
  methods: {

  },
  created() {

  }
};
</script>
<style>
</style>
