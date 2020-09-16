<template>
   <div class="step">
    <Sider id="sider" style="overflow:scroll" width="380px">
       <Menu active-name="1-3" :open-names="['1']" width="380px">
        <Submenu name="1">
            <template slot="title">
                <Icon type="ios-analytics" />
                HorizonPeripheralsAgent Installer Guide
            </template>

               <router-link to="/help" class="link">
                <MenuItem name="1-1">HorizonPeripheralsAgent.zip</MenuItem>
               </router-link>
              <router-link to="/options" class="link">
                <MenuItem name="1-2">HorizonPeripheralsAgent.msi</MenuItem>
              </router-link>
              <router-link to="/installstep" class="link">
                <MenuItem name="1-3">Installation steps</MenuItem>
              </router-link>

              <router-link to="/tips" class="link">
                <MenuItem name="1-4">Installation failure and modification</MenuItem>
              </router-link>

        </Submenu>
        <Submenu name="2">
            <template slot="title">
                <Icon type="ios-filing" />
                HorizonPeripheralsClient Installer Guide
            </template>
          <router-link to="/step" class="link">
            <MenuItem name="2-1">Installation steps</MenuItem>
          </router-link>
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
   .link{
    color: black;
  }
  .link:hover{
    color: #0F1D38;
  }
</style>
