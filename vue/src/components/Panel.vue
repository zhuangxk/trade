<template>
  <div class="pannel">
    <h1>
      <span style="margin-right: 2em">
         当前索引：{{index}}
      </span>
      <span>
         当前剩余：{{total - index}}
      </span>
    </h1>

    <el-form label-position="left">
      <el-form-item >
        <el-input v-model="value" placeholder="请输入一个数字"></el-input>
      </el-form-item>
      <div>
        随机间隔时间: 
      </div>
      <el-form-item >
          <el-slider
            v-model="range"
            range
            :marks="marks"
            show-stops
            :max="10">
          </el-slider>
      </el-form-item>
      <el-form-item style="margin-top: 3em">
            <el-button style="width: 100%" type="primary" @click="begin" >开 始 执 行</el-button>
      </el-form-item>
    </el-form>

    <div v-show="showProgress">
      <span style="line-height:2em; font-size: 15px">
        {{tel}}  成功！
      </span>
      <el-progress :text-inside="true" :stroke-width="26" :percentage="((taskIndex + 1) / value) * 100"></el-progress>
    </div>

  </div>

</template>

<script lang="ts">
import { ref, defineComponent } from 'vue'
import axios from "axios"

export default defineComponent({
  name: 'Panel',
  data(){
    return {
      value: null,
      range: [1,3],
      marks: {1: '1秒', 2: '2秒',3: '3秒',4: '4秒',5: '5秒',6: '6秒',7: '7秒',8: '8秒',9: '9秒'},
      taskIndex: 0,
      index: 0,
      total: 0,
      tel: '',
      sleeping: false,
      loading: false,
      showProgress: false
    }
  },
  props: {
    msg: {
      type: String,
      required: true
    }
  },
  setup: () => {
    const count = ref(0)
    return { count }
  },
  methods: {
    async getCount(){
      const res = await axios.get('/api/count')
      const data = res.data
      this.index = data.index
      this.total = data.total
    },
    async addUser(){
      this.loading = true
      const res = await axios.post('/api/user')
      const data = res.data
      this.index = data.index
      this.tel = data.tel
      this.loading = false
    },
    async begin(){
      this.showProgress = true
      for (let index = 0; index < this.value; index++) {
        this.taskIndex = index
        const t = this.getRand(this.range[0], this.range[1])
        await this.sleep(t)
        await this.addUser()
      }
    },
    getRand(min, max) {
      return Math.random() * (max - min) + min;
    },
    sleep(t){
      this.sleeping = true
      return new Promise((resolve, reject)=>{
        setTimeout(()=>{
          this.sleeping = false
          resolve(null)
        }, t * 1000)
      })
    }
  },
  created(){
    this.getCount()
  }
})
</script>

<style scoped>
.pannel{
  margin: 15px;
}

@media screen and (max-width: 700px) {
    h1 > span {
        display: block;
    }

}
</style>
