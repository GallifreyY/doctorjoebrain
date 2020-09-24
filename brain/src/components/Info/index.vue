<template>
  <div class="container">
    <!--basic value-->
    <Row type="flex">
      <Col :sm="12" :lg="8">
        <!-- Device display -->
        <device-display :deviceInfo="deviceInfo" :labelDict="labelDict" :index.sync="index"></device-display>
      </Col>

      <Col :sm="12" :lg="16" class="col-tables">
        <div style="margin:10px 0px">
          <Card shadow>
            <p slot="title">Device Information</p>
            <span slot="extra" style=" font-weight:400">
              <Tag
                color="success"
                type="border"
                size="default"
              >Detected in {{deviceInfo[index].end.replace(/^\S/,s =>s.toUpperCase())}}</Tag>
              <Tag
                v-if="deviceInfo[index].tag.isVirtualPrinter"
                color="warning"
                type="border"
              >Virtual Printer</Tag>
              <Tag
                v-else-if="deviceInfo[index].tag.isPresent"
                color="success"
                type="border"
              >Connected</Tag>
              <Tag v-else color="error" type="border">Disconnected</Tag>
              <Tag v-if="deviceInfo[index].hasProblem" color="error" type="border">Has problem</Tag>
              <Tag
                v-if="deviceInfo[index].tag.isRebootNeed"
                color="warning"
                type="border"
              >Reboot Need</Tag>
              <Tag
                v-if="deviceInfo[index].tag.isUsbRedirect"
                color="warning"
                type="border"
              >Usb Redirected</Tag>
            </span>
            <Table
              stripe
              :show-header="showHeader"
              :columns="columns"
              :data="device_column_data"
              :size="tableSize"
            ></Table>
          </Card>
        </div>

        <div style="margin: 10px 0px">
          <Card shadow>
            <p slot="title">Client Information</p>
            <span slot="extra">
              <Poptip trigger="hover" placement="left" width="750">
                <a>More Information</a>
                <!-- <div slot="title">Detail Information about the Client</div> -->
                <div slot="content" style="height: 500px;overflow:scroll">
                  <Table
                    stripe
                    :show-header="showHeader"
                    :columns="columns"
                    :data="clientDetail"
                    :size="tableSize"
                  ></Table>
                </div>
              </Poptip>
            </span>
            <Table
              stripe
              :show-header="showHeader"
              :columns="columns"
              :data="clientInfo"
              :size="tableSize"
            ></Table>
          </Card>
        </div>

        <div style="margin: 10px 0px">
          <Card shadow>
            <p slot="title">Agent Information</p>
            <Table
              stripe
              :show-header="showHeader"
              :columns="columns"
              :data="agentInfo"
              :size="tableSize"
            ></Table>
          </Card>
        </div>
      </Col>
    </Row>

    <!--progress bar-->
    <!-- <Row style="padding:20px 0px">
      <Progress v-if="showProgressBar" :percent="percent" :status="progressStatus"></Progress>
    </Row>-->

    <!--client and agent value-->
    <Row style="margin:20px 0px">
      <Col span="12">
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

      <Col span="12">
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

    <!--suggestion-->
    <Row style="margin:20px 0px;">
      <Card shawdow>
        <p slot="title">Suggestions</p>
        <List size="small">
          <ListItem v-for="suggestion in suggestions" :key="suggestion">
            <!-- <ListItemMeta :title="suggestion.context" /> -->
            <div>
              <Icon type="ios-alert-outline" color="red" />
              <span class="suggestions">{{suggestion.context}}</span>
              <span class="suggestions" v-if="suggestion.hasDetail">
                Follow
                <a :href="suggestion.detail">
                  this link
                  <Icon type="ios-search" size="16" />
                </a>
                to find more guidance.
              </span>
            </div>
          </ListItem>
        </List>
      </Card>
    </Row>

    <!--reference video-->
    <!-- <Row  style="padding:20px 0px">
      <Card>
        <p slot="title">Reference Video</p>
        <video
          controls
          :src="'/static/diagnosis/'+ compatibilityCheck.referenceVideo"
          type="video/mp4"
        ></video>
      </Card>
    </Row>-->
  </div>
</template>

<script>
import { getBasicInfo, getDiagnosisInfo } from "@/api/diagnosis";
import DeviceDisplay from "@/components/DeviceDisplay";
import DeviceCard from "@/components/DeviceCard";
import { mapGetters } from "vuex";
export default {
  name: "Info",
  components: { DeviceDisplay, DeviceCard },
  data() {
    return {
      deviceInfo: undefined,
      clientInfo: undefined,
      agentInfo: undefined,
      clientDetail: undefined,
      index: 0,
      numOfDevices: 0,
      diagnosisInfo: undefined,
      //suggestions: undefined,
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
          this.$Message.success("Successfully get the report of this device");
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






<style scoped>
.container {
  padding: 30px 60px;
  background-color: #eee;
  /* font-family: 'Open Sans', serif; */
  font-weight: 700;
}

img {
  width: 100%;
}

.name-and-link {
  text-align: center;
  font-weight: 600;
  font-size: 1.25rem;
}

.col-tables {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
</style>
