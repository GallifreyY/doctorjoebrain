<template>
   <div class="content1">
    <Sider id="sider" style="overflow:scroll" width="380px">
       <Menu active-name="1-2" :open-names="['1']" width="380px">
        <Submenu name="1">
            <template slot="title">
                <Icon type="ios-analytics" />
                HorizonPeripheralsAgent Installer Guide
            </template>
                <a name="1-1" @click="handlezip" class="active">HorizonPeripheralsAgent.zip</a>
                <a class="linka" @click="handlemsi" name="1-2">HorizonPeripheralsAgent.msi</a>
                <a class="linka" @click="handlestep" name="1-3">Installation steps</a>
                <a class="linka" @click="handlemod" name="1-4">Web server configuration</a>

        </Submenu>
        <Submenu name="2">
            <template slot="title">
                <Icon type="ios-filing" />
                HorizonPeripheralsClient Installer Guide
            </template>
            <a class="linka" @click="handleclient" name="2-1">Installation steps</a>
        </Submenu>

    </Menu>
    </Sider>
    <div class="content">
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;We provide two ways to install the HorizonPeripheralsAgent program – zip package and msi installer. Use the zip package if you only have normal user permission in the remote agent desktop. Use the msi installer if you have admin user permission.</h4><br />
      <br /><h3>  HorizonPeripheralsAgent.zip</h3><br />
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;HorizonPeripheralsAgent.zip contains all the files to be copied and extracted on your Horizon agent machine. Use this zip file instead of msi installer to deploy the program if the agent OS has some limitations to run MSI installer under normal user privilege. In this way, the AutoLaunch registries and functions will be missing. You must manually launch the HorizonPeripheralsAgent program under the installation folder. You will not be able to launch the program in Horizon remote app session since it is not auto launched.</h4>

    </div>
  </div>
</template>
<script>
    export default {
name:"GuideContent",
methods:{
  handlezip(){
    this.$router.replace("/help");
  },
  handlemsi(){
    this.$router.replace("/options");
  },
  handlestep(){
    this.$router.replace("/installstep");
  },
  handlemod(){
    this.$router.replace("/tips");
  },
  handleclient(){
    this.$router.replace("/step");
  }
}
    }
</script>
<style>
 .content {
  margin-left: 33vw;
  margin-top: 100px;
  /* border: 1px solid red; */
  height:100vh;
   width: 810px;
}
#sider {
  position: fixed;
  height: 100vh;
  left: 0;
  /* overflow: auto; */
  top: 70px;
  background: #fff;
  z-index: 25;
}
  .dj-installer-pic{
    margin-top: 100px;
    margin-left: 100px;
  }
   .link{
    color: black;
  }
  .link:hover{
    color: #0F1D38;
  }
   .linka{
    display: block;
    height:50px;
     margin-top: 20px;
    color:#0F1D38;
    margin-left: 40px;
  }
  .linka:hover{
    color: #2b85e4;
    margin-left: 40px;
    margin-top: 20px;
  }
  .active{
    color: #00aeff;
    display: block;
    height:50px;
    margin-top: 20px;
    margin-left: 40px;
  }
</style>
