<template>
  <div id="app">
    <router-view v-if="isRouterAlive"/>
  </div>
</template>

<script>
import {getLanguageInfo} from "@/api/diagnosis";
export default {
  name: 'App',
  provide(){
    return {
      reload:this.reload
    }

  },
  data(){
    return {
      isRouterAlive:true
    }
  },
  methods:{
    reload(){
      this.isRouterAlive = false
      this.$nextTick(function(){
        this.isRouterAlive = true;
      })
    },
    fetchLanguageInfo() {
      let language = navigator.language
      console.log(language)
      getLanguageInfo(language)
        .then(response => {
          console.log(response)
        })
        .catch(() => {
          this.$Loading.error();
          this.$Message.error(
            "Sorry, could not get your language information..."
          );
        });
    },
  },
  created() {
     this.fetchLanguageInfo();
  }
}
</script>

