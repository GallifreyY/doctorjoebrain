<template>
    <div class="home-footer">
      <Row>
        <Col span="8">
          <h1 class="des">DJIntelligence</h1>
          <h3 class="info">About Us</h3>
          <h3 class="info">Visit Us</h3>
          <h3 class="info">Design Guide</h3>
        </Col>
        <Col span="8">
          <h1 class="legal">Legal</h1>
          <h3 class="linfo">Privacy Policy</h3>
          <h3 class="linfo">Terms&Conditions</h3>
        </Col>
        <Col span="8">
            <h1 class="contact">Contact</h1>
          <h3 class="cinfo">China</h3>
          <Icon class="cinfo" type="logo-facebook" />
          <Icon class="iinfo" type="logo-twitter" />
          <Icon class="iinfo" type="logo-googleplus" />
        </Col>
    </Row>
      <Divider />
    </div>
</template>

<script>
    export default {
        name: "homefooter"
    }
</script>

<style scoped>
.home-footer{
  background-color: #696969;
  height: 300px;
  }
  .des{
    color: #F5F5F5;
    margin-left: 100px;
    margin-top: 50px;
  }
  .info{
    color: #F5F5F5;
    margin-left: 100px;
    margin-top: 10px;
  }
  .legal{
    color: #F5F5F5;
    margin-left: 150px;
    margin-top: 50px;
  }
  .linfo{
    color: #F5F5F5;
    margin-left: 150px;
    margin-top: 10px;
  }
  .contact{
    color: #F5F5F5;
    margin-left: 100px;
    margin-top: 50px;
  }
  .cinfo {
    color: #F5F5F5;
    margin-left: 100px;
    margin-top: 10px;
  }
    .iinfo {
    color: #F5F5F5;
    margin-left: 10px;
    margin-top: 10px;
  }

</style>
