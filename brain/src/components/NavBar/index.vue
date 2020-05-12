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
           <router-link :to="reportLink" class="link">
            <Icon type="md-podium" color="white" size="20" />
            <p>My report</p>
          </router-link>
          <router-link to="/Device-Matrix" class="link">
            <Icon type="md-analytics" color="white" size="20" />
            <p>Device Matrix</p>
          </router-link>

          <router-link v-if="token == 'false'" to="/Log-in" class="link">
            <Icon type="md-log-in" color="white" size="20" />
            <p>Log in</p>
          </router-link>
          <div v-else @click="personal=true" class="link">
            <Icon type="md-contact" color="white" size="20" />
            <p>{{name}}</p>
          </div>
          <!-- personal info -->
          <Modal v-model="personal" width="360">
            <p slot="header" style="color:rgb(0, 174, 255);text-align:center">
              <Icon type="ios-information-circle"></Icon>
              <span>Your Information</span>
            </p>
            <div style="text-align:center">
              <p>Username: {{name}}</p>
              <p>Permission: {{roles}}</p>
            </div>
            <div slot="footer">
              <Button type="error" size="large" long @click="handleLogout">Log out</Button>
            </div>
          </Modal>

          <a a href="https://www.vmware.com/cn.html" class="link">
            <Icon type="md-globe" color="white" size="20" />
            <p>Visit us</p>
          </a>
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
import { mapGetters } from "vuex";
export default {
  name: "NavBar",
  data() {
    return {
      personal:false,
      personalLoading:false,
      //reportLink:""

    };
  },
  computed: {
    ...mapGetters(["token", "name", "roles","uuid"]),
    reportLink:{
      get: function(){
        return '/diagnosis/'+this.uuid;
      }
    }
  },
  methods:{
    handleLogout(){
      this.personalLoading = true
      this.$store.dispatch("user/logout").then(() =>{
        this.personal = false
        this.personalLoading = false
        this.$Message.success('Successfully Log out')
      }).catch(()=>{
        this.personalLoading = false
        this.$Message.error('Something going wrong..')

      }) 
    }
  },


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
  background-size: 100%;
  background-repeat:no-repeat;
  border-bottom: 2px solid rgb(200, 241, 241);
  position: fixed;
  width: 100%;
  z-index: 30;
  top: 0;
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
  font-size: 0.8rem;
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