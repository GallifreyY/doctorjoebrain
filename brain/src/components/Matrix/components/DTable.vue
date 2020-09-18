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
      <Col span="11" offset="2">
        <ButtonGroup shape="circle">
          <Button v-if="token == 'false'" @click="handleLogin">
            <Icon type="md-person" size="18" style="margin-right:3px"/>
            admin Login
          </Button>
          <Button v-else @click="personal=true" class="link">
            <Icon type="ios-log-out" size="18" style="margin-right:3px"/>
           Log out
          </Button>
          <Modal v-model="personal" width="360">
            <p slot="header" style="color:rgb(0, 174, 255);text-align:center">
              <Icon type="ios-information-circle"></Icon>
              <span>Your Information</span>
            </p>
            <div style="text-align:center">
              <p>Administrator confirms logout</p>

            </div>
            <div slot="footer">
              <Button type="error" size="large" long @click="handleLogout">Log out
              </Button>
            </div>
          </Modal>
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
    </br>
    <Row class="buttons">
    <Col span="8">
      <Input
          v-model="searchVersion"
          search
          placeholder="Search horizon versions..."
          @on-search="handleSearchV"
        />
      </Col>
      <Col span="3">
        <Button shape="circle" @click="reload" style="margin-left:5% ">
          <Icon type="ios-refresh" size="18" />
        </Button>
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
        <Table :columns="columns1" :data="matrixSearchedData" ref="table"></Table>
      </Row>
    </div>
    <div v-if="showSearchResult == false">
    <Row class="table">
      <Table stripe :columns="columns1" :data="matrixDisplayData" ref="table"></Table>
      <d-item :modalItem.sync="modalItem" :data="modalItemDataProps"></d-item>
    </Row>
    </div>

  </div>
</template>

<script>
import { getMatrix, deleteData } from "@/api/matrix";
import DForm from "./DForm.vue";
import DItem from "./DItem.vue";
import { mapGetters } from "vuex";
import {trsPassword} from "@/api/user";

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
      personal: false,
      personalLoading: false,
      cateList:[],
      searchString: "",
      searchVersion: "",
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
  computed: {
      ...mapGetters(["token", "name", "roles", "uuid"]),
      reportLink: {
        get: function () {
          return '/diagnosis/' + this.uuid;
        }
      }
    },
  methods: {
    handleLogout() {
        this.personalLoading = true
        this.$store.dispatch("user/logout").then(() => {
          this.personal = false
          this.personalLoading = false
          this.$Message.success('Successfully Log out')
        }).catch(() => {
          this.personalLoading = false
          this.$Message.error('Something going wrong..')

        })
      },

      handleLogin() {
        trsPassword()
          .then(response => {
            var result = response.data['message']
            if (result > 0) {
              this.$router.replace("/Log-in")
            } else {
              this.$router.replace("/modify")
            }
          })
          .catch(error => {
            console.log(error);
            this.$Message.error("Sorry, there's something wrong with this this page");
          });
      },
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
    handleSearchV() {
      this.showSearchResult = true;
      this.searchedData = this._searchV(this.searchVersion);
    },
    handleClose(){
      this.showSearchResult = false;
      this.searchedData = undefined
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
    },
  
  _searchV(searchVersion){
      const res = []
      if(!searchVersion) return []
      if(this.searchedData === undefined ){
      for(let data of this.matrixDisplayData){
        console.log(data);
        if(data.Horizon_client_version.slice(0,searchVersion.length) === searchVersion|| data.Horizon_agent_version.slice(0,searchVersion.length) === searchVersion){
          res.push(data)
        }
      }
      }
      else{
        for(let data of this.matrixSearchedData){
        console.log(data);
        if(data.Horizon_client_version.slice(0,searchVersion.length) === searchVersion|| data.Horizon_agent_version.slice(0,searchVersion.length) === searchVersion){
          res.push(data)
        }
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
    matrixSearchedData: function() {
      return this._filter(this.searchedData, this.filter);
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
