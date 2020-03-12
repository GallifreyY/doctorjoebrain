<template>
  <div class="nav-bar">
    <Row type="flex" justify="space-between" align="middle">
      <Col span="8">
        <div class="brand">
          <a href="https://www.vmware.com/cn.html">
            <img src="@/assets/vm-logo.png" alt="VMware" />
          </a>
        </div>
      </Col>
      <Col span="5">
        <div class="link-bar">
          <a href>
            <Icon type="ios-home" color="white" size="20" />
            <p>Home</p>
          </a>

          <a href>
            <Icon type="md-analytics" color="white" size="20" />
            <p>Device Matrix</p>
          </a>
           <a href>
            <Icon type="md-log-in" color="white" size="20" />
            <p>Log in</p>
          </a>
          <a href>
            <Icon type="md-globe" color="white" size="20" />
            <p>Visit us</p>
          </a>

          <a href>
            <Icon type="md-help-circle" color="white" size="20" />
            <p>Help</p>
          </a>
        </div>
      </Col>
    </Row>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {};
  }
};
</script>

<style lang="" scoped>
.brand {
  margin: 1rem 1.5rem;
}
.nav-bar {
  padding: 0px 10px;
  background-image: url(../../assets/background.jpeg);
}
.link-bar {
  color: white;
  display: flex;
  justify-content: space-around;
}
a {
  /* display: inline; */
  color: white;
  font-size: 4px;
  text-align: center;
}


</style>