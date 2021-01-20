<template>
  <div class="more-info-menu">
    <div class="moreinfocontent">
  <Row>
    <Col span="24">
        <div style="height: 500px;overflow:scroll">
          <Table
                    stripe
                    :show-header="showHeader"
                    :columns="columns"
                    :data="clientDetail"
                    :size="tableSize"
                  ></Table>
                </div>
      </Col>
    </Row>
    </div>
    <br>
    </div>
</template>
<script>
 import { getBasicInfo} from "@/api/diagnosis";
 import {mapGetters} from "vuex";
    export default {
  name: "MoreInfoMenu",
  components: { },
  data() {
    return {

      clientDetail: undefined,
      columns: [
        { title: "Key", key: "key" },
        { title: "Value", key: "value" }
      ],
      showHeader: false, //tableHeader
      tableSize: "big"
    };
  },

  methods: {
    fetchBasicInfo(uuid) {
      getBasicInfo(uuid)
        .then(response => {
          this.clientDetail = response.data.basicInfo.clientDetail;
          this.$Loading.finish();

        })
        .catch(() => {
          this.$Loading.error();
          this.$Message.error(
            "Sorry, could not get your diagnosis information..."
          );
        });
    }
  },
  watch: {
    index: function() {
      this.$Message.success("Updated the diagnosis report for the device");
    }
  },

  computed: {
    ...mapGetters(["uuid"]),
  },
  created() {
    this.$store.commit("uuid/SET_UUID", this.$route.params.id);
    this.$Loading.start();
    this.fetchBasicInfo(this.uuid);
  }
};
</script>
<style>
  #sider {
  position: fixed;
  height: 90vh;
  width: 35vw;
  left: 0;
  /* overflow: auto; */
  background: #fff;
  z-index: 25;
}

</style>
