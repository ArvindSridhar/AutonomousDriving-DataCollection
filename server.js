var express = require('express');
var path = require('path');
var app = express();
var fs = require('fs')

app.set('port', 3000);
app.use(express.static(path.join(__dirname, '/frontend')));

app.get('/send', function(req, res) {
	var data = req.param("name");
    data = JSON.parse(data);
    console.log(data[0]);
	res.send(req.body);
});

var server = app.listen(app.get('port'), function() {
  var port = server.address().port;
  console.log('Magic happens on port ' + port);
});