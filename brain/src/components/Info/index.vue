<template>
  <div class="container">
    <!--basic info-->
    <Row :gutter="16" style="background:inherit;" type="flex">
      <Col :sm="12" :lg="8">
        <Card :bordered="false" shadow>
          <img :src="'/static/'+ productPic" :alt="productName" />
          <Row type="flex" justify="center" align="middle">
            <Col :span="8">
              <img :src="'/static/'+ productLogo" />
            </Col>
            <Col :span="16">
              <div class="name-and-link">
                <p>{{productName}}</p>
                <a :href="productLink">{{productLink}}</a>
              </div>
            </Col>
          </Row>
          <Col class="content">
            <p>{{productDescription}}</p>
          </Col>
        </Card>
      </Col>

      <Col :sm="12" :lg="16" class="col-tables">
        <Card shadow>
          <p slot="title">Device Information</p>
          <Table
            stripe
            :show-header="showHeader"
            :columns="deviceInfo.columns"
            :data="deviceInfo.data"
            :size="tableSize"
          ></Table>
        </Card>
        <Card shadow>
          <p slot="title">Client Information</p>
          <Table
            stripe
            :show-header="showHeader"
            :columns="clientInfo.columns"
            :data="clientInfo.data"
            :size="tableSize"
          ></Table>
        </Card>
        <Card shadow>
          <p slot="title">Compatility Check</p>
          <Row type="flex" justify="center">
            <Button type="primary" shape="circle" long @click="progress">Compatility Check</Button>
          </Row>
        </Card>
      </Col>
    </Row>

    <!--progress bar-->
    <Row style="padding:20px 0px">
      <Progress v-if="showProgressBar" :percent="percent"></Progress>
    </Row>

    <!--client and agent info-->
    <Row v-if="showCheckingResult" :gutter="16" style="padding:20px 0px;">
      <Col span="12">
        <Card shadow>
          <p slot="title">Client Compatibility Check</p>
          <Table
            stripe
            :show-header="showHeader"
            :columns="compatilityCheck.columns"
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
            :columns="compatilityCheck.columns"
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
        <video controls :src="'/static/'+ compatilityCheck.referenceVedio" type="video/mp4"></video>
      </Card>
    </Row>
    
  </div>
</template>

<script>
export default {
  name: "Info",
  props: {
    productPic: {
      type: String,
      default: "mic.jpg"
    },
    productName: {
      type: String,
      default: "Nuance Power MIC III"
    },
    productLink: {
      type: String,
      default: "https://www.nuance.com"
    },
    productLogo: {
      type: String,
      default: "nuance.jpg"
    },
    productDescription: {
      type: String,
      default:
        "Designed to enhance productivity and provide ergonomic control of both standard dictation and speech recognition functions."
    },
    deviceInfo: {
      default: {
        columns: [
          { title: "Features", key: "feature" },
          { title: "Information", key: "info" }
        ],
        data: [
          { feature: "Device Name", info: "Nuance Power MIC III" },
          { feature: "Vendor Name", info: "Nuance" },
          { feature: "VID", info: "vid-0554" },
          { feature: "PID", info: "pid-1001" }
        ]
      }
    },
    clientInfo: {
      default: {
        columns: [
          { title: "Features", key: "feature" },
          { title: "Information", key: "info" }
        ],
        data: [
          { feature: "Client OS", info: "Windows 10 64bits 1903" },
          { feature: "Client Hardware", info: "Dell Optiplex 7060" }
        ]
      }
    },
    compatilityCheck: {
      default: {
        columns: [
          { title: "Features", key: "feature" },
          { title: "Info", key: "info" },
          {
            title: "Check",
            key: "check",
            width: 100,
            render: (h, params) => {
              let _string = "Pass";
              let _color = "success";
              console.log(params);
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
        client: [
          { feature: "Client OS", info: "Windows 10 64bits 1903", check: true },
          {
            feature: "Client Hardware",
            info: "Dell Optiplex 7060",
            check: true
          },
          { feature: "PowerMic Firmware", info: "1.4.1", check: true },
          {
            feature: "Setting",
            info: "USB split GPO setting in Client side",
            check: false
          },
          {
            feature: "Setting",
            info: "USB split registy setting in Client side",
            check: false
          },
          { feature: "Horizon client version", info: "5.2", check: true },
          {
            feature: "Horizon client USB arbitrator Service status",
            info: "Runing",
            check: true
          },
          {
            feature: "Horizon client log level",
            info: "Information",
            check: true
          },
          {
            feature: "Nuance solution",
            info: "Nuance PowerMic VMware Client Extension",
            check: false
          }
        ],
        agent: [
          { feature: "Agent OS", info: "Windows 10 64bits 1903", check: false },
          { feature: "Agent Hardware", info: "vSphere VM", check: false },
          { feature: "PowerMic Firmware", info: "1.41", check: false },
          {
            feature: "Setting",
            info: "USB split GPO setting in agent side",
            check: false
          },
          {
            feature: "Setting",
            info: "USB split registy setting in agent side",
            check: false
          },
          { feature: "Horizon agent version", info: "7.10", check: true },
          {
            feature: "Horizon agent USB arbitrator Service status",
            info: "Runing",
            check: true
          },
          {
            feature: "Horizon agent log level",
            info: "Information",
            check: true
          },
          {
            feature: "Nuance solution",
            info: "Nuance PowerMic VMware Agent Extension",
            check: false
          }
        ],
        suggestions: [
          "PowerMic is a USB composite device. It is recommended to use Nuance extension solution to redirect this device instead of USB redirection.",
          "Please follow the guide of Nuance to configure the extensions on client and agent side.",
          "If you don’t use the extension solution, you can follow the KB to configure the GPO for USB split on Horizon agent machine."
        ],
        referenceVedio: "PowerMic.mp4"
      }
    }
  },

  data() {
    return {
      showHeader: false, //tableHeader
      showProgressBar: false,
      showCheckingResult: false,
      tableSize: "small",
      percent: 0
    };
  },
  methods: {
    progress() {
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
          this.showCheckingResult = true;
        });
      }
    }
  }
};
</script>






<style scoped>
.container {
  padding: 30px 60px;
  background-color: #eee;
  /* font-family: 'Open Sans', serif; */
  font-weight:700;
}

.row {
}
img {
  width: 100%;
}

.name-and-link {
  text-align: center;
  font-weight: 600;
  font-size: 1.25rem;
}
.content,
.name-and-link {
  font-family: "Open Sans", serif;
}

.col-tables {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
