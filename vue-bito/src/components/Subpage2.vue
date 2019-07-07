<template>
<div>
  <h2><strong>Snapshot Chart</strong></h2>
  <el-card shadow="always">
    <x-chart id="highcharts2" class="high" :data.sync="data" :titles="chartTitles"></x-chart>
  </el-card>
</div>
</template>

<script>
import XChart from '@/components/Charts'
import api from '../api'
export default {
  name: 'subpage2',
  data () {
    return {
      data: [],
      chartTitles: {
        title: '2010 ~ 2016 年太阳能行业就业人员发展情况',
        subtitle: '数据来源：thesolarfoundation.com',
        yAxisTitle: '就业人数'
      }
    }
  },
  created () {
    this.$root.eventHub.$on('refreshSubpage2', (data) => {
      this.data = data
    })
  },
  mounted () {
    this.getPeopleSnapshotData()
  },
  methods: {
    getPeopleSnapshotData () {
      api.getPeopleSnapshotResource(100)
        .then((res) => {
          this.data = res.data
        })
        .catch((res) => {
          console.log(res)
        })
    }
  },
  components: {
    XChart
  }
}
</script>

<style scoped>
  h2 {
    margin-top: 0;
  }
</style>
