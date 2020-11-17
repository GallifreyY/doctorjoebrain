<template>
  <div class="report-menu">
    <Sider id="reportsider" style="overflow:scroll">
    <Menu theme="light" active-name="1">
       <MenuItem v-for = "(item,index) in reportCategoryList" :key="index" :name="index" @click.native="handleClick(item)" >
          <Icon type="ios-arrow-forward"></Icon>
         {{item}}
          </MenuItem>
    </Menu>
      </Sider>
    <div class="reportcontent">
<template>
    <Table :columns="reportColumns" :data="reportData" style="margin-left: 220px" class="infotable"></Table>
</template>
<!--     <report-table></report-table>-->
    </div>
    <br>
    </div>
</template>
<script>
   import rexpandRow from '@/components/ReportTableExpand';
    import { getBasicInfo} from "@/api/diagnosis";
    export default {
      name: "ReportMenu",
      components: {rexpandRow},
      data () {
            return {
              reportColumns: [
                    {
                        type: 'expand',
                        width: 50,
                        render: (h, params) => {
                            return h(rexpandRow, {
                                props: {
                                    row: params.row,
                                    index: params.index
                                }
                            })
                        }
                    },
                    {
                        title: 'DeviceName',
                        key: 'deviceName'
                    },
                  {
                    title: ' ',
                    key: 'infoLen',
                    width: '400px',
                    align: 'right',
                    render: (h, params) => {
                      if(this.reportData[params.index].infoLen.warningLen != 0 && this.reportData[params.index].infoLen.errorLen===0 && this.reportData[params.index].infoLen.suggestionLen===0){
                      return h('div', [
                        h('Button', {
                          props: {
                            type: 'warning',
                            size: 'small'
                          },
                          style: {
                            width:'110px'
                          },
                        }, this.data9[params.index].infoLen.warningLen + '  warning'),
                      ]);
                      }else if(this.reportData[params.index].infoLen.warningLen != 0 && this.reportData[params.index].infoLen.errorLen!=0 && this.reportData[params.index].infoLen.suggestionLen!=0){
                        return h('div', [
                        h('Button', {
                          props: {
                            type: 'error',
                            size: 'small'
                          },
                          style: {
                            marginRight: '5px',
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.errorLen + '  error'),
                         h('Button', {
                          props: {
                            type: 'warning',
                            size: 'small'
                          },
                          style: {
                            marginRight: '5px',
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.warningLen + '  warning'),
                        h('Button', {
                          props: {
                            type: 'success',
                            size: 'small'
                          },
                          style: {
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.suggestionLen + '  suggestions')
                      ]);
                      }else if(this.reportData[params.index].infoLen.warningLen === 0 && this.reportData[params.index].infoLen.errorLen!=0 && this.reportData[params.index].infoLen.suggestionLen===0){
                        return h('div', [
                        h('Button', {
                          props: {
                            type: 'error',
                            size: 'small'
                          },
                         style: {
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.errorLen + '  error'),
                      ]);
                      }else if(this.reportData[params.index].infoLen.warningLen === 0 && this.reportData[params.index].infoLen.errorLen===0 && this.reportData[params.index].infoLen.suggestionLen!=0){
                        return h('div', [
                        h('Button', {
                          props: {
                            type: 'success',
                            size: 'small'
                          },
                          style: {
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.suggestionLen + '  suggestions')
                      ]);
                      }else if(this.reportData[params.index].infoLen.warningLen != 0 && this.reportData[params.index].infoLen.errorLen!=0 && this.reportData[params.index].infoLen.suggestionLen===0){
                        return h('div', [
                        h('Button', {
                          props: {
                            type: 'warning',
                            size: 'small'
                          },
                          style: {
                            marginRight: '5px',
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.warningLen + '  warning'),
                        h('Button', {
                          props: {
                            type: 'error',
                            size: 'small'
                          },
                          style: {
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.errorLen + '  error')
                      ]);
                      }else if(this.reportData[params.index].infoLen.warningLen === 0 && this.reportData[params.index].infoLen.errorLen!=0 && this.reportData[params.index].infoLen.suggestionLen!=0){
                        return h('div', [
                        h('Button', {
                          props: {
                            type: 'error',
                            size: 'small'
                          },
                          style: {
                            marginRight: '5px',
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.errorLen + '  error'),
                        h('Button', {
                          props: {
                            type: 'success',
                            size: 'small'
                          },
                           style: {
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.suggestionLen + '  suggestions')
                      ]);
                      }else if(this.reportData[params.index].infoLen.warningLen != 0 && this.reportData[params.index].infoLen.errorLen===0 && this.reportData[params.index].infoLen.suggestionLen!=0){
                        return h('div', [
                        h('Button', {
                          props: {
                            type: 'warning',
                            size: 'small'
                          },
                          style: {
                            marginRight: '5px',
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.warningLen + '  warning'),
                        h('Button', {
                          props: {
                            type: 'success',
                            size: 'small'
                          },
                           style: {
                            width:'110px'
                          },
                        }, this.reportData[params.index].infoLen.suggestionLen + '  suggestions')
                      ]);
                      }

                    }
                  }
                ],
                reportData: [],
              filter:'all',
              reportCategoryList : [],
            }
        },
      methods:{
          handleClick(Category){
      this.filter = Category
            this.fetchInfoTable();
    },
        fetchInfoTable() {
          let uid = this.$route.params.id;
      getBasicInfo(uid)
        .then(response => {
          var infoDataSet = new Set();
          let infoData = response.data.diagnosisTypeInfo;
          infoData.forEach(function (value) {
              var copyValue = value;
             let errorRes = [];
          value.errorInfo.forEach(item => {
          let errorSug = {};
          if (item instanceof Array) {
            errorSug["rcontext"] = item[0];
            errorSug["rhasDetail"] = true;
            errorSug["rdetail"] = item[1];
          } else {
            errorSug["rcontext"] = item;
            errorSug["rhasDetail"] = false;
          }
          errorRes.push(errorSug);
        });
              copyValue.errorInfo = errorRes;

            let warnRes = [];
        value.warningInfo.forEach(item => {
        let warnSug = {};
        if (item instanceof Array) {
          warnSug["rcontext"] = item[0];
          warnSug["rhasDetail"] = true;
          warnSug["rdetail"] = item[1];
        } else {
          warnSug["rcontext"] = item;
          warnSug["rhasDetail"] = false;
        }
        warnRes.push(warnSug);});
        copyValue.warningInfo = warnRes;
        let sugRes = [];
        value.suggestionInfo.forEach(item => {
        let sugSug = {};
        if (item instanceof Array) {
          sugSug["rcontext"] = item[0];
          sugSug["rhasDetail"] = true;
          sugSug["rdetail"] = item[1];
        } else {
          sugSug["rcontext"] = item;
          sugSug["rhasDetail"] = false;
        }
        sugRes.push(sugSug);});
              copyValue.suggestionInfo = sugRes;

              infoDataSet.add(value);
          })
          let requestDataArray = []
          infoDataSet.forEach(item => {
            console.log(item.deviceType)
            if (item.deviceType === this.filter) {
               requestDataArray.push(item);
            }
          })
          if (this.filter === 'all') {
            this.reportData = Array.from(infoDataSet);
          } else {
            this.reportData = requestDataArray;
          }
        //  this.reportData = response.data.diagnosisTypeInfo; //array

        })
        .catch(() => {
          this.$Loading.error();
          this.$Message.error(
            "Sorry, could not get your diagnosis information..."
          );
        });
         },


        fetchCategoryTable() {
          let uid = this.$route.params.id;
          console.log(this.$route.params.id)
          getBasicInfo(uid)
            .then(response => {
              var categoryInfoDataSet = new Set();
              let categoryInfoData = response.data.diagnosisTypeInfo;
              categoryInfoData.forEach(function (value) {
                categoryInfoDataSet.add(value.deviceType);

              })
              this.reportCategoryList = categoryInfoDataSet;
              console.log(this.reportCategoryList);
            })
            .catch(() => {
              this.$Loading.error();
            });
        }
  },
       created(){
    this.fetchCategoryTable();
      this.fetchInfoTable();

  }
    }
</script>
<style>
  #reportsider {
  position: fixed;
  height: 90vh;
  width: 35vw;
  left: 0;
  /* overflow: auto; */
  background: #fff;
  z-index: 25;
}
</style>
