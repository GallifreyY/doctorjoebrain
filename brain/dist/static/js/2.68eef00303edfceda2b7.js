webpackJsonp([2],{"2ivq":function(t,e){},"5oEE":function(t,e){},mRcU:function(t,e,a){"use strict";var n={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container"},[a("Row",{staticStyle:{padding:"30px"},attrs:{type:"flex",justify:"center",gutter:40}},[a("Col",{attrs:{span:4}},[a("h2",[t._v("Product")]),t._v(" "),a("p",[t._v("111111")]),t._v(" "),a("p",[t._v("111111")]),t._v(" "),a("p",[t._v("111111")])]),t._v(" "),a("Col",{attrs:{span:"4"}},[a("h2",[t._v("Support")]),t._v(" "),a("p",[t._v("111111")]),t._v(" "),a("p",[t._v("111111")]),t._v(" "),a("p",[t._v("111111")])]),t._v(" "),a("Col",{attrs:{span:"4"}},[a("h2",[t._v("About us")]),t._v(" "),a("p",[t._v("111111")]),t._v(" "),a("p",[t._v("111111")]),t._v(" "),a("p",[t._v("111111")])])],1),t._v(" "),a("Row",{attrs:{justify:"center"}},[a("Tag",{attrs:{color:"black"}},[t._v("© 2019 VMware, Inc")]),t._v(" "),a("Tag",{attrs:{color:"primary"}},[a("Icon",{attrs:{type:"ios-mail"}}),t._v(" "),a("Icon",{attrs:{type:"md-cloudy"}}),t._v(" "),a("Icon",{attrs:{type:"logo-facebook"}}),t._v(" "),a("Icon",{attrs:{type:"logo-google"}})],1)],1)],1)},staticRenderFns:[]};var r=a("VU/8")({name:"RearBar"},n,!1,function(t){a("rBOJ")},"data-v-2ef192af",null);e.a=r.exports},rBOJ:function(t,e){},uCMJ:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=a("Dd8w"),r=a.n(n),o=a("NYxO"),s={name:"",data:function(){return{loginForm:{userName:"",password:""}}},computed:r()({},Object(o.b)(["token"])),methods:{handleLogin:function(){var t=this;this.$store.dispatch("user/login",this.loginForm).then(function(){"false"==t.token?(t.$Message.error("The username or password is incorrect"),t.loginForm.userName="",t.loginForm.password=""):(t.$Message.success("Successfully Log in"),t.$router.push({path:"/"}))})}}},i={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"login-box"},[a("div",[a("span",[t._v("User Name:")]),t._v(" "),a("Input",{staticStyle:{width:"20vw"},attrs:{prefix:"ios-contact",clearable:"",placeholder:"Default: admin"},model:{value:t.loginForm.userName,callback:function(e){t.$set(t.loginForm,"userName",e)},expression:"loginForm.userName"}})],1),t._v(" "),a("div",[a("span",[t._v("Password:")]),t._v(" "),a("Input",{staticStyle:{width:"20vw"},attrs:{type:"password",placeholder:"Default:ca$hc0w"},model:{value:t.loginForm.password,callback:function(e){t.$set(t.loginForm,"password",e)},expression:"loginForm.password"}})],1),t._v(" "),a("div",{staticStyle:{"justify-content":"center"}},[a("Button",{attrs:{type:"primary",shape:"circle"},on:{click:t.handleLogin}},[t._v("Log In")])],1)])},staticRenderFns:[]};var c=a("VU/8")(s,i,!1,function(t){a("2ivq")},"data-v-03402c70",null).exports,l=a("XpZt"),v=a("mRcU"),u={name:"Login",components:{LoginBox:c,NavBar:l.a,RearBar:v.a},data:function(){return{}}},p={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"log-in"},[e("nav-bar"),this._v(" "),e("login-box")],1)},staticRenderFns:[]};var d=a("VU/8")(u,p,!1,function(t){a("5oEE")},"data-v-6197e945",null);e.default=d.exports}});
//# sourceMappingURL=2.68eef00303edfceda2b7.js.map