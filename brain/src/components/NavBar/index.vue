<template>
  <div class="nav-bar">
    <Row type="flex" align="middle">
      <Col span="8">
        <div class="brand">
          <a href="https://www.vmware.com/cn.html">
            <img src="@/assets/vm-logo.png" alt="VMware" />
          </a>
        </div>
      </Col>
      <Col span="16">
        <div class="link-bar">
          <router-link to="/" class="link">
            <Icon type="ios-home" color="white" size="20" />
            <p>Home</p>
          </router-link>
          <router-link to="/Device-Matrix" class="link">
            <Icon type="md-analytics" color="white" size="20" />
            <p>Device Matrix</p>
          </router-link>
          <router-link to="/Log-in" class="link">
            <Icon type="md-log-in" color="white" size="20" />
            <p>Log in</p>
          </router-link>
          <router-link to="/test1" class="link">
            <Icon type="md-globe" color="white" size="20" />
            <p>Visit us</p>
          </router-link>
          <router-link to="/help" class="link">
            <Icon type="md-help-circle" color="white" size="20" />
            <p>Help</p>
          </router-link>
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
  /* margin: 1rem 1.5rem; */
  padding: 10px;
}
.nav-bar {
  padding: 0px 10px;
  background-image: url(../../assets/background.jpeg);
  border-bottom: 2px solid rgb(200, 241, 241);
  position: fixed; 
  width:100%;
  z-index:1;
  top:0;
  /* height:50px; */
}
.link-bar {
  color: white;
  display: flex;
  justify-content: flex-end;
   
}
.link-bar .link {
  /* display: inline; */
  color: white;
  font-size: 4px;
  text-align: center;
  height: 100%;
  /* merge border */
  border-bottom: 2px solid rgb(218, 241, 241);
  margin-bottom: -2px;
  padding: 1vw;
}

.link-bar .link:hover {
  border-bottom: 2px solid rgb(0, 174, 255);
}
</style>