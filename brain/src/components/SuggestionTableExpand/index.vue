<style scoped>
    .expand-row{
        margin-bottom: 16px;
    }
</style>
<template>
    <div>
        <Row class="suexpand-row">
           <Col span="24" v-if="(row.errorType===1) || (row.errorType===11)">
                <div v-for="(item,i) in row.errorInfo">
              <Icon type="ios-alert-outline" color="red" />
              <span class="suggestions">{{row.errorInfo[i].context}}</span>
              <span class="suggestions" v-if="row.errorInfo[i].hasDetail">
                Follow
                <a :href="row.errorInfo[i].detail">
                  this link
                  <Icon type="ios-search" size="16" />
                </a>
                to find more guidance.
              </span>
                 </div>
        </Col>
       <Col span="24" v-else-if="(row.errorType===0) || (row.errorType===10)">
                <div v-for="(item,i) in row.warningInfo">
              <Icon type="ios-alert-outline" color="#FFA500" />
              <span class="suggestions">{{row.warningInfo[i].context}}</span>
              <span class="suggestions" v-if="row.warningInfo[i].hasDetail">
                Follow
                <a :href="row.warningInfo[i].detail">
                  this link
                  <Icon type="ios-search" size="16" />
                </a>
                to find more guidance.
              </span>
                 </div>
              </Col>

          <Col span="24" v-else-if="(row.errorType===2) || (row.errorType===21)">
                <div v-for="(item,i) in row.errorInfo">
              <Icon type="ios-alert-outline" color="red" />
              <span class="suggestions">{{row.errorInfo[i].context}}</span>
              <span class="suggestions" v-if="row.errorInfo[i].hasDetail">
                Follow
                <a :href="row.errorInfo[i].detail">
                  this link
                  <Icon type="ios-search" size="16" />
                </a>
                to find more guidance.
              </span>
                 </div>
             <div v-for="(item,i) in row.warningInfo">
              <Icon type="ios-alert-outline" color="#FFA500" />
              <span class="suggestions">{{row.warningInfo[i].context}}</span>
              <span class="suggestions" v-if="row.warningInfo[i].hasDetail">
                Follow
                <a :href="row.warningInfo[i].detail">
                  this link
                  <Icon type="ios-search" size="16" />
                </a>
                to find more guidance.
              </span>
                 </div>
              </Col>



        </Row>
    </div>
</template>
<script>
    export default {
      name: "SuggestionTableExpand",
        props: {
            row: Object,
            index: Object
        }
    };
</script>
