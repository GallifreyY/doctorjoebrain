<template>
  <div class="layout">
    <Sider id="sider" style="overflow:scroll">
      <Menu hide-trigger theme="light" width="auto" open-names="['1']">
        <Submenu name="1">
          <template slot="title">
            <Icon type="md-analytics" size="20" />{{$t("Matrix")}}
          </template>
          <MenuItem name="1" @click.native= "filter = 'all'" >{{$t("All Devices")}}</MenuItem>
          <MenuItem v-for = "(item,index) in categoryList" :key="index" :name="'1-'+index" @click.native="handleClick(item)" >
          {{item}}
          </MenuItem>
          <MenuItem name="other" @click.native= "filter = 'other'" >{{$t("Other Devices")}}</MenuItem>
        </Submenu>
      </Menu>
    </Sider>
    <div class="matrixcontent">
      <d-table :filter='filter' :otherIndex='16' ></d-table>
    </div>
  </div>
</template>

<script>
import DTable from './components/DTable.vue';
import DForm from './components/DForm.vue';
import {getCategoryInfo} from "@/api/matrix";
export default {
  name: "Matrix",
  components:{DTable,DForm},
  data() {
    return {
      filter:'all',
      categoryList : [],
      otherIndex :16
    };
  },
  methods:{
    handleClick(Category){
      this.filter = Category
    }
  },
  created(){
    getCategoryInfo().then(response => {
      console.log(response.data)
      this.categoryList = response.data.slice(0,this.otherIndex);
    }).catch(() => {
          this.$Message.error("Sorry, could not get Category Information..");
        });

  }
};
</script>

<style lang="" scoped>


.matrixcontent {
  margin-left: 12vw;
  margin-top: 75px;
  width: 1180px;
  /* border: 1px solid red; */
  height:100vh;
}
#sider {
  position: fixed;
  height: 90vh;
  width: 35vw;
  left: 0;
  /* overflow: auto; */
  top: 70px;
  background: #fff;
  z-index: 25;
}
</style>
