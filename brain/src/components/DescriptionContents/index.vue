<template>
    <div class="description-content">
       <Row>
        <Col span="12">
          <img class="screenshoot" src="../../assets/screenshoot.png">
        </Col>
        <Col span="12">
          <div class="description">
          <h3 style="color: white;margin-top: 20px">{{$t("Horizon Peripherals Intelligence is an online diagnosis system for peripherals usage in Horizon environment. ")}}</h3>
          <h3 style="color: white;margin-top: 20px">{{$t("Horizon Peripherals Intelligence is flexible and self-serviced. It can facilitate Horizon users and admins to detect and diagnose a wide range of peripherals issues and generate the device report in HTML format accordingly. ")}}</h3>
        </div>
        </Col>
    </Row>
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
  width:570px;
  margin-left: 80px;
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
