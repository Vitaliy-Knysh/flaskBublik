

var data = [{
  values: [88, 84, 77, 66, 55, 50, 34],
  labels: ['Укропу', 'Кошачью жопу', 'Картошек', 'Мандавошек', 'Воды', 'Хуёв туды', 'Дров'],
  type: 'pie'
}];

var layout = {
  height: 400,
  width: 500
};

Plotly.newPlot('myDiv', data, layout);
