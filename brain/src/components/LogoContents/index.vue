<template>
  <div class="logo-contents">
    <div class="install-content">
      <Row>
        <Col span="12">
          <div class="djclient-install">
            <Button class="dj-client-button" @click="download_client">
              <Row>
              <Col span="8"><img class="diagnose-logo" src="../../assets/diagnoselogo-c.jpg">
              </Col>
              <Col span="16">
                <div class="dj-install-des">
                <h1>Download</h1>
                <h2>DJClient installer</h2>
                <p>If you want more information of this product and the guide of installation,please scroll down and see details!</p>
              </div>
              </Col>
            </Row>
            </Button>
          </div>
        </Col>
        <Col span="12"><div class="djagent-install">
         <Button class="dj-agent-button"  @click="download_agent">
            <Row>
              <Col span="8"><img class="diagnose-logo" src="../../assets/diagnoselogo-a.jpg">
              </Col>
              <Col span="16">
                <div class="dj-install-des">
                <h1>Download</h1>
                <h2>DJAgent installer</h2>
                <p>If you want more information of this product and the guide of installation,please scroll down and see details!</p>
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
                buttonSize: 'large'
            }
        },
     methods: {
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
  margin-right: 20px;
}
  .install-content{
    width:1000px;
    height:120px;
    margin:auto;
    margin-top: 20px;

  }
  .dj-agent-button{
    width:450px;
    height: 170px;
    float: right;
    background-color: 	#E1FFFF;
    border: 2px solid 	#4682B4;
    border-radius: 10px;
  }
    .dj-client-button{
    width:450px;
    height: 170px;
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
  }
  h2{
    margin-left: 10px;
  }
  .dj-install-des{
    margin-left: -20px;
  }
</style>
