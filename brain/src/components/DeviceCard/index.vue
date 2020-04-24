<template>
  <div style="margin:20px">
    <Card :bordered="false" shadow>
      <!-- heading -->
      <Row type="flex" justify="space-between">
        <Col class="heading">{{deviceInfo.deviceName}} ({{index}})</Col>
        <Col >
          <Poptip v-if="deviceInfo.hasProblem" trigger="hover">
            <Icon type="ios-alert-outline" color="red" />
            <span slot="content" style="color:red;font-size:10px">This device has some problems</span>
          </Poptip>
          <Poptip v-else trigger="hover">
            <Icon type="ios-checkmark-circle-outline" color="green" />
            <span slot="content" style="color:green;font-size:10px">This device works normally</span>
          </Poptip>
        </Col>
      </Row>


      <!-- details -->
      <div v-show="showDetails">
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
    index: {
      type: Number,
      default: 0
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
.heading{
  font-size: 16px;
    color: #17233d;
    font-weight: 500;
    /* font-family: "Open Sans", serif; */
}

</style>