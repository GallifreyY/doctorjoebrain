<template>
    <div class="description-content">
       <Row>
        <Col span="12">
          <img class="screenshoot" src="../../assets/screenshoot.jpg">
        </Col>
        <Col span="12">
          <div class="description">
          <h3 style="color: white;margin-top: 20px">Horizon Peripherals Intelligence is an online diagnosis system for peripherals usage in Horizon environment. </h3>
          <h3 style="color: white;margin-top: 20px">Horizon Peripherals Intelligence is flexible and self-serviced. It can facilitate Horizon users and admins to detect and diagnose a wide range of peripherals issues and generate the device report in HTML format accordingly. </h3>
        </div>
        </Col>
    </Row>
<!--      <Divider orientation="left"  style="4eight: 2px;margin-top: 20px;background-color:#DCDCDC;color:#808080;font-size: 20px">Details</Divider>-->
<!--      <Tabs value="name1">-->
<!--        <TabPane label="HorizonPeripheralsAgent Installer Guide" name="name1">-->
<!--           <Row>-->
<!--        <Col span="12">-->
<!--          <div class="guide">-->
<!--            <h1><strong>HorizonPeripheralsAgent Installer Guide</strong></h1><br /><br />-->
<!--            <h2>installation</h2><br />-->
<!--            <h4>HorizonPeripheralsAgent.msi is the installer to be run on your Horizon agent machine. The web server address and port number need to be configured to the correct value firstly. If you don’t know the value, you can use the default one and change it after the installation by editing the config file.</h4><br />-->
<!--            <br /><br /><br /><br /><br /><br /><br /><br /><br />-->
<!--            <h4>There are 2 options in the following installer setup page – Custom and Complete Installations. To make full use of the installer capabilities, we suggest Complete installation with admin privilege.</h4>-->
<!--            <h4><strong>1.</strong>&nbsp;&nbsp;&nbsp;&nbsp;If you launch the installer with admin privilege, choose Complete option. The feature selection page will be skipped. Both features (filecopy and autolaunch) will be installed together. Change the installation directory if you want. By default, it is C:\HorizonPeripheralsAgent\ directory.</h4><br />-->
<!--            <h4>The HorizonPeripheralsAgent.exe will be auto launched after horizon client connects to a new remote desktop or app session.</h4><br />-->
<!--            <br /><br /><br /><br /><br /><br /><br />-->
<!--            <h4><strong>2.</strong>&nbsp;&nbsp;&nbsp;&nbsp;If you launch the installer with normal user privilege, choose the Custom option. There are two features in the custom setup page – Filecopy and Autolaunch. The Autolaunch feature is deselected by default. You can change the installation directory. By default, it is C:\HorizonPeripheralsAgent\ directory. </h4><br />-->
<!--            <h4>You   need   to   manually   click   the   HorizonPeripheralsAgent.exe   under   installation directory to launch it after successful installation.</h4><br />-->
<!--            <h4><strong>*</strong>&nbsp;&nbsp;&nbsp;Filecopy feature will copy all necessary files to the installation directory you choose.</h4><br />-->
<!--            <br /><br /><br /><br /><br /><br /><br /><br /><br /><br />-->
<!--            <h4><strong>*</strong>&nbsp;&nbsp;&nbsp;&nbsp;Autolaunch   feature   will   add   registry   entries   in   HKLM   path.   These registries make   HorizonPeripheralsAgent.exe   launch   automatically   whenever you freshly login a Horizon desktop or app session. The registries are –</h4>-->
<!--            <h4 style="font-style: italic">“HKLM\\Software\\VMware, Inc.\\VMware VDM\\UnityShell\\Run”</h4>-->
<!--            <h4 style="font-style: italic">“HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run”</h4>-->
<!--            <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />-->
<!--            <h2>After the installation</h2><br />-->
<!--            <h4>The hpagentconfig.ini under the installation folder contains the web server address and port which are configured during installation. If you don’t input them correctly during installation, you could manually change them by editing this config file.</h4>-->
<!--          </div>-->
<!--        </Col>-->
<!--              <Col span="12">-->
<!--          <img class="dj-installer-pic" src="../../assets/dj-agent-installer1.png">-->
<!--                <img class="dj-installer-pic" src="../../assets/dj-agent-installer2.png">-->
<!--                <img class="dj-installer-pic" src="../../assets/dj-agent-installer3.png">-->
<!--                <img class="dj-installer-pic" src="../../assets/dj-agent-installer4.png">-->
<!--                <img class="dj-installer-pic" src="../../assets/dj-agent-installer5.png">-->
<!--        </Col>-->
<!--    </Row>-->
<!--         <Button class="dj-installer-button" :size="buttonSize" icon="ios-download-outline" type="primary" @click="download_agent">Download HorizonPeripheralsAgent</Button>-->
<!--        </TabPane>-->
<!--        <TabPane label="HorizonPeripheralsClient Installer Guide" name="name2">-->
<!--           <Row>-->
<!--        <Col span="12">-->
<!--          <div class="guide">-->
<!--            <h1><strong>HorizonPeripheralsClient Installer Guide</strong></h1><br /><br />-->
<!--          <h4>HorizonPeripheralsClient.msi is the installer to be run on your Horizon client machine. It doesn’t require the administrator privilege to run.</h4><br />-->
<!--            <h4>You can choose the installation directory for HorizonPeripheralsClient. By default, it isC:\HorizonPeripheralsClient.</h4>-->
<!--        </div>-->
<!--        </Col>-->
<!--              <Col span="12">-->
<!--          <img class="dj-installer-pic" src="../../assets/dj-client-installer.png">-->
<!--        </Col>-->
<!--    </Row>-->
<!--          <Button class="dj-installer-button" :size="buttonSize" icon="ios-download-outline" type="primary"  @click="download_client">Download HorizonPeripheralsClient</Button>-->
<!--        </TabPane>-->
<!--    </Tabs>-->
    </div>
</template>

<script>
    export default {
        name: "descriptionContents",
         data () {
            return {
                buttonSize: 'large'
            }
        },
      methods:{
          download_client(){
            var url = 'https://'+window.location.host+'/download/HorizonPeripheralsClient.msi';
            window.open(url,'_blank');
          },
          download_agent(){
            var url = 'https://'+window.location.host+'/download/HorizonPeripheralsAgent.msi';
            window.open(url,'_blank');
          }
      }
    }
</script>

<style scoped>
.screenshoot{
  height:500px;
  width:500px;
  margin-left: 100px;
  margin-top: -50px;
}
  .description{
    margin-top: 10%;
  }
  .dj-installer-pic{
    height: 400px;
    width: 500px;
    margin-left: 100px;
  }
  h1{
    margin-top: -40px;
    margin-left: 20px;
  }
  h3,h2,h4{
    margin-left: 20px;
  }
.dj-installer-button{
  height:60px;
  width:350px;
  margin-left: 250px;
  margin-bottom: 50px;
}
  .description{
    width:520px;
    margin-left: 50px;
  }
  .guide{
    margin-top: 100px;
    margin-right: -30px;
  }

</style>
