# Google Chart / Note Code

## About 

See real examples:

* <https://developers.google.com/chart>

## Table of contents

> * [Branch Google Chart](#about)
>   * [Combo Chart With Lines And Stacked Column / Biểu đồ kết hợp cột đường với cột chồng](#combo-chart-with-lines-and-stacked-column)


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
