<template>
  <Form ref="formCustom" :model="formCustom" :rules="ruleCustom"
        :label-width="80">
    <FormItem label="Password" prop="passwd">
      <Input type="password" v-model="formCustom.passwd"></Input>
    </FormItem>
    <FormItem label="Confirm" prop="passwdCheck">
      <Input type="password" v-model="formCustom.passwdCheck" name="password"></Input>
    </FormItem>
    <FormItem>
      <Button type="primary" @click="handleSubmit('formCustom')">Submit</Button>
      <Button @click="handleReset('formCustom')" style="margin-left: 58px">Reset</Button>
    </FormItem>
  </Form>
</template>
<script>
  import {modifyPassword} from "@/api/user";
  import qs from 'qs'
  import axios from 'axios';

  export default {
    data() {
      const validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please enter your password'));
        } else {
          if (this.formCustom.passwdCheck !== '') {
            // 对第二个密码框单独验证
            this.$refs.formCustom.validateField('passwdCheck');
          }
          callback();
        }
      };
      const validatePassCheck = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please enter your password again'));
        } else if (value !== this.formCustom.passwd) {
          callback(new Error('The two input passwords do not match!'));
        } else {
          callback();
        }
      };
      return {
        formCustom: {
          passwd: '',
          passwdCheck: ''
        },
        ruleCustom: {
          passwd: [
            {validator: validatePass, trigger: 'blur'}
          ],
          passwdCheck: [
            {validator: validatePassCheck, trigger: 'blur'}
          ],

        }
      }
    },
    methods: {
      trs_password(load) {
        const path = 'http://localhost:5000/reg';
        axios.post(path, load)
          .then(() => {
            console.log("success")
          })
          .catch((error) => {
            console.log(error);
          });
      },
      handleSubmit(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            this.$Message.success('Success!');
            this.$router.replace("/Log-in")
            const load = {
              password: this.formCustom.passwd,
            };
            this.trs_password(load)
            this.$http.post('/reg', data).then(res => {
              console.log(res)
            }, err => {
              console.log(err)// error callback
            });

          } else {
            this.$Message.error('Fail!');
          }

        })
      },
      handleReset(name) {
        this.$refs[name].resetFields();
      },
    }
  }
</script>
