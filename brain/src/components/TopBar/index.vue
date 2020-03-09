<template>
  <div class="topBar">
    <div class="header">
      <Row>
        <Col span="6">
        <div class = "brand">
          <a href="https://www.vmware.com/cn.html">
            <img src="@/assets/vm-logo.png" alt="VMware" />
          </a>
          </div>
        </Col>
        <Col span="18">
          <p>future nav bar</p>
        </Col>
      </Row>
    </div>
    <div class="content">
      <div class="titles">
        <h1 class="title">{{title}}</h1>
        <h2 class="subtitle">{{subtitle}}</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopBar",
  data() {
    return {
      title: "Peripheral devices Cloud Doctor",
      subtitle:
        "Online self diagnosis for Peripheral devices usages in Horizon environment."
    };
  }
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.topBar {
  background-image: url(../../assets/background.jpeg);
}

.titles {
  color: white;
  text-align: center;
  padding-bottom: 9rem;
  padding-top: 9rem;
}
.brand{
  margin-left: 1.5rem;
  /* padding-left: 1.5rem; */
  margin-top :1rem;
}

.title {
  font-size: 2rem;
  font-weight: 600;
  line-height: 1.125;
  margin-bottom: 1.5rem;
}
.subtitle {
  font-size: 1.25rem;
  font-weight: 400;
  line-height: 1.25;
}
</style>

