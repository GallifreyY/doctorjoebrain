<template>
  <div class="container">
    <!--basic value-->
    <Row :gutter="16" style="background:inherit;" type="flex">
      <Col :sm="12" :lg="8">
        <Card :bordered="false" shadow>
          <img :src="'/static/device/'+ deviceInfo.pic" alt="No Picture" />
          <Row type="flex" justify="center" align="middle">
            <Col :span="8">
              <img :src="'/static/device/'+ deviceInfo.logo" />
            </Col>
            <Col :span="16">
              <div class="name-and-link">
                <p>{{deviceInfo.name}}</p>
                <a :href="deviceInfo.link">{{deviceInfo.link}}</a>
              </div>
            </Col>
          </Row>
          <Col class="content">
            <p>{{deviceInfo.description}}</p>
          </Col>
        </Card>
      </Col>

      <Col :sm="12" :lg="16" class="col-tables">
        <Card shadow>
          <p slot="title">Device Information</p>
          <Table
            stripe
            :show-header="showHeader"
            :columns="columns"
            :data="deviceInfo.data"
            :size="tableSize"
          ></Table>
        </Card>
        <Card shadow>
          <p slot="title">Client Information</p>
          <Table
            stripe
            :show-header="showHeader"
            :columns="columns"
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

    <!--client and agent value-->
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
        <video controls :src="'/static/diagnosis/'+ compatilityCheck.referenceVedio" type="video/mp4"></video>
      </Card>
    </Row>
  </div>
</template>

<script>

const df = require("./default")
console.log(df)

export default {
  name: "Info",
  props: {
  },

  data() {
    return {
      //Data
      deviceInfo: df.deviceInfo,
      clientInfo: df.clientInfo,
      compatilityCheck : df.compatilityCheck,


      //UI
      columns: [
        { title: "Key", key: "key" },
        { title: "Value", key: "value" }
      ],
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
    },
    fetchDeviceInfo(){

    },
    fetchClientInfo(){

    },
    fetchDiagnosisInfo(){
      
    }
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
