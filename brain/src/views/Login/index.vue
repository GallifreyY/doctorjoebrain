<template>
    <div class = "log-in">
    <nav-bar></nav-bar>
        <login-box></login-box>


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
    display: flex;
    align-items: center;
    justify-content: center;

}

</style>
