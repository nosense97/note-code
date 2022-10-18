# Google Chart / Note Code

## About 

See real examples:

* <https://developers.google.com/chart>

## Table of contents

> * [Draw Chart Basic With JS](#google-chart-with-js-basic)
> * [Combo Chart With Lines And Stacked Column / Biểu đồ kết hợp cột đường với cột chồng](#combo-chart-with-lines-and-stacked-column)  

  
## Google Chart With JS Basic

``` 
<script type="text/javascript">
    var BuildColumnChart = (params) => {

        columnChartElement = document.querySelector(params.div)
        if (columnChartElement) {

            google.charts.load('current', {
                'packages': ['bar']
            });
            google.charts.setOnLoadCallback(drawChart);

            function drawChart() {

                var data = google.visualization.arrayToDataTable(params.dataTable);
                var chart = new google.charts.Bar(columnChartElement);
                chart.draw(data, google.charts.Bar.convertOptions(params.options));
            }
        }
    }

    BuildColumnChart({
        div: '#columnchart_material',
        dataTable: [
            ['Year', 'Sales', 'Expenses', 'Profit'],
            ['2014', 1000, 400, 200],
            ['2015', 1170, 460, 250],
            ['2016', 660, 1120, 300],
            ['2017', 1030, 540, 350]
        ],
        options: {
            width: 600,
            height: 400,
            chart: {
                title: 'Company Performance',
                subtitle: 'Sales, Expenses, and Profit: 2014-2017',
            }
        }
    })
</script>
```
This is result: 
![image](https://user-images.githubusercontent.com/108250685/196375980-2dde583b-52e1-4a1b-96b9-be87650787c9.png)


## Combo Chart With Lines And Stacked Column  

```
            var data = google.visualization.arrayToDataTable([
                ['Genre', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General', 'Western', 'Literature', {
                    role: 'annotation'
                }],
                ['2010', 10, 24, 20, 32, 18, 5, ''],
                ['2020', 16, 22, 23, 30, 16, 9, ''],
                ['2030', 28, 19, 29, 30, 12, 13, '']
            ]);

            var options = {
                width: 600,
                height: 400,
                legend: { // ghi chú của chart 
                    position: 'top',
                    maxLines: 3
                },
                bar: {
                    groupWidth: '75%'
                },
                isStacked: true,
                title: 'Monthly Coffee Production by Country',
                vAxis: {
                    title: 'Cups'
                },
                hAxis: {
                    title: 'Month'
                },
                seriesType: 'bars',
                series: { // bắt đầu từ 0, kí hiệu thứ 2 là đường thẳng
                    2: {
                        type: 'line'
                    }
                }
            };
```
