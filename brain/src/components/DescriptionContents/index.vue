<template>
    <div class="description-content">
       <Row>
        <Col span="12">
          <img class="screenshoot" src="../../assets/screenshoot.jpg">
        </Col>
        <Col span="12">
          <div class="description">
          <h2>DoctorJoe 1.0.1: Device intelligence diagnosis service for VMware Horizon</h2><br /><br />
          <h5>DoctorJoe is a self diagnosis system for peripheral devices usages in Horizon environment. DoctorJoe is flexible: configure and arrange the user interface to support a wide range of peripheral devices.</h5>
        </div>
        </Col>
    </Row>
      <Divider orientation="left"  style="height: 2px;margin-top: 20px;background-color:#DCDCDC;color:#808080;font-size: 20px">Details</Divider>
      <Tabs value="name1">
        <TabPane label="DJAgent Installer Guide" name="name1">
           <Row>
        <Col span="12">
          <div class="guide">
          <h1>DJAgent Installer Guide</h1><br />
            <h4>DoctorJoeAgent.msi is the installer to be run on your Horizon agent machine. There are 3 options in the installer setup page – Typical/Custom/Complete. Tomake full use of the installer capabilities, we suggest you launch the installerwith administrator privilege.</h4>
            <h4><strong>1.</strong>&nbsp;&nbsp;&nbsp;&nbsp;If you launch the installer with administrator privilege, choose either Typical or Complete option. Both are ok. The components selection page will be skipped. The Filecopy and Autolaunch components will be installed by default. Change the installation directory if you want. By default, it is C:\DoctorJoeAgent\ directory.</h4><br />
            <h4>The DoctorJoeAgent.exe will be auto launched after horizon client connects to a new remote desktop or app session.</h4><br />
            <br /><br /><br /><br /><br /><br /><br />
            <h4><strong>2.</strong>&nbsp;&nbsp;&nbsp;&nbsp;If you launch the installer with ordinary user privilege, choose the Custom option. There are two components in the custom setup page – Filecopy and Autolaunch. Deselect the Autolaunch component. Click the Filecopy component, if you want to change the installation directory. By default, it is C:\DoctorJoeAgent\ directory. </h4><br />
            <h4>You   need   to   manually   click   the   DoctorJoeAgent.exe   under   installationdirectory to launch it after successful installation.</h4><br />
            <h4><strong>*</strong>&nbsp;&nbsp;&nbsp;Filecopy feature will copy all necessary files to the installation directoryyou choose.</h4><br />
            <br /><br /><br /><br /><br /><br />
            <h4><strong>*</strong>&nbsp;&nbsp;&nbsp;&nbsp;Autolaunch   feature   will   add   registry   entries   in   HKLM   path.   Theseregistries   make   DoctorJoeAgent.exe   launch   automatically   wheneveryou freshly login a Horizon desktop or app session. The registries are –“HKLM\\Software\\VMware, Inc.\\VMware VDM\\UnityShell\\Run”“HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run”</h4><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
            <h2>After the installation</h2><br />
            <h4>Djagentconfig.ini under the installation folder contains the default web server address and port. Do not change them unless instructed by your administrator. They should be configured to the real FQDN of the web OVAserver and web port listening on that server.</h4>
          </div>
        </Col>
              <Col span="12">
          <img class="dj-installer-pic" src="../../assets/dj-agent-installer1.png">
                <img class="dj-installer-pic" src="../../assets/dj-agent-installer2.png">
                <img class="dj-installer-pic" src="../../assets/dj-agent-installer4.png">
                <img class="dj-installer-pic" src="../../assets/dj-agent-installer3.png">
        </Col>
    </Row>
         <Button class="dj-installer-button" :size="buttonSize" icon="ios-download-outline" type="primary" @click="download_agent">Download DJAgent</Button>
        </TabPane>
        <TabPane label="DJClient Installer Guide" name="name2">
           <Row>
        <Col span="12">
          <div class="guide">
          <h1>DJClient Installer Guide</h1><br /><br />
          <h4>DoctorJoeClient.msi is the installer to be run on your Horizon client machine. It doesn’t require the administrator privilege to run.</h4><br />
            <h4>You can choose the installation directory for DoctorJoeClient. By default, it isC:\DoctorJoeClient.</h4>
        </div>
        </Col>
              <Col span="12">
          <img class="dj-installer-pic" src="../../assets/dj-client-installer.png">
        </Col>
    </Row>
          <Button class="dj-installer-button" :size="buttonSize" icon="ios-download-outline" type="primary"  @click="download_client">Download DJClient</Button>
        </TabPane>
    </Tabs>
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
            var url = 'https://'+window.location.host+'/download/DoctorJoe%20Client.msi';
            window.open(url,'_blank');
          },
          download_agent(){
            var url = 'https://'+window.location.host+'/download/DoctorJoe%20Agent.msi';
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
  margin-top: 50px;
}
  .description{
    margin-top: 30%;
  }
  .dj-installer-pic{
    height: 400px;
    width: 500px;
    margin-left: 100px;
  }
  h1{
    margin-top: -40px;
    margin-left: 100px;
  }
  h3,h2,h4{
    margin-left: 20px;
  }
.dj-installer-button{
  height:60px;
  width:200px;
  margin-left: 250px;
  margin-bottom: 50px;
}
  .description{
    width:400px;
    margin-left: 50px;
  }
  .guide{
    margin-top: 100px;
  }

</style>
