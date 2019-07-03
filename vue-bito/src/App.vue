<template>
  <div id="app">
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="subpage1" name="subpage1">
        <subpage1></subpage1>
      </el-tab-pane>
      <el-tab-pane label="subpage2" name="subpage2">
        <subpage2></subpage2>
      </el-tab-pane>
    </el-tabs>
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
  .el-tabs {
    width: 1200px;
    margin: auto;
  }
  html {
    background: #CCCCCC;
  }
</style>
