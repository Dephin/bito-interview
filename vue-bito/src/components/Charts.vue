<template>
  <div class="x-bar">
    <div :id="id"></div>
  </div>
</template>

<script>
import HighCharts from 'highcharts'

export default {
  name: 'charts', // 验证类型
  props: {
    id: {
      type: String
    },
    data: {
      type: Array
    },
    titles: {
      type: Object
    }
  },
  data () {
    return {
      option: {
        title: {
          // 大标题
          text: this.titles.title
        },
        subtitle: {
          // 小标题
          text: this.titles.subtitle
        },
        yAxis: {
          title: {
            text: this.titles.yAxisTitle
          }
        },
        legend: {
          layout: 'vertical',
          align: 'right',
          verticalAlign: 'middle'
        },
        plotOptions: {
          series: {
            label: {
              connectorAllowed: false
            },
            pointStart: 2010
          }
        },
        series: '',
        responsive: {
          rules: [{
            condition: {
              maxWidth: 500
            },
            chartOptions: {
              legend: {
                layout: 'horizontal',
                align: 'center',
                verticalAlign: 'bottom'
              }
            }
          }]
        }
      }
    }
  },
  watch: {
    data: {
      handler (newValue, oldValue) {
        console.log('watch')
        console.log(newValue)
        this.option.series = newValue
        HighCharts.chart(this.id, this.option)
      },
      deep: true
    }
  },
  mounted () {
    console.log('mounted')
    console.log(this.option)
    console.log(this.data)
    this.option.series = this.data
    HighCharts.chart(this.id, this.option)
  }
}
</script>

<style scoped>

</style>
