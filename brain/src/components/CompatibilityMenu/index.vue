<template>
  <div class="compat-menu">
<!--    <Sider id="sider" style="overflow:scroll">-->
<!--    <Menu theme="light" active-name="1">-->
<!--       <Submenu name="1">-->
<!--          <Icon type="ios-arrow-forward"></Icon>-->
<!--         Client Compatibility Check-->
<!--          </Submenu>-->
<!--       <Submenu name="2">-->
<!--          <Icon type="ios-arrow-forward"></Icon>-->
<!--         Agent Compatibility Check-->
<!--          </Submenu>-->
<!--    </Menu>-->
<!--      </Sider>-->
    <div class="compatibilitycontent">
  <Row>
    <Col span="24">
        <div style="margin:0px 10px 0px 0px">
          <Card shadow>
            <p slot="title">Client Compatibility Check</p>
            <Table
              stripe
              :show-header="showHeader"
              :columns="checkColumns"
              :data="compatilityCheck.client"
              :size="tableSize"
            ></Table>
          </Card>
        </div>
      </Col>
    </Row>
  <Row>
    <Col span="24">
        <div style="margin:0px 0px 0px 10px ">
          <Card shadow>
            <p slot="title">Agent Compatibility Check</p>
            <Table
              stripe
              :show-header="showHeader"
              :columns="checkColumns"
              :data="compatilityCheck.agent"
              :size="tableSize"
            ></Table>
          </Card>
        </div>
      </Col>
    </Row>
    </div>
    <br>
    </div>
</template>
<script>
 import { getBasicInfo} from "@/api/diagnosis";
 import {mapGetters} from "vuex";
    export default {
  name: "CompatibilityMenu",
  components: { },
  data() {
    return {
      deviceInfo: undefined,
      clientInfo: undefined,
      agentInfo: undefined,
      clientDetail: undefined,
      index: 0,
      numOfDevices: 0,
      diagnosisInfo: undefined,
      labelDict: {
        printers: "Printers",
        usbdisk: "USB Disk Devices",
        scanners: "Scanners",
        cameras: "Cameras"
      },
      //UI
      columns: [
        { title: "Key", key: "key" },
        { title: "Value", key: "value" }
      ],
      checkColumns: [
        { title: "Key", key: "key" },
        { title: "Value", key: "value" },
        {
          title: "Check",
          key: "check",
          width: 100,
          render: (h, params) => {
            let _string = "Pass";
            let _color = "success";
            if (params.row.check == false) {
              _string = "Failed";
              _color = "error";
            }
            else if(params.row.check == 'null'){
              _string = "";
              _color = "white";
            }
            return h(
              "Tag",
              {
                props: { color: _color, size: "small", type: "border" }
              },
              _string
            );
          }
        }
      ],
      showHeader: false, //tableHeader
      showProgressBar: false,
      tableSize: "big"
    };
  },

  methods: {
    parseSuggestions(suggestions) {
      let res = [];
      suggestions.forEach(item => {
        let suggestion = {};
        if (item instanceof Array) {
          suggestion["context"] = item[0];
          suggestion["hasDetail"] = true;
          suggestion["detail"] = item[1];
        } else {
          suggestion["context"] = item;
          suggestion["hasDetail"] = false;
        }
        res.push(suggestion);
      });
      return res;
    },

    fetchBasicInfo(uuid) {
      getBasicInfo(uuid)
        .then(response => {
          this.deviceInfo = response.data.basicInfo.device; //array
          this.clientInfo = response.data.basicInfo.client;
          this.agentInfo = response.data.basicInfo.agent;
          this.clientDetail = response.data.basicInfo.clientDetail;
          this.numOfDevices = this.deviceInfo.length;
          this.diagnosisInfo = response.data.diagnosisInfo;
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
  watch: {
    index: function() {
      this.$Message.success("Updated the diagnosis report for the device");
    }
  },

  computed: {
    ...mapGetters(["uuid"]),
    compatilityCheck: {
      get: function() {
        return typeof this.diagnosisInfo == "undefined"
          ? undefined
          : this.diagnosisInfo[this.index].checkResult;
      }
    },
    suggestions: {
      get: function() {
        return typeof this.diagnosisInfo == "undefined"
          ? undefined
          : this.parseSuggestions(this.diagnosisInfo[this.index].suggestions);
      }
    },
    device_column_data: {
      get: function() {
        return [
          {
            key: "Device Name",
            value: this.deviceInfo[this.index].deviceName
          },
          { key: "VID", value: this.deviceInfo[this.index].vid },
          { key: "PID", value: this.deviceInfo[this.index].pid },
          {
            key: "Device Type",
            value: this.labelDict[this.deviceInfo[this.index].type]
          }
        ];
      }
    }
  },
  created() {
    this.$store.commit("uuid/SET_UUID", this.$route.params.id);
    this.$Loading.start();
    this.fetchBasicInfo(this.uuid);
  }
};
</script>
<style>
  #sider {
  position: fixed;
  height: 90vh;
  width: 35vw;
  left: 0;
  /* overflow: auto; */
  background: #fff;
  z-index: 25;
}

</style>
