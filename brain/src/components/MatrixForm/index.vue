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

        <FormItem
          v-for="(index,item) in clientDriverList"
          v-if="item.status"
          :key="item.index"
          :label="'Client Driver' + index"
        >
          <Row>
            <Col span="18">
              <Input
                type="text"
                v-model="item.value"
                placeholder="Enter the name of supported driver..."
              ></Input>
            </Col>
            <Col span="4" offset="1">
              <Button @click="handleRemove(index)">Delete</Button>
            </Col>
          </Row>
        </FormItem>

        <Row type="flex" align="center">
          <Col
            span="6"
            style="text-align:center; height:30px;line-height:30px"
          >Horizon Client Versions</Col>
          <Col span="18">
            <Select multiple v-model="formItem.HorizonVersionsRes">
              <Option
                v-for="item in HorizonVersionsList"
                :key="item.value"
                :value="item.value"
              >{{item.label}}</Option>
            </Select>
          </Col>
        </Row>
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
        clientOS: [],
        agentOS: [],
        HorizonVersionsRes: [],
        clientDriverRes: [],
        agentDriverRes: []
      },

      HorizonVersionsList: [
        { label: "6.3", value: "6.3" },
        { label: "6.4", value: "6.4" },
        { label: "6.5", value: "6.5" },
        { label: "6.8", value: "6.8" },
        { label: "6.9", value: "6.9" },
        { label: "7.1", value: "7.1" }
      ],

      clientDriverList: [{ value: "", index: 1, status: true }],
      agentDriverList: []
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