<template>
  <div style="padding:2% 5% 2% 5% ">
    <Row class="buttons">
      <Col span="8">
        <Input
          v-model="searchString"
          search
          placeholder="Search device names..."
          @on-search="handleSearch"
        />
      </Col>
      <Col span="3">
        <Button shape="circle" @click="reload" style="margin-left:5% ">
          <Icon type="ios-refresh" size="18" />
        </Button>
      </Col>
      <Col span="7" offset="6">
        <ButtonGroup shape="circle">
          <Button @click="handleUpload" :disabled="!admission">
            <Icon type="ios-cloud-upload-outline" size="18" style="margin-right:5px" />Add New Device
          </Button>
          <d-form :modalForm.sync="modalForm" :categoryList="cateList"></d-form>
          <Button @click="handleDownload">
            <Icon type="ios-cloud-download-outline" size="18" style="margin-right:5px" />Download
          </Button>
        </ButtonGroup>
      </Col>
    </Row>
    <div v-if="showSearchResult">
      <Divider>
        Search Result
        <Icon
          type="ios-close-circle-outline"
          color="red"
          style="margin-left:10%;cursor:pointer"
          @click.native="handleClose"
        />
      </Divider>
      <Row class="search-result">
        <Table :columns="columns1" :data="searchedData"></Table>
      </Row>
      <Divider>Matrix</Divider>
    </div>
    <Row class="table">
      <Table stripe :columns="columns1" :data="matrixDisplayData" ref="table"></Table>
      <d-item :modalItem.sync="modalItem" :data="modalItemDataProps"></d-item>
    </Row>
  </div>
</template>

<script>
import { getMatrix, deleteData } from "@/api/matrix";
import DForm from "./DForm.vue";
import DItem from "./DItem.vue";
import { mapGetters } from "vuex";

export default {
  name: "DTable",
  inject: ["reload"],
  components: { DForm, DItem },
  props: {
    filter: {
      default: "all",
      type: String,
      required: false
    },
    otherIndex :{
      default:'5',
      type: String,
      required:false
    }
  },
  data() {
    return {
      cateList:[],
      searchString: "",
      searchedData:undefined,
      showSearchResult: false,
      matrixAllData: undefined,
      modalItemData: undefined,
      submit: false,
      modalForm: false,
      modalItem: false,
      columns1: [
        { type: "index", width: 60, align: "center" },
        {
          title: "Device Name",
          key: "device_name",
          width: "200",
          align: "center",
          sortable: true
        },
        {
          title: "Category",
          key: "category",
          width: "130",
          align: "center",
          sortable: true
        },
        {
          title: "Vid",
          key: "vendor_id",
          width: "100",
          align: "center",
          sortable: true
        },
        {
          title: "Pid",
          key: "product_id",
          width: "100",
          align: "center",
          sortable: true
        },
        { title: "Model", key: "model", width: "100", align: "center" },
        {
          title: "Horizon Version",
          align: "center",
          children: [
            {
              title: "Client",
              key: "Horizon_client_version",
              width: "100",
              align: "center",
              sortable: true
            },
            {
              title: "Agent",
              key: "Horizon_agent_version",
              width: "100",
              align: "center",
              sortable: true
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
                    size: "small",
                    disabled: !this.admission
                  },
                  style: {
                    marginRight: "5px"
                  },
                  on: {
                    click: () => {
                      this.handleEdit(params.index);
                    }
                  }
                },
                "Edit"
              ),
              h(
                "Button",
                {
                  props: {
                    type: "error",
                    size: "small",
                    disabled: !this.admission
                  },
                  on: {
                    click: () => {
                      this.handleDelete(params.index);
                    }
                  }
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
          this.cateList = response.cateList;
          this._parse_cate(this.matrixAllData);
        })
        .catch(() => {
          this.$Message.error("Sorry, could not get Data Matrix..");
        });
    },
    handleSearch() {
      this.showSearchResult = true;
      this.searchedData = this._search(this.searchString);
    },
    handleClose(){
      this.showSearchResult = false;
    },
    handleUpload() {
      this.modalForm = true;
    },
    handleDownload() {
      this.$refs.table.exportCsv({
        filename: "Device Matrix Data"
      });
    },
    handleDelete(index) {
      let deleteItem = this.matrixDisplayData[index];
      alert(this.matrixDisplayData[index].device_name);
      delete deleteItem.category;
      delete deleteItem.device_name;

      deleteData(deleteItem)
        .then(response => {
          this.$Message.success("Successfully delete this item..");
          this.reload();
        })
        .catch(error => {
          this.$Message.error("Sorry, could not get Delete this item");
        });
    },
    handleEdit(index) {
      this.modalItem = true;
      this.modalItemData = this.matrixDisplayData[index];
    },

    _parse_cate(items) {
      items.forEach((val, index, arr) => {
        arr[index].category = this.cateList[arr[index].category] || "Other Devices";
      });
    },
    _other_filter(ele){
      return (this.cateList.indexOf(ele.category) > this.otherIndex) || ele.category === 'Other Devices'
    },
    _filter(items, filter, otherIndex) {
      if (this.filter === "all") return items;
      console.log(this.otherIndex)
      if(this.filter === 'other'){
        return items.filter(this._other_filter)
      }
      return items.filter(item => item.category === filter);
    },
    _search(searchString){
      const res = []
      if(!searchString) return []
      for(let data of this.matrixDisplayData){
        console.log(data);
        if(data.device_name.slice(0,searchString.length).toLowerCase() === searchString.toLowerCase()){
          res.push(data)
        }
      }
      if(res.length === 0 ){
        this.$Notice.error({
          title:"No Search Result"

        })
      }
      return res
    }
  },
  computed: {
    ...mapGetters(["token"]),
    admission: function() {
      return this.token === "true";
    },
    matrixDisplayData: function() {
      return this._filter(this.matrixAllData, this.filter);
    },
    modalItemDataProps: function() {
      return this.modalItemData;
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
.search-result {
  margin: 2% 0;
}
</style>