<template>
    <Table :columns="columns10" :data="data9" height="400"></Table>
</template>
<script>
    import suexpandRow from '@/components/SuggestionTableExpand';
    import { getBasicInfo} from "@/api/diagnosis";
    // import {getLanguageInfo} from "@/api/diagnosis";
    export default {
       name: "SuggestionTable",
        components: { suexpandRow },
        data () {
         if (navigator.language !== "zh-CN") {
            return {
                columns10: [
                    {
                        type: 'expand',
                        width: 50,
                        render: (h, params) => {
                            return h(suexpandRow, {
                                props: {
                                    row: params.row,
                                    index: params.index
                                }
                            })
                        }
                    },
                    {
                        title: 'Peripherals Health',
                        key: 'deviceName'
                    },
                  {
                    title: ' ',
                    key: 'infoLen',
                    width: '400px',
                    align: 'right',
                    render: (h, params) => {
                      if((this.data9[params.index].errorType === 1) || (this.data9[params.index].errorType === 11)){
                        return h('div', [
                        h('Button', {
                          props: {
                            type: 'error',
                            size: 'small'
                          },
                          style: {
                            width:'110px'
                          },
                        }, this.data9[params.index].infoLen.errorLen + '  error')
                      ]);
                      }else if((this.data9[params.index].erroeType === 0) || (this.data9[params.index].errorType === 10)){
                        return h('div', [
                        h('Button', {
                          props: {
                            type: 'warning',
                            size: 'small'
                          },
                          style: {
                            width:'110px'
                          },
                        }, this.data9[params.index].infoLen.warningLen + '  warning')
                      ]);
                      }else if((this.data9[params.index].erroeType === 2) || (this.data9[params.index].errorType === 21)){
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
                        }, this.data9[params.index].infoLen.warningLen + '  warning'),
                        h('Button', {
                          props: {
                            type: 'error',
                            size: 'small'
                          },
                           style: {
                            width:'110px'
                          },
                        }, this.data9[params.index].infoLen.errorLen + '  error')
                      ]);
                      }

                    }
                  }
                ],
                data9: [],
                errorType: 0
            };
         }else{
            return {
                columns10: [
                    {
                        type: 'expand',
                        width: 50,
                        render: (h, params) => {
                            return h(suexpandRow, {
                                props: {
                                    row: params.row,
                                    index: params.index
                                }
                            })
                        }
                    },
                    {
                        title: '外围设备健康信息',
                        key: 'deviceName'
                    },
                  {
                    title: ' ',
                    key: 'infoLen',
                    width: '400px',
                    align: 'right',
                    render: (h, params) => {
                      if((this.data9[params.index].errorType === 1) || (this.data9[params.index].errorType === 11)){
                        return h('div', [
                        h('Button', {
                          props: {
                            type: 'error',
                            size: 'small'
                          },
                          style: {
                            width:'110px'
                          },
                        }, this.data9[params.index].infoLen.errorLen + '  错误')
                      ]);
                      }else if((this.data9[params.index].erroeType === 0) || (this.data9[params.index].errorType === 10)){
                        return h('div', [
                        h('Button', {
                          props: {
                            type: 'warning',
                            size: 'small'
                          },
                          style: {
                            width:'110px'
                          },
                        }, this.data9[params.index].infoLen.warningLen + '  警告')
                      ]);
                      }else if((this.data9[params.index].erroeType === 2) || (this.data9[params.index].errorType === 21)){
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
                        }, this.data9[params.index].infoLen.warningLen + '  警告'),
                        h('Button', {
                          props: {
                            type: 'error',
                            size: 'small'
                          },
                           style: {
                            width:'110px'
                          },
                        }, this.data9[params.index].infoLen.errorLen + '  错误')
                      ]);
                      }

                    }
                  }
                ],
                data9: [],
                errorType: 0
            };
         }

        },
      methods: {
        fetchInfoTable() {
          let uid = this.$route.params.id;
      getBasicInfo(uid)
        .then(response => {
          let infoDataArray = [];
          let infoData = response.data.diagnosisTypeInfo;
          infoData.forEach(function (value) {
            if ((value.infoLen.errorLen > 0) || (value.infoLen.warningLen > 0)) {
              var copyValue = value;
              let errorRes = [];
               let warnRes = [];
              if ((value.errorType === 1) || (value.errorType === 11)) {
                  value.errorInfo.forEach(item => {
          let errorSug = {};
          if (item instanceof Array) {
            errorSug["context"] = item[0];
            errorSug["hasDetail"] = true;
            errorSug["detail"] = item[1];
          } else {
            errorSug["context"] = item;
            errorSug["hasDetail"] = false;
          }
          errorRes.push(errorSug);
        });
              copyValue.errorInfo = errorRes;
              }
        else if ((value.errorType === 2) || (value.errorType === 21)) {
        value.errorInfo.forEach(item => {
          let errorSug = {};
          if (item instanceof Array) {
            errorSug["context"] = item[0];
            errorSug["hasDetail"] = true;
            errorSug["detail"] = item[1];
          } else {
            errorSug["context"] = item;
            errorSug["hasDetail"] = false;
          }
          errorRes.push(errorSug);
        });
              copyValue.errorInfo = errorRes;
        value.warningInfo.forEach(item => {
        let warnSug = {};
        if (item instanceof Array) {
          warnSug["context"] = item[0];
          warnSug["hasDetail"] = true;
          warnSug["detail"] = item[1];
        } else {
          warnSug["context"] = item;
          warnSug["hasDetail"] = false;
        }
        warnRes.push(warnSug);});
              copyValue.warningInfo = warnRes;
        }
        else if ((value.errorType === 0) || (value.errorType === 10)) {
        value.warningInfo.forEach(item => {
        let warnSug = {};
        if (item instanceof Array) {
          warnSug["context"] = item[0];
          warnSug["hasDetail"] = true;
          warnSug["detail"] = item[1];
        } else {
          warnSug["context"] = item;
          warnSug["hasDetail"] = false;
        }
        warnRes.push(warnSug);});
              copyValue.warningInfo = warnRes;
          }
              infoDataArray.push(value);
            }

          })
          this.data9 = infoDataArray;
          this.$Message.success("Successfully get the report of this device");
        })
        .catch(() => {
          this.$Loading.error();
          this.$Message.error(
            "Sorry, could not get your diagnosis information..."
          );
        });
         },

         },
  created() {
    this.fetchInfoTable();
     // this.fetchLanguageInfo();
  }
    };
</script>
