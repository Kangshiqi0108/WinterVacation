<template>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="id" label="ID" width="180" />
      <el-table-column prop="title" label="TITLE" />
      <el-table-column prop="author" label="AUTHOR" />
    </el-table>
  </template>
  <script>
  import axios from "axios";
  export default {
    mounted() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/exp/resr/",
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
  