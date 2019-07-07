<template>
  <div>
    <el-row>
      <el-col span="4">
        <h2 style=""><strong>People Chart</strong></h2>
      </el-col>
      <el-col span="2" offset="15">
        <el-button  @click="snapshot" type="primary">save</el-button>
      </el-col>
    </el-row>
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
    snapshot () {
      this.updateSnapshotPeopleData(this.data)
    },
    getPeopleData () {
      console.log('refresh')
      api.getPeopleResource()
        .then((res) => {
          this.data = res.data
          this.updatePeopleData(res.data)
        })
        .catch((res) => {
          console.log(res)
        })
    },
    updatePeopleData (data) {
      api.updatePeopleResource(data)
        .then((res) => {
        })
        .catch((res) => {
          console.log(res)
        })
    },
    updateSnapshotPeopleData (data) {
      api.updatePeopleSnapshotResource(data)
        .then((res) => {
          this.$message('save successfully')
          this.$root.eventHub.$emit('refreshSubpage2', this.data)
        })
        .catch((res) => {
          this.$message('save failed')
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
