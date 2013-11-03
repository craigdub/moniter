function init_second_network(socket) {
    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });

    $('#second-network').highcharts({
        credits: {
            enabled: false
        },
        scrollbar: {
            liveRedraw: false,
            minWidth: 20
        },
        chart: {
            height: 100,
            width: 400
        },
        title: {
            text: 'Network Packets Sent/Recieved',
            style: {
                color: '#333',
                fontSize: '1.1em'
            },
            align: 'right',
            verticalAlign: 'bottom'
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            line: {
                marker: {
                    enabled: false
                }
            }
        },
        rangeSelector: {
            enabled: false,
            buttons: [{
                type: 'minute',
                count: 60,
                text: '1h'
            }, {
                type: 'minute',
                count: 360,
                text: '6h'
            }, {
                type: 'minute',
                count: 720,
                text: '12h'
            }, {
                type: 'day',
                count: 1,
                text: '1d'
            }, {
                type: 'week',
                count: 1,
                text: '1w'
            }, {
                type: 'month',
                count: 1,
                text: '1m'
            }],
            selected: 0,
            inputDateFormat: '%Y-%m-%d'
        },
        yAxis: {
            title: '',
            min: 0,
            plotLines: [{
                value: 0,
                width: 2,
                color: 'silver'
            }]
        },
        xAxis: {
            labels: {
              enabled: false
            }
        },
        tooltip: {
            formatter: function() {
                return '<span style="color:' + this.series.color +'">' + this.series.name + '</span>: <b>' + this.y + '</b><br/>';
            },
            valueDecimals: 2
        },
        navigator: {
            adaptToUpdatedData: false,
        },
        series: [{'name':'Sent', data:[]}, {'name':'Received', data:[]}]
    });

    socket.on('second_net_bandwidth', function(data) {
        var chart = $('#second-network').highcharts();

        data = JSON.parse(data);

        var sshift = chart.series[0].data.length > 40;

        chart.series[0].addPoint(data.packets_sent, true, sshift);
        chart.series[1].addPoint(data.packets_recv, true, sshift);
    });
}