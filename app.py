def express()
var express = require('express');

var app = express(); #the main app
var admin = express(); #the sub app

admin.get('/', function (req, res) {
  console.log(admin.mountpath); 
  res.send('Admin Homepage');
});

app.use('/admin', admin); 

