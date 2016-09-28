function draw_donut(element, val, sentiment, color ) {
    AmCharts.makeChart(element, {
      "type": "pie",
      "allLabels": [{
        "text": val + "%",
        "align": "center",
        "size": "50",
        "bold": true,
        "fontFamily": "raleway",
        "y": 220
      }, {
        "text": sentiment,
        "align": "center",
        "size": "15",
        "fontFamily": "raleway",
        "bold": false,
        "y": 300
      }],
      "dataProvider": [{
        "title": "Other",
        "value": 100 - val,
      }, {
        "title": "Sentiment",
        "value": val,
      }],
      "titleField": "title",
      "valueField": "value",
      "labelRadius": -130,
      "radius": "150",
      "innerRadius": "120",
      "labelText": "",
      "startDuration": 0,
      "colors": ["#ccc", color],
      "fontFamily": "raleway",
    });
    console.log('donut drawn')
    console.log(element)
}

draw_donut('bar1', 70, 'Positive', '#26A65B')
draw_donut('bar2', 20, 'Neutral', '#F89406')
draw_donut('bar3', 10, 'Negative', '#F22613')

//setInterval(function() {run();}, 1000)

function run() {
    i = Math.floor((Math.random() * 100) + 1);
    j = Math.floor((Math.random() * (100-i)) + 1);
    k = 100 -i -j
    draw_donut('bar1', i, 'Positive', '#26A65B')
    draw_donut('bar2', j, 'Neutral', '#F89406')
    draw_donut('bar3', k, 'Negative', '#F22613')
}

function get_messages() {
    $.ajax({
		method: "GET",
		url: '/messages',
		success: function(data) {
			display_tweets(data)
		}
	});
}

function display_tweets(data) {
    console.log(JSON.parse(data.replace(/u'/g, "'");))
}