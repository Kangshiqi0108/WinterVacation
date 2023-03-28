<script>
import axios from 'axios'
import {
  Memo,
  Medal,
  School,
  Sunrise,
} from '@element-plus/icons-vue'
export default{
    data() {
        return {
        };
    },
    methods: {
        getList() {
            axios({
                method: "get",
                url: "http://127.0.0.1:8000/exp/"
            }).then(response => {
                list = response.data[0]["name"];
            });
        },
        handleOpen: (key, keyPath) => {
            console.log(key, keyPath);
        },
        handleClose: (key, keyPath) => {
            console.log(key, keyPath);
        },
    },
    components: { }
}


</script>


<template>
<div class="common-layout">
    <el-container>
      <el-header class="headertag">
        <img src="../img/logo.png" />
      </el-header>
      <el-container>
        <el-aside >
          <el-row class="tac">
    <el-col :span="17">
      <h5 class="mb-2">
          <br>
          <br>
          <p class="menutag">
            Site Menu
        </p>
      </h5>
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
      >
               <el-sub-menu index="1">
          <template #title>
            <el-icon><School /></el-icon>
            <span>Overview</span>
          </template>
          <el-menu-item-group title="Overview">
            <el-menu-item index="1-1">item one</el-menu-item>
            <el-menu-item index="1-2">item two</el-menu-item>
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          
        </el-sub-menu>
                <el-sub-menu index="2">
          <template #title>
            <el-icon><Sunrise /></el-icon>
            <span>Students</span>
          </template>
          <el-menu-item-group title="Students">
            <el-menu-item index="1-1">item one</el-menu-item>
            <el-menu-item index="1-2">item two</el-menu-item>
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          
        </el-sub-menu>
          <el-sub-menu index="3">
          <template #title>
            <el-icon><Medal /></el-icon>
            <span>Research Results</span>
          </template>
          <el-menu-item-group title="Research Results">
            <el-menu-item index="1-1">item one</el-menu-item>
            <el-menu-item index="1-2">item two</el-menu-item>
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          
        </el-sub-menu>
                <el-sub-menu index="4">
          <template #title>
            <el-icon><Memo /></el-icon>
            <span>Related Resources</span>
          </template>
          <el-menu-item-group title="Related Resources">
            <el-menu-item index="1-1">item one</el-menu-item>
            <el-menu-item index="1-2">item two</el-menu-item>
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          
        </el-sub-menu>
      </el-menu>
    </el-col>
    <el-col >
    </el-col>
  </el-row>
        </el-aside>
        <el-main>
          <div>
            <el-carousel :interval="4000" type="card" height="200px">
    <el-carousel-item v-for="item in 6" :key="item">
      <h3 text="2xl" justify="center">{{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
   
</template>

<style scoped>
.demo-image__placeholder .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 49%;
  box-sizing: border-box;
  vertical-align: top;
}
.demo-image__placeholder .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}
.demo-image__placeholder .el-image {
  padding: 0 5px;
  max-width: 300px;
  max-height: 200px;
}

.demo-image__placeholder.image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: var(--el-fill-color-light);
  color: var(--el-text-color-secondary);
  font-size: 14px;
}
.demo-image__placeholder .dot {
  animation: dot 2s infinite steps(3, start);
  overflow: hidden;
}
.menutag{
  font-size: large;
}
.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

</style>