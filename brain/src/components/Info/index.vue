<template>
  <!-- <div class="container">
    <Row style="margin-top:20px">
        <Col :sm="12" :lg="8">
        <div class = "product">
           <div class = "card">
               <img :src="'/static/'+ productPic" :alt="productName">
                <Row type = "flex" justify="center" align="middle">
                    <Col :span = "8">
                        <img :src="'/static/'+ productLogo">
                    </Col>
                    <Col :span="16">
                        <div class="name-and-link">
                            <p>{{productName}}</p>
                            <a :href="productLink">{{productLink}}</a>
                        </div>
                    </Col>
                </Row>
                <div class="content">
                    <p>{{productDescription}}</p>
                </div>

           </div>
        </div>
        </Col>
        <Col :sm="12" :lg="16">
        <div class = "info">
            <div class="card">
                <Table stripe :show-header="showHeader" :columns="deviceInfo.columns" :data="deviceInfo.data"></Table>
            </div>
            <div class="card">
                <Table stripe :show-header="showHeader" :columns="clientInfo.columns" :data="clientInfo.data"></Table> 
            </div>
        </div>
        </Col>
    </Row>
  </div>-->
  <div class="container">
    <Row :gutter="16" style="background:inherit;padding:20px" type="flex" justify="space-around">
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

      <Col :sm="12" :lg="16" class="tables">
        <Card shadow>
          <p slot="title">Device Information</p>
          <Table
            stripe
            :show-header="showHeader"
            :columns="deviceInfo.columns"
            :data="deviceInfo.data"
          ></Table>
        </Card>
        <Card shadow>
          <p slot="title">Client Information</p>
          <Table
            stripe
            :show-header="showHeader"
            :columns="clientInfo.columns"
            :data="clientInfo.data"
          ></Table>
        </Card>
        <Card shadow>
          <p slot="title">Compatility Check</p>
          <Row type="flex" justify="center">
            <Button type="primary" shape="circle" long>Compatility Check</Button>
          </Row>
        </Card>
      </Col>
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
    }
  },
  data() {
    return {
      showHeader: false
    };
  }
};
</script>






<style scoped>
.container {
  padding-left: 35px;
  padding-right: 35px;
  background-color: #eee;
  font-family: 'Open Sans', serif;
}

img {
  width: 100%;
}
.name-and-link {
  text-align: center;
  
  font-weight: 600;
  font-size: 1.25rem;
   

}
.tables {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
