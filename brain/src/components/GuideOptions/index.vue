<template>
  <div class="options">
   <Sider id="sider" style="overflow-y:scroll" width="380px" >
       <Menu active-name="1-2" :open-names="['1']" width="380px">
        <Submenu name="1">
            <template slot="title">
                <Icon type="ios-analytics" />
                HorizonPeripheralsAgent Installer Guide
            </template>

               <a name="1-1" @click="handlezip" class="linka">HorizonPeripheralsAgent.zip</a>
                <a class="active" @click="handlemsi" name="1-2">HorizonPeripheralsAgent.msi</a>
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
                <a class="linka" @click="handleusermatrix" name="3-2">How to check the device support matrix?</a>
                <a class="linka" @click="handleuserlogin" name="3-3">How to login as Admin to maintain and edit the device support matrix?</a>

        </Submenu>

    </Menu>
    </Sider>
    <div class="content">
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;There are two files in the downloaded HorizonPeripheralsAgent.zip installer – a zip file (HorizonPeripheralsAgent.zip) and a msi installer (HorizonPeripheralsAgent.msi). Use the zip file if you only have normal user permission in the remote agent desktop. Use the msi installer if you have admin user permission.</h4><br />
      <br /><h3>HorizonPeripheralsAgent.msi</h3><br />
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;HorizonPeripheralsAgent.msi is the installer to be run on your Horizon agent machine. The web server address and port number need to be configured to the correct value firstly. If you don’t know the value, you can use the default one and change it after the installation by editing the config file – hpagentconfig.ini.</h4>

    </div>
  </div>
</template>
<script>
  export default {
    name: "GuideOptions",
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
  }
  .dj-installer-pic1{
    width: 600px;
    height: 450px;
    margin-top: 50px;
    margin-left: 100px;
    margin-bottom: 50px;
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
