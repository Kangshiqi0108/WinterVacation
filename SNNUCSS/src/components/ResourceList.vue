<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column prop="name" label="NAME" width="180" />
    <el-table-column prop="link" label="LINK" />
  </el-table>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      tableData:axios({
        method: "get",
        url: "http://127.0.0.1:8000/exp/relr/",
      }).data
      /*{ name: 'SNNU_MAIN_SITE',
    link: 'https://www.snnu.edu.cn/',
  },
  {
    name: 'BLACK_BOARD_SNNU',
    link: 'https://bb.snnu.edu.cn/',
  },*/
    };
  },
};
</script>
