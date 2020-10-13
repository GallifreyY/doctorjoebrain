<template>
   <div class="step">
    <Sider id="sider" style="overflow:scroll" width="380px">
       <Menu active-name="1-3" :open-names="['1']" width="380px">
        <Submenu name="1">
            <template slot="title">
                <Icon type="ios-analytics" />
                HorizonPeripheralsAgent Installer Guide
            </template>

              <a name="1-1" @click="handlezip" class="linka">HorizonPeripheralsAgent.zip</a>
                <a class="linka" @click="handlemsi" name="1-2">HorizonPeripheralsAgent.msi</a>
                <a class="active" @click="handlestep" name="1-3">Installation steps</a>
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
                <a class="linka" @click="handleusermatrix" name="3-2">How to check the device support matrix?</a>
                <a class="linka" @click="handleuserlogin" name="3-3">How to login as Admin to maintain and edit the device support matrix?</a>

        </Submenu>
    </Menu>
    </Sider>
    <div class="content">
       <h4>&nbsp;&nbsp;&nbsp;&nbsp;We provide two ways to install the HorizonPeripheralsAgent program – zip package and msi installer. Use the zip package if you only have normal user permission in the remote agent desktop. Use the msi installer if you have admin user permission.</h4><br />
         <img class="dj-installer-pic" src="../../assets/dj-agent-installer1.png">
      <h4>&nbsp;&nbsp;&nbsp;You can change the installation directory. By default, it is C:\HorizonPeripheralsAgent\ directory.</h4>
        <img class="dj-installer-pic" src="../../assets/dj-agent-installer2.png">
      <h4>There are two sub features of the msi installer – core and autolaunch. Zip package only contains the core feature.</h4>
      <h4><strong>*</strong>&nbsp;&nbsp;&nbsp;Core feature will copy all necessary files to the installation directory you choose.</h4>
      <h4><strong>*</strong>&nbsp;&nbsp;&nbsp;Autolaunch feature will add registry entries in HKLM path. These registries make HorizonPeripheralsAgent.exe launch automatically when you freshly login a Horizon desktop or app session.</h4>
      <h4><strong>*</strong>&nbsp;&nbsp;&nbsp;The registry entries are in the HKLM path. These registries make HorizonPeripheralsAgent.exe launch automatically whenever you freshly login a Horizon desktop or app session. The registries are –</h4>
      <h4 style="font-style: italic">&nbsp;&nbsp;&nbsp;“HKLM\\Software\\VMware, Inc.\\VMware VDM\\UnityShell\\Run”</h4>
      <h4 style="font-style: italic">&nbsp;&nbsp;&nbsp;“HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run”</h4>
      <br /><img style="width: 800px;height: 350px" src="../../assets/dj-agent-installer4.png"><br />
    </div>
  </div>
</template>
<script>
    export default {
name:"InstallStep",
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
    margin-left: 100px;
    margin-bottom: 50px;
    width: 500px;
    height: 400px;
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
