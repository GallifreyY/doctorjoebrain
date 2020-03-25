<template>
  <Layout class="device-layout">
    <Sider style="position:fixed;height:100%;background-color:rgb(229, 235, 238);">
      <!-- search bar -->
      <div style="padding:5%">
        <Input search enter-button placeholder="Search Products..." />
      </div>

      <!--select category-->
      <div class="select-category">
        <Tag size="large" color="primary" style="margin-left: 5%;">
          <Icon type="md-apps" size="15" />Device Category
        </Tag>
        <RadioGroup v-model="vertical" vertical class="radios">
          <Radio v-for="cate in deviceCategory" :key="cate" :label="cate" class="radio">
            <Icon type="social-apple"></Icon>
            <span>{{cate}}</span>
          </Radio>
        </RadioGroup>
      </div>
    </Sider>

    <!--table-->

    <Content class="table-container" style="margin-left:200px;padding:15px;">
      <div class="table-menu"></div>

      <div class="table-main">
        <Table border size="small" :columns="mainColumn" :data="matrixData"></Table>
      </div>
    </Content>

    <!-- <Card></Card> -->
  </Layout>
</template>

<script>
import { getMatrix } from "@/api/matrix";
export default {
  name: "DeviceTable",
  props: {
    deviceCategory: {
      default: [
        "All Devices",
        "Printers",
        "Scanners",
        "SppechMics",
        "USB DVD Recorders",
        "Pin Pads"
      ]
    }
  },
  data() {
    return {
      mainColumn: [
        { title: "Name", key: "device_name", width: 200, fixed: "left" },
        { title: "Version", key: "device_version", width: 100 },
        {
          title: "Picture",
          key: "picture",
          width: 150,
          render: (h, params) => {
            let _path = params.row.picture;
            console.log("/static/device/" + _path);
            return h(
              "div",
              [
                h("img", {
                  attrs: {
                    src: "/static/device/" + _path,
                    style: "width:100px;height:100px;"
                  }
                })
              ],
              {
                attrs: {
                  //style:"display:flex; justify-content:center"
                }
              }
            );
          }
        },
        { title: "Client OS", key: "client_os_name", width: 200 },
        {
          title: "Horizon Client Versions",
          key: "Horizon_client_version",
          width: 200
        },
        { title: "Agent OS", key: "agent_os_name", width: 200 },
        { title: "Client Driver", key: "agent_driver", width: 150 },
        { title: "Agent Driver", key: "client_driver", width: 150 }
      ],
      matrixData: undefined
    };
  },
  methods: {
    fetchMatrix() {
      getMatrix()
        .then(response => {
          this.matrixData = response.data;
        })
        .catch(() => {
          this.$Message.error("'Sorry, could not get Data Matrix..'");
        });
    }
  },
  created() {
    this.fetchMatrix();
  }
};
</script>

<style lang="" scoped>
.device-layout {
  margin-top: 70px;
}
.select-category {
  width: 100%;
  /* text-align: center; */
  padding: 5% 0%;
}
span {
  font-size: 12px;
  font-weight: 500;
}
.radios {
  text-align: start;
  width: 100%;
}
.radio {
  padding: 5% 0% 5% 15%;
}
.table-container {
  width: 100%;
  /* border: 2px solid red; */
  margin-left: 200px;
  padding: 15px;
  background-color: white;
}

.table-main {
  padding: 5%;
  width: 100%;
  /* border: 2px solid red; */
}
</style>