<template>
  <div v-if="showForm">
    <Card>
      <p slot="title">Update the Device Matrix</p>
      <Button slot="extra" @click="cancel"> Cancel</Button>
      <Button slot="extra" @click="submit"> Submit</Button>
      <Form ref :model="formItem" label-width="100">
        <FormItem label="Device Name">
          <Input v-model="formItem.deviceName" placeholder="Enter the Device Name.." />
        </FormItem>
      </Form>
    </Card>
  </div>
</template>

<script>
export default {
  name: "MatrixForm",
  props:{
    showForm:{
        type:Boolean
    }
  },
  data() {
    return {
      formItem: {
        deviceName: "",
      }
    };
  },
  methods:{
    cancel(){
        this.showForm=false;
        this.formItem= {
            deviceName: "",
        }
    },
    submit(){
        this.showForm=false;
        this.$Message.success("Submitted successfully!")

    }
  }
};
</script>

<style lang="" scoped>
</style>