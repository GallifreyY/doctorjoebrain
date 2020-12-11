<template>
    <Tabs>
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
      methods: {
    }

    };
</script>
