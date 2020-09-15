<template>
  <div class="options">
    <Sider id="sider" style="overflow:scroll" width="380px">
      <Menu active-name="1-2" :open-names="['1']" width="380px">
        <Submenu name="1">
          <template slot="title">
            <Icon type="ios-analytics"/>
            HorizonPeripheralsAgent Installer Guide
          </template>
          <MenuGroup title="Installation">
            <router-link to="/help" class="link">
              <MenuItem name="1-1">Step</MenuItem>
            </router-link>
            <router-link to="/options" class="link">
              <MenuItem name="1-2">Options</MenuItem>
            </router-link>
          </MenuGroup>
          <MenuGroup title="After the Installation">
            <router-link to="/tips" class="link">
              <MenuItem name="1-3">Tips</MenuItem>
            </router-link>
          </MenuGroup>
        </Submenu>
        <Submenu name="2">
          <template slot="title">
            <Icon type="ios-filing"/>
            HorizonPeripheralsClient Installer Guide
          </template>
          <router-link to="/step" class="link">
            <MenuItem name="2-1">Step</MenuItem>
          </router-link>
        </Submenu>

      </Menu>
    </Sider>
    <div class="content">
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;There are 2 options in the following installer setup page – Custom and Complete Installations. To make full
        use of the installer capabilities, we suggest Complete installation with admin privilege.</h4>
      <img class="dj-installer-pic" src="../../assets/dj-agent-installer2.png">
      <h4><strong>1.</strong>&nbsp;&nbsp;&nbsp;&nbsp;If you launch the installer with admin privilege, choose Complete
        option. The feature selection page will be skipped. Both features (filecopy and autolaunch) will be installed
        together. Change the installation directory if you want. By default, it is C:\HorizonPeripheralsAgent\
        directory.</h4>
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;The HorizonPeripheralsAgent.exe will be auto launched after horizon client connects to a new remote desktop or
        app session.</h4><br/>
      <h4><strong>2.</strong>&nbsp;&nbsp;&nbsp;&nbsp;If you launch the installer with normal user privilege, choose the
        Custom option. There are two features in the custom setup page – Filecopy and Autolaunch. The Autolaunch feature
        is deselected by default. You can change the installation directory. By default, it is
        C:\HorizonPeripheralsAgent\ directory. </h4>
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;You need to manually click the HorizonPeripheralsAgent.exe under installation directory to launch it after
        successful installation.</h4><br/>
      <img class="dj-installer-pic" src="../../assets/dj-agent-installer3.png">
      <h4><strong>*</strong>&nbsp;&nbsp;&nbsp;Filecopy feature will copy all necessary files to the installation
        directory you choose.</h4><br/>
      <h4><strong>*</strong>&nbsp;&nbsp;&nbsp;&nbsp;Autolaunch feature will add registry entries in HKLM path. These
        registries make HorizonPeripheralsAgent.exe launch automatically whenever you freshly login a Horizon desktop or
        app session. The registries are –</h4>
      <h4 style="font-style: italic">“HKLM\\Software\\VMware, Inc.\\VMware VDM\\UnityShell\\Run”</h4>
      <h4 style="font-style: italic">“HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run”</h4>
      <img class="dj-installer-pic1" src="../../assets/dj-agent-installer4.png">
    </div>
  </div>
</template>
<script>
  export default {
    name: "GuideOptions",

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
</style>
