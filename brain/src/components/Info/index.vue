<template>
  <div class="container">
    <!--basic value-->
    <Row :gutter="16" style="background:inherit;" type="flex">
      <Col :sm="12" :lg="8">
        <div v-for="(dInfo,index) in deviceInfo">
          <!-- 暂缓之策 -->
          <a @click.stop="handleDeviceClick(index)">
            <device-card :deviceInfo="dInfo" :index = index :showDetails="deviveDetails[index]"></device-card>
          </a>
        </div>
      </Col>

      <Col :sm="12" :lg="16" class="col-tables">
        <!-- <div style="display:flex;flex-direction:column;justify-content:center"> -->
          <div style="margin:20px">
            <Card shadow>
              <p slot="title">Device Information</p>
              <Table
                stripe
                :show-header="showHeader"
                :columns="columns"
                :data="device_column_data"
                :size="tableSize"
              ></Table>
            </Card>
          </div>

          <div style="margin:20px">
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

          <div style="margin:20px">
            <Card shadow>
              <p slot="title">Diagnosis</p>
              <Row type="flex" justify="center">
                <Button type="primary" shape="circle" long @click="progress">Diagnosis</Button>
              </Row>
            </Card>
          </div>
        <!-- </div> -->
      </Col>
    </Row>

    <!--progress bar-->
    <Row style="padding:20px 0px">
      <Progress v-if="showProgressBar" :percent="percent" :status="progressStatus"></Progress>
    </Row>

    <!--client and agent value-->
    <Row v-if="showCheckingResult" :gutter="16" style="padding:20px 0px;">
      <Col span="12">
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
      </Col>
      <Col span="12">
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
      </Col>
    </Row>

    <!--suggestion-->
    <Row v-if="showCheckingResult" style="padding:20px 0px;">
      <Card shawdow>
        <p slot="title">Suggesions</p>
        <List size="small">
          <ListItem v-for="suggestion in compatilityCheck.suggestions" :key="suggestion">
            <ListItemMeta :title="suggestion" />
            <template slot="action">
              <li>
                <Button type="success" size="small">Effect</Button>
              </li>
              <li>
                <Button type="error" size="small">No Effect</Button>
              </li>
            </template>
          </ListItem>
        </List>
      </Card>
    </Row>

    <!--reference video-->
    <Row v-if="showCheckingResult" style="padding:20px 0px">
      <Card>
        <p slot="title">Referece Video</p>
        <video
          controls
          :src="'/static/diagnosis/'+ compatilityCheck.referenceVideo"
          type="video/mp4"
        ></video>
      </Card>
    </Row>
  </div>
</template>

<script>
const df = require("./default/");
import { getBasicInfo, getDiagnosisInfo } from "@/api/diagnosis";
import DeviceCard from "@/components/DeviceCard";
import { mapGetters } from "vuex";
export default {
  name: "Info",
  components: { DeviceCard },
  data() {
    return {
      //Data
      // deviceInfo: df.deviceInfo,
      // clientInfo: df.clientInfo,
      deviceInfo: undefined,
      clientInfo: undefined,
      compatilityCheck: undefined,
      index: 0,
      numOfDevices: 0,
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
      showCheckingResult: false,
      tableSize: "small",
      percent: 0,
      progressStatus: "active"
    };
  },

  methods: {
    initProgress() {
      this.percent = 0;
    },
    progress() {
      this.initProgress();
      this.showProgressBar = true;
      //暂时先这么写着 后续会根据数据是否到达设置进条
      if (this.percent == 0) {
        return new Promise((resolve, reject) => {
          let interval = setInterval(() => {
            this.percent = this.percent + 10;
            if (this.percent === 100) {
              clearInterval(interval);
              resolve(true);
            }
          }, 200);
        }).then(() => {
          this.fetchDiagnosisInfo(this.uuid, this.index);
        });
      }
    },
    handleDeviceClick(index) {
      this.index = index;
    },
    fetchBasicInfo(uuid) {
      getBasicInfo(uuid)
        .then(response => {
          this.deviceInfo = response.data.device; //array
          this.clientInfo = response.data.client;
          this.numOfDevices = this.deviceInfo.length;

          // todo： 查询目录里是否有图片 没有的话用default图片代替
          // if(this.deviceInfo.pic == null){this.deviceInfo.pic = "devices.jpg"}
          // if(this.deviceInfo.logo == null){this.deviceInfo.logo = "vendor.png"}

          this.$Message.success("Successfully get your device information..");
        })
        .catch(() => {
          this.$Message.error(
            "Sorry, could not get your device information..Please diagnosis again"
          );
        });
    },

    fetchDiagnosisInfo(uuid, index) {
      getDiagnosisInfo(uuid, index)
        .then(response => {
          this.compatilityCheck = response.data;
          this.progressStatus = "success";
          this.showCheckingResult = true;
          this.$Message.success(
            "Successfully get your diagnosis information.."
          );
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
  computed: {
    ...mapGetters(["uuid"]),
    deviveDetails: {
      get: function() {
        let res = Array(this.numOfDevices).fill(false);
        res[this.index] = true;
        return res;
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
          { key: "PID", value: this.deviceInfo[this.index].pid }
        ];
      }
    }
  },
  created() {
    this.$store.commit("uuid/SET_UUID", this.$route.params.id);
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
  justify-content: center;
}
</style>
