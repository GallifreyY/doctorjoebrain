<template>
    <Tabs v-if="isLanguage==='zh-CN'">
        <TabPane label="设备信息" icon="ios-briefcase">
          <report-menu style="height: 500px;overflow: scroll"></report-menu>
        </TabPane>
      <TabPane label="兼容性信息" icon="ios-analytics"><compatibility-menu  style="height: 500px;overflow: scroll"></compatibility-menu></TabPane>
        <TabPane label="更多信息" icon="ios-desktop"><more-info-menu></more-info-menu></TabPane>
    </Tabs>
  <Tabs v-else-if="isLanguage==='zh-TW'">
    <TabPane label="設備信息" icon="ios-briefcase">
          <report-menu style="height: 500px;overflow: scroll"></report-menu>
        </TabPane>
      <TabPane label="兼容性信息" icon="ios-analytics"><compatibility-menu  style="height: 500px;overflow: scroll"></compatibility-menu></TabPane>
        <TabPane label="更多信息" icon="ios-desktop"><more-info-menu></more-info-menu></TabPane>
    </Tabs>
<Tabs v-else>
    <TabPane label="Device Infomation" icon="ios-briefcase">
          <report-menu style="height: 500px;overflow: scroll"></report-menu>
        </TabPane>
      <TabPane label="Compatibility Infomation" icon="ios-analytics"><compatibility-menu  style="height: 500px;overflow: scroll"></compatibility-menu></TabPane>
        <TabPane label="More Infomation" icon="ios-desktop"><more-info-menu></more-info-menu></TabPane>
    </Tabs>
</template>
<script>
    import ReportMenu from "../ReportMenu/index";
    import CompatibilityMenu from "../CompatibilityMenu/index";
    import MoreInfoMenu from "../MoreInfoMenu/index";
    export default {
        name: "ReportTabs",
      components: {MoreInfoMenu, CompatibilityMenu, ReportMenu},
       data(){
    return {
      isLanguage:undefined
    }
  },
      methods: {
          initLanguage(){
            if (navigator.language==='zh-CN'){
              this.isLanguage='zh-CN';
            }else if(navigator.language==='zh-TW'){
              this.isLanguage='zh-TW';
            }else{
               this.isLanguage='en';
            }

          }

    },
      created() {
          this.initLanguage();
      }

    };
</script>
