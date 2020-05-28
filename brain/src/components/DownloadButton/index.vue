<template>
  <a >
    <div class="button" >
        <img :src=pic alt="">
        <p>Download DoctorJoe</p>
    </div>
  </a>
</template>

<script>
export default {
  name: "DownloadButton",
  props: {
    name: {
      type: String,
      default: "Name"
    },
    pic: {
      type: String,
      default: "/static/icon/down.png"
    }
  },
  data() {
    return {};
  }
};
</script>

<style  scoped>
.button {
  border-radius: 50%;
  width: 60px;
  height: 60px;
  border: 2px solid white;
  position: fixed;
  top:90vh;
  left:85vw;
  text-align: center;
}
.button p{
    display:none;
    color:white;
    line-height: 60px;
    vertical-align: middle;
    /* margin-top: -25px ; */
    font-size: 16px;
    

}

a :hover{
    width: 200px;
    height: 60px;
    border-radius: 8px;
}
a :hover img{
    display: none;
}

a :hover p {
   display: block; 
}

a :active {
    background-color: white;
     color:black;
    
    
} 

img{
    width: 40px;
    height : 40px;
    margin :8px;  /*减去border*/  
}

</style>