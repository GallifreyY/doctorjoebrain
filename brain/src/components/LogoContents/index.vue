<template>
  <div class="logo-contents">
    <div class="install-content">
      <Row>
        <Col span="12">
          <div class="djclient-install">
            <Button class="dj-client-button" @click="download_client">
              <Row>
              <Col span="8"><img class="diagnose-logo" src="../../assets/logo.png">
              </Col>
              <Col span="16">
                <div class="dj-install-des">
                <h1>{{$t("Download")}}</h1>
                <h2>{{$t("HorizonPeripheralsClient Windows")}}</h2>
                <h2>{{$t("64bits Installer")}} {{version}}</h2>
                </div>
              </Col>
            </Row>
            </Button>
          </div>
        </Col>
        <Col span="12"><div class="djagent-install">
         <Button class="dj-agent-button"  @click="download_agent">
            <Row>
              <Col span="8"><img class="diagnose-logo" src="../../assets/logo.png">
              </Col>
              <Col span="16">
                <div class="dj-install-des">
                <h1>{{$t("Download")}}</h1>
                <h2>{{$t("HorizonPeripheralsAgent Windows")}}</h2>
                <h2>{{$t("64bits Installer")}} {{version}}</h2>
               </div>
              </Col>
            </Row>
          </Button>
        </div>
        </Col>
      </Row>
    </div>

    <div class="install-content">
      <Row>
        <Col span="12">
          <div class="djclient-install">
            <Button class="dj-client-button" @click="download32_client">
              <Row>
              <Col span="8"><img class="diagnose-logo" src="../../assets/logo.png">
              </Col>
              <Col span="16">
                <div class="dj-install-des">
                <h1>{{$t("Download")}}</h1>
                <h2>{{$t("HorizonPeripheralsClient Windows")}}</h2>
                <h2>{{$t("32bits Installer")}} {{version}}</h2>
                </div>
              </Col>
            </Row>
            </Button>
          </div>
        </Col>
        <Col span="12"><div class="djagent-install">
         <Button class="dj-agent-button"  @click="download32_agent">
            <Row>
              <Col span="8"><img class="diagnose-logo" src="../../assets/logo.png">
              </Col>
              <Col span="16">
                <div class="dj-install-des">
                <h1>{{$t("Download")}}</h1>
                <h2>{{$t("HorizonPeripheralsAgent Windows")}}</h2>
                <h2>{{$t("32bits Installer")}} {{version}}</h2>
               </div>
              </Col>
            </Row>
          </Button>
        </div>
        </Col>
      </Row>
    </div>

    <div class="install-content">
      <Row>
        <Col span="12">
          <div class="djclient-install">
            <Button class="dj-client-button" @click="download_client_linux">
              <Row>
              <Col span="8"><img class="diagnose-logo" src="../../assets/logo.png">
              </Col>
              <Col span="16">
                <div class="dj-install-des">
                <h1>{{$t("Download")}}</h1>
                <h2>{{$t("HorizonPeripheralsClient Linux")}}</h2>
                <h2>{{$t("64bits Installer")}} {{version}}</h2>
                </div>
              </Col>
            </Row>
            </Button>
          </div>
        </Col>
        <Col span="12"><div class="djagent-install">
         <Button class="dj-agent-button"  @click="download_agent_wpf">
            <Row>
              <Col span="8"><img class="diagnose-logo" src="../../assets/logo.png">
              </Col>
              <Col span="16">
                <div class="dj-install-des">
                <h1>{{$t("Download")}}</h1>
                <h2>{{$t("HorizonPeripheralsAgent WPF")}}</h2>
                <h2>{{$t("Windows 64bits Installer")}} {{version}}</h2>
               </div>
              </Col>
            </Row>
          </Button>
        </div>
        </Col>
        </Row>
        </div>

      <div class="install-content">
      <Row>
        <Col span="24">
          <div class="djagent-install">
            <Button class="dj-agent-button" @click="download_agent_mvvm">
              <Row>
              <Col span="8"><img class="diagnose-logo" src="../../assets/logo.png">
              </Col>
              <Col span="16">
                <div class="dj-install-des">
                <h1>{{$t("Download")}}</h1>
                <h2>{{$t("HorizonPeripheralsAgent MVVM")}}</h2>
                <h2>{{$t("64bits Installer")}} {{version}}</h2>
                </div>
              </Col>
            </Row>
            </Button>
          </div>
        </Col>
        </Row>
        </div>

  </div>


</template>

<script>
  export default {
    name: "logocontents",
     data () {
            return {
                buttonSize: 'large',
                version: '2.0'
            }
        },
     methods: {
      download_client(){
            var url = 'https://'+window.location.host+'/download/HorizonPeripheralsClient_Win64.msi';
            window.open(url,'_blank');
          },
          download_agent(){
            var url = 'https://'+window.location.host+'/download/HorizonPeripheralsAgent_Win64.zip';
            window.open(url,'_blank');
          },
          download32_client(){
            var url = 'https://'+window.location.host+'/download/32bits/HorizonPeripheralsClient_Win32.msi';
            window.open(url,'_blank');
          },
          download32_agent(){
            var url = 'https://'+window.location.host+'/download/32bits/HorizonPeripheralsAgent_Win32.zip';
            window.open(url,'_blank');
          },
          download_client_linux(){
            var url = 'https://'+window.location.host+'/download/linux/HorizonPeripheralsClient_Lin64.zip';
            window.open(url,'_blank');
          },
          download_agent_wpf(){
            var url = 'https://'+window.location.host+'/download/HorizonPeripheralsAgent_Win64.msi';
            window.open(url,'_blank');
          },
          download_agent_mvvm(){
            var url = 'https://'+window.location.host+'/download/HorizonPeripheralsAgent.mvvm_Win64.msi';
            window.open(url,'_blank');
          }
     }
  }
</script>

<style scoped>
  /*.logo-contents{*/
  /*  background:url("../../assets/logobk.jpg") no-repeat 0 -118px;*/
  /*  height: 60%;*/
  /*  width: 100%;*/
  /*  background-size:100% 100%;*/
  /*}*/
.diagnose-logo{
  width: 80px;
  height: 80px;
  margin-top: 20px;
  margin-right: 50px;
}
  .install-content{
    width:1100px;
    height:120px;
    margin:auto;
    margin-top: 20px;

  }
  .dj-agent-button{
    width:500px;
    height: 130px;
    float: right;
    background-color: 	#E1FFFF;
    border: 2px solid 	#4682B4;
    border-radius: 10px;
  }
    .dj-client-button{
    width:500px;
    height: 130px;
      background-color: #FFFFF0;
    border: 2px solid 	#EEE8AA;
    border-radius: 10px;
  }
  h1{
    margin-bottom: 10px;
  }
  p{
    white-space:normal;
    width:300px;
    margin-left: 25px;
  }
  h2{
    margin-left:5px;
  }
  .dj-install-des{
    margin-left: -40px;
  }
</style>
