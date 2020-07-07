<template>
  <div class="home">
    <el-input
      type="textarea"
      :rows="3"
      placeholder="复制表格内容进来"
      v-model="textarea"
    ></el-input>
    共{{ list.length }} 条数据
    <el-button type="primary" @click="start">开始整理</el-button>
    <el-button type="primary" @click="exportCVS">导出数据</el-button>
    <el-table :data="list" style="width: 100%" @sort-change="sortChange">
      <el-table-column type="index" width="100"> </el-table-column>
      <el-table-column sortable prop="name" label="昵称"> </el-table-column>
      <el-table-column sortable prop="num" label="电话"> </el-table-column>
      <el-table-column prop="email" label="邮箱"> </el-table-column>
      <el-table-column sortable prop="country" label="国家"> </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { countries } from "../store/cuntries";
export default {
  name: "Home",
  data() {
    return {
      list: [],
      countries,
      textarea: ""
    };
  },
  methods: {
    start() {
      const arr = [];
      const l = this.textarea.split("\n");
      l.forEach(element => {
        const i = element.split("\t");
        const c = this.getCountry(i[1]);
        arr.push({
          name: i[0],
          num: i[1],
          email: i[2],
          country: c && c.name,
          countryCode: c && c.short,
          tel: (c && c.tel) || 0
        });
        this.list = arr;
      });
    },
    sortChange(column, prop, order) {
      console.log(column, prop, order);
    },
    getCountry(num) {
      const c = countries.find(item => {
        const re = new RegExp("^" + item.tel + "\\d{8,11}$");
        // console.log(re, num);
        return re.test(num);
      });
      // let c = "";
      // for (const key in phones) {
      //   const element = phones[key];
      //   if (element.test(num)) {
      //     c += key;
      //   }
      // }
      return c;
    },
    exportCVS() {
      this.list.sort((a, b) => a.tel - b.tel);
      let countryIndex = 0;
      let lastCountryCode = "";
      this.list.forEach(item => {
        if (lastCountryCode != item.countryCode) {
          countryIndex = 0;
        }
        item.countryIndex = ++countryIndex;
        lastCountryCode = item.countryCode;
      });
      console.log;
      this.exportToCsv(
        new Date().toLocaleDateString() +
          new Date().toLocaleTimeString() +
          ".csv",
        this.list.map(item => [
          "b" +
            (item.countryCode || "NOCOUNTRY") +
            ("000" + item.countryIndex).slice(-4) +
            " > " +
            item.name,
          item.name,
          item.num,
          item.country,
          item.countryCode,
          "\n"
        ])
      );
    },
    exportToCsv: function(filename, data) {
      console.log(11);
      const blob = new Blob(data, { type: "text/csv,charset=UTF-8" });
      const csvUrl = URL.createObjectURL(blob);
      let link = document.createElement("a");
      link.download = filename; //文件名字
      link.href = csvUrl;
      link.click();
    }
  },
  computed: {
    // list() {
    //   const arr = [];
    //   const l = this.textarea.split("\n");
    //   l.forEach(element => {
    //     const i = element.split("\t");
    //     arr.push({
    //       name: i[0],
    //       num: i[1],
    //       email: i[2]
    //     });
    //   });
    //   return arr;
    // }
  }
};
</script>
