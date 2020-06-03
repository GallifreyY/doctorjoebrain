<template>
  <div class="layout">
    <Sider id="sider">
      <Menu hide-trigger theme="light" width="auto" open-names="['1','2']">
        <Submenu name="1">
          <template slot="title">
            <Icon type="md-analytics" size="20" />Matrix
          </template>
          <MenuItem name="1-1">All Devices</MenuItem>
          <MenuItem name="1-2">USB Disks</MenuItem>
          <MenuItem name="1-3">Printers</MenuItem>
          <MenuItem name="1-4">Scanners</MenuItem>
          <MenuItem name="1-5">Cameras</MenuItem>
          <MenuItem name="1-6">Other Devices</MenuItem>
        </Submenu>
        <Submenu name="2">
          <template slot="title">
            <Icon type="md-checkbox" size="20" />Check
          </template>
          <MenuItem name="2-1">Horizon Versions</MenuItem>
          <MenuItem name="2-2">Device Drivers</MenuItem>
        </Submenu>
        <MenuItem name="3">
          <Icon type="md-create" size="20" />Edit
        </MenuItem>
        <MenuItem name="4">
          <Icon type="md-contacts" size="20" />Contact us
        </MenuItem>
      </Menu>
    </Sider>
    <div class="content">
      <d-table></d-table>
    </div>
  </div>
</template>

<script>
import DTable from './components/DTable.vue'
export default {
  name: "Matrix",
  components:{DTable},
  data() {
    return {};
  }
};
</script>

<style lang="" scoped>


.content {
  margin-left: 15vw;
  margin-top: 75px;
  border: 1px solid red;
  height:100vh;
}
#sider {
  position: fixed;
  height: 80vh;
  width: 35vw;
  left: 0;
  /* overflow: auto; */
  top: 70px;
  background: #fff;
  z-index: 25;
}
</style>