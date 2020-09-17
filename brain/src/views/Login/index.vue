<template>
    <div class = "log-in">
    <nav-bar style="margin-left: 15px"></nav-bar>
        <login-box style="position: absolute;top: 0;left: 0;right: 0;bottom: 0;margin: auto"></login-box>


    </div>
</template>

<script>
import LoginBox from "@/components/LoginBox";
import NavBar from "@/components/NavBar";
import RearBar from "@/components/RearBar";
    export default {
        name: 'Login',
        components:{LoginBox, NavBar,RearBar},
        data() {
            return {

            }
        }
    }
</script>


<style lang="" scoped>

.log-in{
    height: 100vh;

    background: url(../../assets/background.jpeg);
  position: relative;
    /*display: flex;*/
    /*align-items: center;*/
    /*justify-content: center;*/

}

</style>
