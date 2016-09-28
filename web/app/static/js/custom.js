LAST_INDEX = 0
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
}
get_messages()
//Polls every 5 seconds
setInterval(function() {get_messages();}, 5000)

function calculate(i, j, k) {
    total = i + j + k
    i = Math.round(i * 100 /total)
    j = Math.round(j * 100 /total)
    k = Math.round(k * 100 /total)
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
    positive_markup = ''
    neutral_markup = ''
    negative_markup = ''
    p = 0, n = 0 , nn = 0
    data = data.split('],')
    for (var i = 0; i < data.length - 1; i++) {
        t = data[i].replace('[', '')
        t = t.split(',')
        text = t[0].replace(/'/g, '')
        score = t[1]
        type = t[2]
        if (score < 0) {negative_markup += tweet(text, '#F22613'); n += 1}
        else if (score > 0) {positive_markup += tweet(text, '#26A65B'); p += 1}
        else {neutral_markup +=  tweet(text, '#F89406'); nn += 1}
    }
    $('#positive-tweets').html(positive_markup)
    $('#neutral-tweets').html(neutral_markup)
    $('#negative-tweets').html(negative_markup)
    calculate(p, nn, n)
}

function tweet(text, color) {
    return '<div class="tweet"><i class="fa fa-twitter" style="color:'+ color + ';"></i><p>' + text + '</p></div>'
}