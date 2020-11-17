<template>
  <div class="diagnose-info">
  <nav-bar style="margin-left: 15px"></nav-bar>
  <div>
    <Row>
        <Col span="8" style="margin-top: 80px;padding-left: 15px;padding-right: 5px;text-align: center">
          <score-circle style="margin-top: 20px"></score-circle>
          <div style="margin-top: 50px">
                <Button type="error">{{errorLen}}  Error</Button>
            <Button type="warning">{{warningLen}}  Warning</Button>
        <Button type="info">{{suggestionLen}} Suggestion</Button>
            </div>
        </Col>
        <Col span="16" style="margin-top: 80px;padding-right: 15px;">
          <div v-if="errorLen>0 || warningLen>0">
          <suggestion-table></suggestion-table>
            </div>
          <div v-else>
          <no-error-page></no-error-page>
          </div>
        </Col>
    </Row>
    </div>
    <div>
      <report-tabs style="padding-right: 15px;padding-left: 15px;margin-top: 80px"></report-tabs>
    </div>
    </div>
</template>

<script>
import ScoreCircle from "@/components/ScoreCircle";
import NavBar from "@/components/NavBar";
import SuggestionTable from "../SuggestionTable/index";
import ReportTabs from "../ReportTabs/index";
import { getBasicInfo} from "@/api/diagnosis";
 import {mapGetters} from "vuex";
import NoErrorPage from "../NoErrorPage/index";
export default {
    name: "DiagnoseInfo",
    components: {
      NoErrorPage,
      ReportTabs,
      ScoreCircle,
      SuggestionTable,
      NavBar

  },
   data() {
    return {
      errorLen:undefined,
      warningLen:undefined,
      suggestionLen:undefined,
      rate:undefined
    };
  },

  methods: {
    fetchDiagnoseInfo(uuid) {
      getBasicInfo(uuid)
        .then(response => {
          console.log("---")
          let errorLen = 0;
          let warningLen = 0;
          let suggestionLen = 0;
          let fetchInfoData = response.data.diagnosisTypeInfo;
          fetchInfoData.forEach(item => {
            errorLen += item.infoLen.errorLen;
            warningLen += item.infoLen.warningLen;
            suggestionLen += item.infoLen.suggestionLen;
          })
          this.errorLen = errorLen;
          this.warningLen = warningLen;
          this.suggestionLen = suggestionLen;
          this.rate = parseInt((suggestionLen/(errorLen+warningLen+suggestionLen))*100);
          this.$Loading.finish();
        })
        .catch(() => {
          this.$Loading.error();
          this.$Message.error(
            "Sorry, could not get your diagnosis information..."
          );
        });
    }
  },
  computed: {
    ...mapGetters(["uuid"]),
  },
  created() {
    this.$store.commit("uuid/SET_UUID", this.$route.params.id);
    this.$Loading.start();
    this.fetchDiagnoseInfo(this.uuid);
  }
};
</script>


<style scoped>

</style>
