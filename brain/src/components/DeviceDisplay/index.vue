<template>
  <div>
    <div style="margin:20px 20px 20px 0px">
      <Card :bordered="false" shadow id="selector">
        <div class="title">Which device you want to diagnose?</div>
        <Cascader placeholder="Please select a device" :data="cascaderData" v-model="selectedData"></Cascader>
      </Card>
    </div>
  <device-card :deviceInfo="deviceInfo[index]" :index="index" :showDetails="true"></device-card>
</div>
</template>

<script>
import DeviceCard from "@/components/DeviceCard";
export default {
  name: "DeviceDisplay",
  components: { DeviceCard },
  props: {
    deviceInfo: {
      type: Array
    },
    labelDict: {
      type: Object
    },
    index: {
      type: Number
    },
    showCheckingResult:{
      type: Boolean
    },
    showProgressBar:{
      type:Boolean
    }
  },
  data() {
    return {
      sortedTag: undefined,
      cascaderData: undefined,
      selectedData: [" ", 0],
    };
  },
  methods: {
    parseDeviceInfo(devices) {
      let res = {};
      devices.forEach((ele, index, _) => {
        if (!(ele.type in res)) {
          res[ele.type] = [];
        }
        let tagStyle = (ele.hasProblem || (ele.tag.isPresent == false)) === true ? "error" : "success";

        res[ele.type].push({
          name: ele.deviceName,
          index: index,
          tagStyle: tagStyle
        });
      });
      return res;
    },
    parseTypeName(name) {
      return this.labelDict[name];
    },
    parseCascaderData(data) {
      let res = [];
      for (let devices in data) {
        let deviceType = {
          value: devices,
          label: this.labelDict[devices] || "Others",
          children: []
        };
        console.log(data[devices]);
        data[devices].forEach((device, index) => {
          deviceType.children.push({
            value: device.index,
            label: device.name
          });
        });
        res.push(deviceType);
      }
      return res;
    }
  },
  computed: {
    index: {
      get: function() {
        let index = this.selectedData[1];
        this.$emit("update:index", index); //父组件传递数据
        this.$emit("update:showCheckingResult", false)
        this.$emit("update:showProgressBar", false)
        return index;
      }
    }
  },
  created() {
    this.sortedTag = this.parseDeviceInfo(this.deviceInfo);
    this.cascaderData = this.parseCascaderData(this.sortedTag);
  }
};
</script>

<style lang="" scoped>
#selector {
  font-size: 14px;
  font-weight: 500;
  color: #17233d;
}
.title {
  margin-bottom:  3%;
}
</style>
