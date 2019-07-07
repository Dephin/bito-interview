<template>
  <div id="app">
    <el-row><h1>BITO  INTRODUCTION</h1></el-row>
    <el-row>
      <el-tabs v-model="activeName" @tab-click="handleClick" tabPosition="left">
        <el-tab-pane label="SUBPAGE1" name="subpage1">
          <subpage1></subpage1>
        </el-tab-pane>
        <el-tab-pane label="SUBPAGE2" name="subpage2">
          <subpage2></subpage2>
        </el-tab-pane>
      </el-tabs>
    </el-row>
  </div>
</template>

<script>
import Subpage1 from '@/components/Subpage1'
import Subpage2 from '@/components/Subpage2'

export default {
  name: 'App',
  data () {
    return {
      activeName: 'subpage1'
    }
  },
  methods: {
    handleClick (tab, event) {
      console.log(tab, event)
    }
  },
  components: {
    'Subpage1': Subpage1,
    'Subpage2': Subpage2
  }
}
</script>

<style>
  .el-row {
    width: 1200px;
    margin: auto;
  }
  .container {
    width: 1200px;
    margin: auto;
  }
  .el-tabs__nav-wrap::after {
    display:none !important;
  }
  .el-tabs__item {
    padding-left: 0;
  }
  .el-tabs--left .el-tabs__item.is-left {
    text-align: left;
  }
  .el-tabs--left .el-tabs__header.is-left {
    margin-right: 48px;
  }
  .el-tabs {
    margin-top: 24px;
  }
  .el-card__body {
    padding: 16px 0 0 0;
  }
</style>
