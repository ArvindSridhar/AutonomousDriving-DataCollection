var express = require('express');
var path = require('path');
var app = express();
var fs = require('fs')

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');
const url = 'mongodb://arvindsridhar:addeepl3arning92@ds225028.mlab.com:25028/autonomousdriving';
const dbName = 'autonomousdriving';

app.set('port', 3000);
app.use(express.static(path.join(__dirname, '/frontend')));

app.get('/send', function(req, res) {
	var data = req.param("name");
    var video = req.param("url");
    data = JSON.parse(data);
    console.log(video);
    
    MongoClient.connect(url, function(err, client) {
        assert.equals(err, null);
        console.log("Connected successfully to server");
        var myobj = { name: video, clickLogs: data };
        const db = client.db(dbName);
        db.collection("timestamps").insertOne(myobj, function(err, res) {
            assert.equals(err, null);
            console.log("1 document inserted");
        });
        db.close();
    });
    
	res.send(req.body);
});

var server = app.listen(app.get('port'), function() {
  var port = server.address().port;
  console.log('Magic happens on port ' + port);
});