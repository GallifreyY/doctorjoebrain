<template>
   <div class="content1">
    <Sider id="sider" style="overflow:scroll" width="380px">
       <Menu active-name="3-3" :open-names="['3']" width="380px">
        <Submenu name="1">
            <template slot="title">
                <Icon type="ios-analytics" />
                HorizonPeripheralsAgent Installer Guide
            </template>
                <a name="1-1" @click="handlezip" class="linka">HorizonPeripheralsAgent.zip</a>
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
         <Submenu name="3">
            <template slot="title">
                <Icon type="ios-aperture" />
                Peripherals Intelligence User Guide
            </template>
                <a name="3-1" @click="handleuserprocess" class="linka">How to start a diagnosis process?</a>
                <a class="active" @click="handleusermatrix" name="3-2">How to check the device support matrix?</a>
                <a class="linka" @click="handleuserlogin" name="3-3">How to login as Admin to maintain and edit the device support matrix?</a>

        </Submenu>

    </Menu>
    </Sider>
    <div class="content">
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;Use any browser to open Horizon Peripherals Intelligence web server page. On the device matrix page, click “admin login” button on the right side.</h4><br />
      <img class="dj-installer-pic" src="../../assets/userguide_matrix1.png">
    </div>
  </div>
</template>
<script>
    export default {
name:"GuideUserMatrix",
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
  },
  handleuserprocess(){
    this.$router.replace("/userprocess");
  },
  handleusermatrix(){
    this.$router.replace("/usermatrix");
  },
  handleuserlogin(){
    this.$router.replace("/userlogin");
  },
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
    margin-top: 50px;
    margin-left: 50px;
    margin-bottom: 50px;
    width: 700px;
    height: 350px;
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
