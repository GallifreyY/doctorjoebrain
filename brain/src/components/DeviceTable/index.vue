<template>
  <Layout class="device-layout">
    <Sider style="position:fixed;height:100%;background-color:#eee;">
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
    
    <Content class ="table-container" style="margin-left:200px;padding:15px;">
      <div class="table-menu">

      </div>

      <div class="table-main">
        <Table border  size = "small" :columns="mainColumn" :data="data"></Table>
      </div>



    </Content>
    

    <!-- <Card></Card> -->
  </Layout>
</template>

<script>
export default {
  name: "DeviceTable",
  props: {
    deviceCategory: {
      default: [
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
      mainColumn:[
          {title:'Name' , key:'name',width:100,fixed:'left'},
          {title:'Version' , key:'version',width:100},
          {title:'Picture', key:'picture',width:150},
          {title:'Client OS', key:'client-os',width :100},
          {title:'Client Versions', key:'client-versions',width :100},
          {title:'Agent OS', key:'agent-os',width :100},
          {title:'Driver Versions', key:'driver-versions',width :100},
          {title:'Suggetions', key:'suggestions',width:300},
          {title:'Status', key:'status',width:100},
      ]

      
    };
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
.table-container{
  width:100%;
  border: 2px solid red;
  margin-left:200px;
  padding:15px;
  background-color:white;

}

.table-main{
  padding: 5%;
  width:100%;
  border: 2px solid red;
}



.test{
  border: 2px solid red;
  width: 100%;
  height:100%;

}
</style>