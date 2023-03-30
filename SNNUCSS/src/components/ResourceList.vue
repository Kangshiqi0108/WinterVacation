<script >
import axios from "axios";
import { Search } from "@element-plus/icons-vue";
export default {
  data() {
    return {
      tableData: [],
    };
  },
  method: {
    refresh() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/exp/relr/",
      }).then(function (response) {
        tableData = response.data;
      });
    },
  },
};
</script>
<template>
  <el-button :@click="refresh" icon="Search" circle  />
  <el-table :data="tableData" style="width: 100%">
    <el-table-column fixed prop="name" label="NAME" width="300" />
    <el-table-column prop="link" label="LINK" width="240" />
  </el-table>
</template>
<style scoped></style>
