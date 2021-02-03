<template>
  <div class="score-circle" v-if="type===1">
    <i-circle :percent="rate" :size="250" stroke-color="#AFEEEE" :stroke-width="10" :trail-width="9">
<!--        <span class="demo-i-circle-inner" style="font-size:24px">-->
<!--          <Icon type="md-checkmark" size="100" style="color:#AFEEEE"></Icon></span>-->
      <span class="demo-i-circle-inner" style="font-size:75px">{{rate}}</span>
    </i-circle>
    </div>
  <div class="score-circle" v-else-if="type===2">
    <i-circle :percent="rate" :size="250" stroke-color="#FFA500" :stroke-width="10" :trail-width="9">
<!--        <span class="demo-i-circle-inner" style="font-size:24px">-->
<!--          <Icon type="md-checkmark" size="100" style="color:#AFEEEE"></Icon></span>-->
      <span class="demo-i-circle-inner" style="font-size:75px">{{rate}}</span>
    </i-circle>
    </div>
  <div class="score-circle" v-else>
    <i-circle :percent="rate" :size="250" stroke-color="#FF0000" :stroke-width="10" :trail-width="9">
<!--        <span class="demo-i-circle-inner" style="font-size:24px">-->
<!--          <Icon type="md-checkmark" size="100" style="color:#AFEEEE"></Icon></span>-->
      <span class="demo-i-circle-inner" style="font-size:75px">{{rate}}</span>
    </i-circle>
    </div>
</template>

<script>
import { getBasicInfo} from "@/api/diagnosis";
 import {mapGetters} from "vuex";
    export default {
        name: "ScoreCircle",
       data() {
    return {
      errorLen:undefined,
      warningLen:undefined,
      suggestionLen:undefined,
      rate:undefined,
      type:undefined
    };
  },

  methods: {
    fetchDiagnoseInfo(uuid) {
      getBasicInfo(uuid)
        .then(response => {
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
          this.rate = parseInt((suggestionLen/(errorLen*10+warningLen*5+suggestionLen))*100);
          if(this.rate<0){
            this.rate=0
          }
          if (this.rate > 79){
            this.type=1
          }else if (this.rate<80 && this.rate>59){
            this.type=2
          }else{
            this.type=3
          }
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

