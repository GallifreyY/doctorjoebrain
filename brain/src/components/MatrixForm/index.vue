<template>
  <div v-if="showForm">
    <Card>
      <p slot="title">Update the Device Matrix</p>
      <Button slot="extra" @click="cancel">Cancel</Button>
      <Button slot="extra" @click="submit">Submit</Button>
      <Form ref :model="formItem" label-width="100" inline>
        <FormItem label="VID">
          <Input v-model="formItem.vid" placeholder="Enter the VID.." />
        </FormItem>
        <FormItem label="PID">
          <Input v-model="formItem.pid" placeholder="Enter the PID..." />
        </FormItem>
      </Form>
      <Form ref :model="formItem" label-width="100">
        <FormItem label="Model">
          <Input
            v-model="formItem.model"
            placeholder="If you do not know about it, please skip it..."
          />
        </FormItem>
        <FormItem label="Device Name">
          <Input v-model="formItem.deviceName" placeholder="Enter the Device Name.." />
        </FormItem>
        <FormItem label="Client OS">
          <CheckboxGroup v-model="formItem.clientOS">
            <Checkbox label="Windows 7"></Checkbox>
            <Checkbox label="Windows 10"></Checkbox>
            <Checkbox label="Windows 2016"></Checkbox>
            <Checkbox label="Windows 2019"></Checkbox>
          </CheckboxGroup>
        </FormItem>
                <FormItem label="Agent OS">
          <CheckboxGroup v-model="formItem.agentOS">
            <Checkbox label="Windows 7"></Checkbox>
            <Checkbox label="Windows 10"></Checkbox>
            <Checkbox label="Windows 2016"></Checkbox>
            <Checkbox label="Windows 2019"></Checkbox>
          </CheckboxGroup>
        </FormItem>
        

      </Form>
    </Card>
  </div>
</template>

<script>
export default {
  name: "MatrixForm",
  props: {
    showForm: {
      type: Boolean
    }
  },
  data() {
    return {
      formItem: {
        vid: "",
        pid: "",
        model: null,
        deviceName: "",
        category: "",
        clientOS:[],
        agentOS:[],
      }
    };
  },
  methods: {
    cancel() {
      this.showForm = false;
      this.formItem = {
        deviceName: ""
      };
    },
    submit() {
      this.showForm = false;
      this.$Message.success("Submitted successfully!");
    }
  }
};
</script>

<style lang="" scoped>
</style>