<template>
  <div>
    <el-card shadow="always">
      <x-chart id="highcharts" class="high" :data.sync="data" :titles="chartTitles"></x-chart>
    </el-card>
  </div>
</template>

<script>
import XChart from '@/components/Charts'
import api from '../api/index'
export default {
  name: 'subpage1',
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
  mounted () {
    this.getPeopleData()
    setInterval(() => {
      setTimeout(this.getPeopleData, 0)
    }, 10 * 1000)
  },
  methods: {
    getPeopleData () {
      console.log('refresh')
      api.getParentResource()
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
</style>
