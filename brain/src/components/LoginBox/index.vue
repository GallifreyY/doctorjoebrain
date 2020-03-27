<template>
  <div class="login-box">
    <div>
      <span>User Name:</span>
      <Input
        v-model="loginForm.userName"
        prefix="ios-contact"
        clearable
        placeholder="Default: admin"
        style="width: 20vw"
      />
    </div>
    <div>
      <span>Password:</span>
      <Input
        v-model="loginForm.password"
        type="password"
        placeholder="Default:ca$hc0w"
        style="width: 20vw"
      />
    </div>
    <div style="justify-content:center;">
      <Button type="primary" shape="circle" @click="handleLogin">Log In</Button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "",
  data() {
    return {
      loginForm: {
        userName: "",
        password: ""
      }
    };
  },
  computed: {
    ...mapGetters(["token"])
  },
  methods: {
    handleLogin() {
      this.$store.dispatch("user/login", this.loginForm).then(() => {
        if (this.token == "false") {
          this.$Message.error("The username or password is incorrect");
          this.loginForm.userName = ""
          this.loginForm.password = ""
        } else {
          this.$Message.success("Successfully Log in");
          this.$router.push({ path: "/" });
        }
      });
    }
  }
};
</script>

<style lang="" scoped>
.login-box {
  width: 30%;
  height: 30%;
  background-color: rgb(255, 255, 255);
  font-family: "Open Sans", serif;
  /* display:flex; */
  /* align-items: space-between; */
  padding: 3% 1% 1% 1%;
  box-shadow: 1px 1px 5px #ccc;
}
span {
  display: inline;
  font-size: 14px;
  vertical-align: middle;
  margin: auto 0;
}
.login-box > div {
  display: flex;
  justify-content: space-between;
  padding: 4% 3%;
}
</style>