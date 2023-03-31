<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column prop="id" label="ID" width="180" />
    <el-table-column prop="first_name" label="FIRST_NAME" />
    <el-table-column prop="second_name" label="SECOND_NAME" />
    <el-table-column prop="gender" label="GENDER" />
    <el-table-column prop="major" label="MAJOR" />

  </el-table>
</template>
<script>
import axios from "axios";
export default {
  mounted() {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/exp/stul/",
    }).then((res) => {
      this.tableData = res.data;
    });
  },
  data() {
    return {
      tableData: [],
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
