<template>
  <Modal
    width="400"
    v-model="modalItem"
    ok-text="Submit"
    cancel-text="Cancel"
    @on-cancel="handleCancel"
    @on-ok="handleSubmit"
    :title="'Edit for the device: '+data.device_name"
  >
    <Form ref="formItem" :model="formItem" label-width="60">
      <Row>
        <Col span="8">
          <FormItem label="VID">
            <Input :placeholder="data.vendor_id" disabled />
          </FormItem>
        </Col>
        <Col span="8">
          <FormItem label="PID">
            <Input :placeholder="data.product_id" disabled />
          </FormItem>
        </Col>
        <Col span="8">
          <FormItem label="Model">
            <Input :placeholder="data.model" disabled />
          </FormItem>
        </Col>
      </Row>
      <FormItem label="Horizon Client Version" label-width="170">
        <Select
          v-model="formItem.Horizon_client_version"
          :placeholder="data.Horizon_client_version"
        >
          <Option
            v-for="ver in HorizonVersionsList.client"
            :key="ver.value"
            :value="ver.value"
          >{{ver.label}}</Option>
        </Select>
      </FormItem>

      <FormItem label="Horizon Agent Version" label-width="170">
        <Select v-model="formItem.Horizon_agent_version" :placeholder="data.Horizon_agent_version">
          <Option
            v-for="ver in HorizonVersionsList.agent"
            :key="ver.value"
            :value="ver.value"
          >{{ver.label}}</Option>
        </Select>
      </FormItem>
    </Form>
  </Modal>
</template>

<script>
import { editData } from "@/api/matrix";
export default {
  name: "DItem",
  inject: ["reload"],
  props: {
    modalItem: {
      type: Boolean,
      default: false
    },
    data: {
      type: Object
    }
  },
  data() {
    return {
      formItem: undefined,
      HorizonVersionsList: {
        client: [
          { label: "5.0.0", value: "5.0.0" },
          { label: "5.1.0", value: "5.1.0" },
          { label: "5.2.0", value: "5.2.0" },
          { label: "5.3.0", value: "5.3.0" },
          { label: "5.4.0", value: "5.4.0" }
        ],
        agent: [
          { label: "7.8.0", value: "7.8.0" },
          { label: "7.9.0", value: "7.9.0" },
          { label: "7.10.0", value: "7.10.0" },
          { label: "7.11.0", value: "7.11.0" },
          { label: "7.12.0", value: "7.12.0" }
        ]
      }
    };
  },
  methods: {
    handleCancel() {
      this.$emit("update:modalItem", false);
      this.init();
    },
    handleSubmit() {
      this.formItem.query = {
          vendor_id:this.data.vendor_id,
          product_id:this.data.product_id,
          model:this.data.model
        },
    
      editData(this.formItem)
        .then(response => {
          this.$Message.success("Successfully edited this item !");
          this.reload()
          
        })
        .catch(error => {
          this.$Message.error("Sorry, could not edit this item");
        });
      this.$emit("update:modalItem", false);
    },
    init() {
      this.formItem = {
        Horizon_client_version: "",
        Horizon_agent_version: "",
      };
    }
  },
  created() {
    this.init();
  }
};
</script>

<style lang="" scoped>
</style>