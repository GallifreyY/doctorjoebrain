<template>
   <div class="tips">
   <Sider id="sider" style="overflow:scroll" width="380px">
       <Menu active-name="1-4" :open-names="['1']" width="380px">
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
       <h4>&nbsp;&nbsp;&nbsp;The hpagentconfig.ini under the installation folder contains the web server address and port which are configured during installation. If you don’t input them correctly during installation, you could manually change them by editing this config file.</h4>
      <img class="dj-installer-pic" src="../../assets/dj-agent-installer5.png">
    </div>
  </div>
</template>
<script>
    export default {
name:"GuideTips",

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
