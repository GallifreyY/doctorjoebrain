<template>
  <div class="container">
    <!--basic value-->
    <Row type="flex">
      <Col :sm="12" :lg="8">
        <!-- Device display -->
        <device-display :deviceInfo="deviceInfo" :labelDict="labelDict" :index.sync="index"></device-display>
      </Col>

      <Col :sm="12" :lg="16" class="col-tables">
        <!-- <div style="display:flex;flex-direction:column;justify-content:center"> -->

        <div style="margin:10px 0px">
          <Card shadow>
            <p slot="title">Device Information</p>
            <span slot="extra" style=" font-weight:400">
              <Tag
                color="success"
                type="border"
              >Detecting in {{deviceInfo[index].end.replace(/^\S/,s =>s.toUpperCase())}}</Tag>
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
              >Usb Redirect</Tag>
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
            <Table
              stripe
              :show-header="showHeader"
              :columns="columns"
              :data="clientInfo.client_column_data"
              :size="tableSize"
            ></Table>
          </Card>
        </div>

        <div style="margin: 10px 0px">
          <Card shadow>
            <p slot="title">Service Information</p>
          </Card>
        </div>

        <!-- <div style="margin:20px 0px">
          <Card shadow>
            <p slot="title">Diagnosis</p>
            <Row type="flex" justify="center">
              <Button
                type="primary"
                shape="circle"
                :loading="buttonLoading"
                long
                @click="progress"
              >Diagnosis</Button>
            </Row>
          </Card>
        </div>
        -->
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

            <!-- <template slot="action">
              <li v-if="suggestion.hasDetail">
                <a :href="suggestion.detail">
                  More Detail
                  <Icon type="ios-search" size="16"/>
                </a>
              </li>
    
            </template>-->
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
      deviceType: undefined,
      compatilityCheck: undefined,
      index: 0,
      numOfDevices: 0,
      suggestions: undefined,
      labelDict: {
        printers: "Printers",
        usbdisk: "USB Disk Devices"
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
      //showCheckingResult: false,
      tableSize: "small"
      //buttonLoading : false,
      //percent: 0,
      //progressStatus: "active"
    };
  },

  methods: {
    // initProgress() {
    //   this.percent = 0;
    //   this.showCheckingResult = false;
    //   this.buttonLoading = false;
    // },
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

    // progress() {
    //   this.initProgress();
    //   this.showProgressBar = true;
    //   this.buttonLoading = true;
    //   if (this.percent == 0) {
    //     return new Promise((resolve, reject) => {
    //       let interval = setInterval(() => {
    //         this.percent = this.percent + 10;
    //         if (this.percent === 100) {
    //           clearInterval(interval);
    //           resolve(true);
    //         }
    //       }, 200);
    //     }).then(() => {
    //       this.buttonLoading = false;
    //       this.fetchDiagnosisInfo(this.uuid, this.index);
    //     });
    //   }
    // },

    fetchBasicInfo(uuid) {
      getBasicInfo(uuid)
        .then(response => {
          this.deviceInfo = response.data.device; //array
          this.clientInfo = response.data.client;
          this.deviceType = response.data.device_type;
          this.numOfDevices = this.deviceInfo.length;

          // this.$Message.success("Successfully get your device information..");
        })
        .catch(() => {
          this.$Message.error(
            "Sorry, could not get your device information..."
          );
        });
    },

    fetchDiagnosisInfo(uuid, index) {
      getDiagnosisInfo(uuid, index)
        .then(response => {
          this.compatilityCheck = response.data;
          //this.parseSuggestions(this.compatilityCheck.suggestions);
          //console.log(this.compatilityCheck.suggestions)

          //todo : render suggestions
          this.suggestions = this.parseSuggestions(response.data.suggestions);
          this.progressStatus = "success";
          this.showCheckingResult = true;
          this.$Message.success("Successfully get the report of this device");
        })
        .catch(err => {
          this.progressStatus = "wrong";
          this.showCheckingResult = false;
          this.$Message.error(
            "Sorry, could not get the diagnosis information.."
          );
        });
    }
  },
  watch: {
    //update to watch index to get report

    
    index: {
      deep: true,
      handler(val) {
        this.fetchDiagnosisInfo(this.uuid, this.index);
      }
    },
    // device_column_data: {
    //   deep: true,
    //   handler(val) {
    //     console.log("change");
    //   }
    // }

  },
  computed: {
    ...mapGetters(["uuid"]),
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
          // { key: "Detecting in", value: this.deviceInfo[this.index].end }
        ];
      }
    }
  },
  created() {
    this.$store.commit("uuid/SET_UUID", this.$route.params.id);
    this.fetchBasicInfo(this.uuid);
    this.fetchDiagnosisInfo(this.uuid, this.index);
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
