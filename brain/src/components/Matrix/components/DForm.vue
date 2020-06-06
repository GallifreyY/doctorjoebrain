<template>
  <Modal
    width="1000"
    okText="Submit"
    cancelText="Cancel"
    style="padding:0 3%"
    v-model="modalForm"
    @on-cancel="handleCancel"
    @on-ok="handleSubmit"
  >
    <Divider orientation="left" size="small" style="padding:2% 0 2% 0;">Device Information</Divider>
    <Form ref="formItem" :model="formItem" label-width="110" :rules="rulesV">
      <Row>
        <Col span="8">
          <FormItem label="VID" prop="vid">
            <Input v-model="formItem.vid" placeholder="Enter the VID.." />
          </FormItem>
        </Col>
        <Col span="8">
          <FormItem label="PID" prop="pid">
            <Input v-model="formItem.pid" placeholder="Enter the VID.." />
          </FormItem>
        </Col>
        <Col span="8">
          <FormItem label="Model">
            <Input v-model="formItem.model" placeholder="Enter the Model.." />
          </FormItem>
        </Col>
      </Row>

      <Row>
        <Col span="16">
          <FormItem label="Device Name" prop="name">
            <Input v-model="formItem.deviceName" placeholder="Enter the Device Name.." />
          </FormItem>
        </Col>
        <Col span="8">
          <FormItem label="Category">
            <Select v-model="formItem.category">
              <Option
                v-for="cate in ['USB Disks','Printers','Scanners','Cameras','Mics','Other Devices']"
                :key="cate"
                :value="cate"
              >{{cate}}</Option>
            </Select>
          </FormItem>
        </Col>
      </Row>

      <Divider
        orientation="left"
        size="small"
        style="padding:2% 0 2% 0;"
      >Horizon Compatibility Versions</Divider>

      <Row v-for="(item,index) in formItem.HorizonVersionsRes" v-if="item.status" :key="index">
        <Col span="8">
          <FormItem :label="'Client Version' + item.index" label-width="150">
            <Select v-model="item.client">
              <Option
                v-for="ver in HorizonVersionsList.client"
                :key="ver.value"
                :value="ver.value"
              >{{ver.label}}</Option>
            </Select>
          </FormItem>
        </Col>
        <Col span="8">
          <FormItem :label="'Agent Version' + item.index" label-width="150">
            <Select v-model="item.agent">
              <Option
                v-for="ver in HorizonVersionsList.agent"
                :key="ver.value"
                :value="ver.value"
              >{{ver.label}}</Option>
            </Select>
          </FormItem>
        </Col>
        <Col span="6" offset="2">
          <Button type="error" ghost @click="handleRemove(index)">Delete</Button>
        </Col>
      </Row>
      <FormItem label-width="150">
        <Row>
          <Col span="14">
            <Button type="dashed" long @click="handleAdd" icon="md-add">Add item</Button>
          </Col>
        </Row>
      </FormItem>

      <Divider
        orientation="left"
        size="small"
        style="padding:2% 0 2% 0;"
      >Driver Compatibility Versions</Divider>

      <FormItem label="Driver Name">
        <Input v-model="formItem.driver" placeholder="Enter the Driver Name.." />
      </FormItem>

      <FormItem label="OS Version">
        <CheckboxGroup v-model="formItem.OS">
          <Checkbox label="Windows 7"></Checkbox>
          <Checkbox label="Windows 10"></Checkbox>
          <Checkbox label="Windows 2016"></Checkbox>
          <Checkbox label="Windows 2019"></Checkbox>
        </CheckboxGroup>
      </FormItem>
    </Form>
  </Modal>
</template>

<script>
import { submitData } from "@/api/matrix";

export default {
  name: "DForm",
  inject:['reload'],
  props: {
    modalForm: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      index: 1,
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
      },
      rulesV: {
        vid: [
          { required: true, message: "VID cannot be empty", trigger: "blur" },
          {
            type: "string",
            max: 4,
            min: 4,
            message: "Incorrect VID format",
            trigger: "blur"
          }
        ],
        pid: [
          { required: true, message: "PID cannot be empty", trigger: "blur" },
          {
            type: "string",
            max: 4,
            min: 4,
            message: "Incorrect PID format",
            trigger: "blur"
          }
        ],
        name: [
          {
            required: true,
            message: "The device name cannot be empty",
            trigger: "blur"
          }
        ]
      }
    };
  },
  computed: {},
  methods: {
    init() {
      this.formItem = {
        vid: "",
        pid: "",
        model: null,
        deviceName: "",
        category: "",
        OS: [],
        driver: "",
        HorizonVersionsRes: [{ client: "", agent: "", index: 1, status: 1 }],
      };
    },
    formatResult() {},
    handleCancel() {
      //  this.modalForm = false;
      //  this.$emit('update:modalForm',this.modalForm)
      this.init();
      this.$emit("update:modalForm", false);
    },
    handleSubmit() {
      submitData(this.formItem)
        .then(() => {
          this.$Message.success("Submitted Successfully!");
          this.init();
          this.reload()
        })
        .catch(() => {
          this.$Message.error("Something going wrong... please try again");
        });
      this.$emit("update:modalForm", false);
    },
    handleAdd() {
      this.index++;
      this.formItem.HorizonVersionsRes.push({
        client: "",
        agent: "",
        index: this.index,
        status: 1
      });
    },
    handleRemove(index) {
      this.formItem.HorizonVersionsRes[index].status = 0;
    }
  },
  created() {
    this.init();
  }
};
</script>

<style lang="" scoped>
</style>