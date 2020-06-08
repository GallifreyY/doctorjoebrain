<template>
  <Modal
    v-model="modalItem"
    @on-cancel="handleCancel"
    @on-ok="handleSubmit"
  >{{data.device_name}}</Modal>
</template>

<script>
export default {
  name: "DItem",
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
    return {};
  },
  methods: {
    handleCancel() {
      this.$emit("update:modalItem", false);
    },
    handleSubmit() {
      this.$emit("update:modalItem", false);
    }
  }
};
</script>

<style lang="" scoped>
</style>