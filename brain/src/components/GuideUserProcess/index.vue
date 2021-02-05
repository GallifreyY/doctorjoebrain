<template>
   <div class="content1">
    <Sider id="sider" style="overflow-y:scroll" width="380px" >
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
                <a name="3-1" @click="handleuserprocess" class="active">How to start a diagnosis process?</a>
                <a class="linka" @click="handleusermatrix" name="3-2">How to check the device support matrix?</a>
                <a class="linka" @click="handleuserlogin" name="3-3">How to login as Admin to maintain and edit the device support matrix?</a>

        </Submenu>

    </Menu>
    </Sider>
    <div class="content">
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;There are several pre-conditions to start a diagnosis process:</h4><br />
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Successfully install and deploy the Horizon Peripherals Intelligence following the installation guide</h4>
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. With some specific peripheral devices attached to the Horizon Windows client to be diagnosed</h4>
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Horizon client connects to a remote desktop or app session</h4>
      <br />
      <h3>Step 1.</h3><br />
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;Manually launch the HorizonPeripheralsAgent.exe from the installation directory on Horizon agent machine if it is not automatically launched after login. The HorizonPeripheralsAgent icon will appear in the right corner of Windows task bar.</h4>
      <img class="dj-installer-pic" src="../../assets/userguide_step1.png">
      <h3>Step 2.</h3><br />
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;Click on the HorizonPeripheralsAgent icon to show up the menu. Click the diagnose option.</h4>
      <img class="dj-installer-pic" src="../../assets/userguide_step2.png">
      <h3>Step 3.</h3><br />
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;A report link message will pop up promptly. If the network connection with Horizon Peripherals Intelligence server is not very good, it may take a while.</h4>
      <img class="dj-installer-pic" src="../../assets/userguide_step3.png">
      <h3>Step 4.</h3><br />
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;Click the link message to use the default browser to open the device diagnosis report . Then select which device you want to diagnose from the device tree in the left navigator.</h4>
      <img class="dj-installer-pic" src="../../assets/userguide_step4.png">
      <h3>Step 5.</h3><br />
      <h4>Check and browse the device details, Horizon services details and the suggestions for device redirection on the same page.</h4>
      <img class="dj-installer-pic" src="../../assets/userguide_step5.png">
      <img class="dj-installer-pic" src="../../assets/userguide_step6.png">
    </div>
  </div>
</template>
<script>
    export default {
name:"GuideUserProcess",
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
