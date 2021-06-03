<template>
   <div class="stepforlinux">
    <Sider id="sider" style="overflow-y:scroll" width="380px" >
       <Menu active-name="2-2" :open-names="['2']" width="380px" >
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
          <a class="linka" @click="handleclient" name="2-1">Installation steps for Windows</a>
          <a class="active" @click="handleclientlinux" name="2-2">Installation steps for Linux</a>
        </Submenu>
<Submenu name="3">
            <template slot="title">
                <Icon type="ios-aperture" />
                Peripherals Intelligence User Guide
            </template>
                <a name="3-1" @click="handleuserprocess" class="linka">How to start a diagnosis process?</a>
                <a class="linka" @click="handleusermatrix" name="3-2">How to check the device support matrix?</a>

        </Submenu>
    </Menu>
    </Sider>
    <div class="content">
      <h2>Before Installation</h2><br />
      <ul>
       <li style="margin-left: 50px">The script is based on Python3.6 or Python3.6+</li>
        <li style="margin-left: 50px">The pyusb package is needed, install it by the following command:
          <code>sudo pip3 install pyusb</code></li>
        <li style="margin-left: 50px">The distro package is needed, install it by the following command:
          <code>sudo pip3 install distro</code></li>
      </ul><br /><br />
      <h2>Cmdline Installation</h2><br />
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;Download HorizonPeripheralsClient Linux 64bits Installer 1.0 from Fling website or the home page of your web OVA server. </h4><br />
      <img style="width: 800px;height: 250px" src="../../assets/dj-client-install-linux1.png">
       <h4>&nbsp;&nbsp;&nbsp;&nbsp;Extract the zip file and run the following command in file path with root privilege or sudo.
         <code>sudo ./hpilinux_install.sh</code></h4><br />
      <img style="width: 800px;height: 250px" src="../../assets/dj-client-install-linux2.png">

    </div>
  </div>
</template>
<script>
    export default {
name:"InstallStepForLinux",
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
  handleclientlinux(){
    this.$router.replace("/stepforlinux");
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
  width: 380px;
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
