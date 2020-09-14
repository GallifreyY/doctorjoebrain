<template>
   <div class="step">
    <Sider id="sider" style="overflow:scroll" width="380px">
       <Menu active-name="2-1" :open-names="['2']" width="380px">
        <Submenu name="1">
            <template slot="title">
                <Icon type="ios-analytics" />
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
                <Icon type="ios-filing" />
                HorizonPeripheralsClient Installer Guide
            </template>
          <router-link to="/step" class="link">
            <MenuItem name="2-1">Step</MenuItem>
          </router-link>
        </Submenu>

    </Menu>
    </Sider>
    <div class="content">
      <h4>&nbsp;&nbsp;&nbsp;HorizonPeripheralsClient.msi is the installer to be run on your Horizon client machine. It doesn’t require the administrator privilege to run.</h4><br />
            <h4>&nbsp;&nbsp;&nbsp;You can choose the installation directory for HorizonPeripheralsClient. By default, it isC:\HorizonPeripheralsClient.</h4>
        <img class="dj-installer-pic" src="../../assets/dj-client-installer.png">
    </div>
  </div>
</template>
<script>
    export default {
name:"GuideStep",

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
