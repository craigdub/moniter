function init_second_cpu(socket) {
	Highcharts.setOptions({
	    global: {
	        useUTC: false
	    }
	});

	$('#second-cpu').highcharts({
	    credits: {
	        enabled: false
	    },
	    scrollbar: {
	        liveRedraw: false,
	        minWidth: 20
	    },
	    chart: {
            type: 'column',
	        height: 100,
            width: 400
	    },
	    title: {
	        text: 'Cpu Load',
	        style: {
	            color: '#333',
	            fontSize: '1.1em'
	        },
	        align: 'right',
	        verticalAlign: 'bottom'
	    },
	    legend: {
	        enabled: true,
	        borderWidth: 0,
	        layout: 'vertical',
	        verticalAlign: 'middle',
	        align: 'left'
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
	        pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}%</b><br/>',
	        valueDecimals: 2
	    },
	    navigator: {
	        adaptToUpdatedData: false,
	    },
	    series: [{'name':'cpu', data:[]}]
	});

	socket.on('second_cpu', function(point) {
		var chart = $('#second-cpu').highcharts();

        var pointColor = 'green';
        if (point > 88) {
            pointColor = 'orange';
        } 
        else if (point > 94) {
            pointColor = 'red';
        }
        var sshift = chart.series[0].data.length > 40;
        chart.series[0].addPoint({y: point, color: pointColor}, true, sshift);
	});
}