<template>
  <Layout class="device-layout">
    <Sider style="position:fixed;height:100%;background-color:rgb(229, 235, 238);">
      <!-- search bar -->
      <div style="padding:5%">
        <Input search enter-button placeholder="Search Products..." />
      </div>

      <!--select category-->
      <!-- would like to change there -->
      <div class="select-category">
        <Tag size="large" color="primary" style="margin-left: 5%;">
          <Icon type="md-apps" size="15" />
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
      <span class="table-menu">
         <Button type="primary" icon = "ios-create" @click = "addItem">Edit</Button>     
          <!-- modal -->
          <Modal
            v-model="editModal"
            title="Warning"
            @on-ok="handelModalOK"
            ok-text="Continue"
            cancel-text="Cancel"
            >
            <p>Your modification will be updated in the Database.</p> 
            <p>Are you sure to continue ?</p>
          </Modal>
      </span>
      <matrix-form style="padding:1% 5% 1% 5%;" :showForm="showForm"></matrix-form>
      <div class="table-main">
        <Table border size="small" :columns="mainColumn" :data="matrixData"></Table>
      </div>
    </Content>

    <!-- <Card></Card> -->
  </Layout>
</template>

<script>
import { getMatrix } from "@/api/matrix";
import MatrixForm from "@/components/MatrixForm";
import { MapGetters, mapGetters } from "vuex";

export default {
  name: "DeviceTable",
  components:{MatrixForm},
  props: {
    deviceCategory: {
      default: [
        "All Devices",
        "Printers",
        "Scanners",
        "SpeechMics",
        "USB DVD Recorders",
        "Pin Pads"
      ]
    }
  },
  data() {
    return {
      editModal : false,
      showForm : false,
      //matrix:
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
  computed:{
    ...mapGetters(["token"])
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
    },
    addItem(){
      if(this.token == 'true'){
          this.editModal = true;
      }else{
        this.$Message.warning("You do not have permission to continue. Please log in.")
      }
    },
    handelModalOK(){
      this.showForm= true;
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
  border: 2px solid red;
  margin-left: 200px;
  /* padding: 15px; */
  background-color: white;
}

.table-main {
  padding: 5%;
  padding-top: 1%;
  width: 100%;
  border: 2px solid red;
}

.table-menu{
  padding : 5%;
  padding-top: 1%;

}

</style>