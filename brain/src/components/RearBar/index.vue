<template>
  <div class = "container">
      <Row type = "flex" justify="center" :gutter="40" style="padding:30px" >
          <Col :span="4">
            <h2>Prodict</h2>
            <p>111111</p>
             <p>111111</p>
              <p>111111</p>
          </Col>
          <Col span="4">
            <h2>Support</h2>
             <p>111111</p>
              <p>111111</p>
               <p>111111</p>

          </Col>
          <Col span="4">
          <h2>About us</h2>
           <p>111111</p>
            <p>111111</p>
             <p>111111</p>
          </Col>
      </Row>
      <Row justify="center">
          <Tag color = "black">© 2019 VMware, Inc</Tag>
           <Tag color = "primary">
               <Icon type="ios-mail" />
               <Icon type="md-cloudy" />
               <Icon type="logo-facebook" />
               <Icon type="logo-google" />
           </Tag>

        

          
      </Row>
  </div>
</template>

<script>
export default {
    name:"RearBar"
}
</script>

<style scoped>
.container{
    padding: 30px;
    text-align: center;
}
</style>
