<template>
  <div style="padding:2% 5% 2% 5% ">
    <Row class="buttons">
      <Col span="8">
        <Input search placeholder="Search device names..." />
      </Col>
      <Col span="5" offset="11">
        <ButtonGroup shape="circle">
          <Button><Icon type="ios-cloud-upload-outline" size="18" style="margin-right:5px"/>Upload</Button>
          <Button><Icon type="ios-cloud-download-outline" size="18" style="margin-right:5px"/>Download</Button>
        </ButtonGroup>
      </Col>
    </Row>
    <Row class="table">
      <Table :columns="columns1" :data="matrixAllData"></Table>
      <!-- <Table></Table> -->
    </Row>
  </div>
</template>

<script>
import { getMatrix } from "@/api/matrix";
export default {
  name: "DTable",
  data() {
    return {
      matrixAllData: undefined,
      columns1: [
        {
          title: "Device Name",
          key: "device_name",
          width: "200",
          align: "center"
        },
        // { title: "Category", key: "category" },
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

        { title: "Redirect Method", key: "redirect_method", align: "center" },
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
.table {
  margin-top: 2%;
}
</style>