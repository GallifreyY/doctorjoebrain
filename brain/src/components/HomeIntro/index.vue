<template>
  <div class="unit">
    <Row type="flex" align="center">
      <Col span="6">
        <img :src="'/static/icon/'+ picture" mode />
      </Col>
      <Col span="18" class="text">
        <Col span="24" class="title">{{title}}</Col>
        <Col span="24" class="content">{{content}}</Col>
      </Col>
    </Row>
  </div>
</template>

<script>
export default {
  name: "HomeIntro",
  props: {
    title: {
      type: String,
      default: "Title"
    },
    content: {
      type: String,
      default:
        "This is the description for the content in this unit. This is the description for the content in this unit. This is the description for the content in this unit. This is the description for the content in this unit. "
    },
    picture: {
      type: String,
      default: "printer.png"
    }
  },
  data() {
    return {};
  }
};
</script>

<style  scoped>
.unit {
  /* border: 2px solid white; */
  /* border-radius: 30%; */
  width: 35vw;
  height: 100%;
  /* background-color: black; */
  color: white;
  display: inline-block;
  margin: 1vw
}
.unit img {
  margin: 2vh;
  width: 80%;
}

.text {
  padding: 0.3rem;
  /* border: 1px solid white; */
}

.title {
  font-size: 1.5rem;
  font-weight: 400;
}
</style>