<template>
  <div class="options">
   <Sider id="sider" style="overflow:scroll" width="380px">
       <Menu active-name="1-2" :open-names="['1']" width="380px">
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
                <MenuItem name="1-4">Web server configuration</MenuItem>
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
       <br /><h3>HorizonPeripheralsAgent.msi</h3><br />
      <h4>&nbsp;&nbsp;&nbsp;&nbsp;HorizonPeripheralsAgent.msi is the installer to be run on your Horizon agent machine. The web server address and port number need to be configured to the correct value firstly. If you don’t know the value, you can use the default one and change it after the installation by editing the config file – hpagentconfig.ini.</h4>

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
