<template>
  <div style="margin:10px">
    <Card :bordered="false" shadow>
      <p slot="title">{{deviceInfo.deviceName}} ({{index}})</p>
      <div slot="extra">
        <Icon v-if="deviceInfo.hasProblem" type="ios-alert-outline" color="red" />
        <Icon v-else type="ios-checkmark-circle-outline" color="green" />
      </div>
      <div id="details" v-show="showDetails">
        <div>
          <img :src="'/static/device/'+ deviceInfo.details.picture" />
        </div>

        <Row type="flex" justify="center" align="middle" style="padding:10px 5px">
          <Col :span="6">
            <div style="width:70px; height:70px">
              <a :href="deviceInfo.details.vendor_link">
                <img :src="'/static/device/'+ deviceInfo.details.vendor_logo" alt="vendor" />
              </a>
            </div>
          </Col>
          <Col :span="18">
            <div style="padding:10px">
              <a :href="deviceInfo.details.vendor_link">Vendor: {{deviceInfo.details.vendor_name}}</a>
              <div class="description">
                <p>"{{deviceInfo.details.description}}"</p>
              </div>
            </div>
          </Col>
        </Row>
      </div>
    </Card>
  </div>
</template>

<script>
export default {
  name: "DeviceCard",
  props: {
    deviceInfo: {
      type: Object
    },
    showDetails: {
      type: Boolean,
      default: false
    },
    index:{
      type:Number,
      default:0
    }
  },
  data() {
    return {};
  }
};
</script>

<style lang="" scoped>
div img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
/* 溢出 不出框 */
div p {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: wrap;
}
.description {
  color: rgba(114, 112, 112, 0.938);
  font-family: "Open Sans", serif;
}
</style>