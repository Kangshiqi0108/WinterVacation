<script>
import axios from 'axios'
export default{
  data(){
    return{
      msg:"Hello world",
      list:['hello','world',]
    }
  },
  methods:{
    getList(){
      axios(
        {
          method:'get',
          url:"http://127.0.0.1:8000/exp/"
        }
      ).then(
        response=>{
          list=response.data[0]['name']
        }
      )
    }
  },
  components:{
  },
}
</script>


<template>
  <p>{{ msg }}</p>
  <el-button type='primary' @click="getList">Click it</el-button>
  <li  v-for="lang in list">{{ lang }}</li>
</template>

<style scoped>
p {
  font-size: large;
}

</style>