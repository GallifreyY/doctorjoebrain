<template>
  <div style="padding:2% 5% 2% 5% ">
    <Row class="buttons">
      <Col span="8">
        <Input search placeholder="Search device names..." />
      </Col>
      <Col span="3" >
      <Button  shape = "circle" @click="reload" style="margin-left:5% "><Icon type="ios-refresh" size="18" /></Button>
      </Col>
      <Col span="5" offset="8">
        <ButtonGroup shape="circle">
          <Button @click="handleUpload">
            <Icon type="ios-cloud-upload-outline" size="18" style="margin-right:5px" />Upload
          </Button>
          <d-form :modalForm.sync = "modalForm"></d-form>
          <Button @click="handleDownload">
            <Icon type="ios-cloud-download-outline" size="18" style="margin-right:5px" />Download
          </Button>
        </ButtonGroup>
      </Col>
    </Row>
    <Row class="table">
      <Table :columns="columns1" :data="matrixAllData" ref="table"></Table>
    </Row>
  </div>
</template>

<script>
import { getMatrix } from "@/api/matrix";
import DForm from "./DForm.vue";

export default {
  name: "DTable",
  inject:['reload'],
  components: { DForm },
  data() {
    return {
      matrixAllData: undefined,
      submit: false,
      modalForm : false,
      columns1: [
        {
          title: "Device Name",
          key: "device_name",
          width: "200",
          align: "center"
        },
        { title: "Category", key: "category", width: "100", align: "center" },
        { title: "Vid", key: "vendor_id", width: "100", align: "center" },
        { title: "Pid", key: "product_id", width: "100", align: "center" },
        { title: "Model", key: "model", width: "100", align: "center" },
        {
          title: "Horizon Version",
          align: "center",
          children: [
            {
              title: "Client",
              key: "Horizon_client_version",
              width: "100",
              align: "center"
            },
            {
              title: "Agent",
              key: "Horizon_agent_version",
              width: "100",
              align: "center"
            }
          ]
        },

        // { title: "Redirect Method", key: "redirect_method", align: "center" },
        {
          title: "Action",
          key: "action",
          align: "center",
          render: (h, params) => {
            return h("div", [
              h(
                "Button",
                {
                  props: {
                    type: "primary",
                    size: "small"
                  },
                  style: {
                    marginRight: "5px"
                  },
                  on: {}
                },
                "View"
              ),
              h(
                "Button",
                {
                  props: {
                    type: "error",
                    size: "small"
                  },
                  on: {}
                },
                "Delete"
              )
            ]);
          }
        }
      ]
    };
  },
  methods: {
    fetchMatrix() {
      getMatrix()
        .then(response => {
          this.matrixAllData = response.data;
          this._parse_cate(this.matrixAllData);
        })
        .catch(() => {
          this.$Message.error("'Sorry, could not get Data Matrix..'");
        });
    },
    handleUpload() {
      this.modalForm = true;
    },
    handleDownload() {
      this.$refs.table.exportCsv({
        filename: "Device Matrix Data"
      });
    },
    _parse_cate(items) {
      items.forEach((val, index, arr) => {
        let map = ["USB Disks", "Printers", "Scanners", "Cameras", "Mics"];
        arr[index].category = map[arr[index].category] || "Other Devices";
      });
    }
  },
  created() {
    this.fetchMatrix();
  }
};
</script>

<style lang="" scoped>
.table {
  margin-top: 2%;
}
</style>