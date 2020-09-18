<template>
  <div class="nav-bar">
    <Row type="flex" align="middle">
      <Col span="8">
        <div class="brand">
          <a href="https://www.vmware.com/cn.html">
            <img src="@/assets/vm-logo.png" alt="VMware"/>
          </a>
        </div>
      </Col>
      <Col span="16">
        <div class="link-bar">
          <router-link to="/" class="link">
            <Icon type="ios-home" color="white" size="20"/>
            <p>Home</p>
          </router-link>
          <router-link to="/Device-Matrix" class="link">
            <Icon type="md-analytics" color="white" size="20"/>
            <p>Device Matrix</p>
          </router-link>

          <a href="https://www.vmware.com/cn.html" class="link">
            <Icon type="md-globe" color="white" size="20"/>
            <p>Visit us</p>
          </a>
          <router-link to="/help" class="link">
            <Icon type="md-help-circle" color="white" size="20"/>
            <p>Help</p>
          </router-link>
        </div>
      </Col>
    </Row>
  </div>
</template>

<script>
  import {mapGetters} from "vuex";
  import axios from "axios";
  import {trsPassword} from "@/api/user";

  export default {
    name: "NavBar",
    data() {
      return {
        personal: false,
        personalLoading: false,
        //reportLink:""

      };
    },
    methods: {
      handleLogout() {
        this.personalLoading = true
        this.$store.dispatch("user/logout").then(() => {
          this.personal = false
          this.personalLoading = false
          this.$Message.success('Successfully Log out')
        }).catch(() => {
          this.personalLoading = false
          this.$Message.error('Something going wrong..')

        })
      },

      handleLogin() {
        trsPassword()
          .then(response => {
            var result = response.data['message']
            if (result > 0) {
              this.$router.replace("/Log-in")
            } else {
              this.$router.replace("/modify")
            }
          })
          .catch(error => {
            console.log(error);
            this.$Message.error("Sorry, there's something wrong with this this page");
          });
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
    background-image: url(../../assets/background.jpeg);
    background-size: 100%;
    background-repeat: no-repeat;
    border-bottom: 2px solid rgb(200, 241, 241);
    position: fixed;
    width: 97.6%;
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
