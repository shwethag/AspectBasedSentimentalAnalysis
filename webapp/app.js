var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var jsonfile = require('jsonfile');

var routes = require('./routes/index');
var users = require('./routes/users');
var server = require('./routes/server');
var dbName = 'project';
var mongoose = require('mongoose');
var csv = require('fast-csv');
var path = require('path');
var schema = require('./model/dbschema');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));


/** DB *****/

var conn_string = 'mongodb://localhost:27017/'+dbName;
mongoose.connect(conn_string);
mongoose.connection.on('open',function(ref){
	console.log('Db connected!!');
	mongoose.connection.db.collectionNames(function (err, names) {
        console.log(names); // [{ name: 'dbname.myCollection' }]
       
    });
    //insertDb();

});

insertDb = function(){
	console.log('inserting values');
	csv.fromPath(path.join(__dirname,'./data.csv')).on("data",function(data){
		var jsonObj = {}
		jsonObj['polarity'] = Number(data[0]);
		jsonObj['title'] = data[1];
		jsonObj['URL'] = data[2];
		jsonObj['objectEntity'] = data[3];
		jsonObj['source'] = data[4];
		jsonObj['articleId'] = data[5];
		jsonObj['subjectEntity'] = data[6];
		/*console.log(data);
		console.log(jsonObj);
		console.log('--------');*/
		var graph = new schema.graph(jsonObj);
		graph.save(function(err){
			if(err){
				console.log('error in inserting data to DB: '+ data);
				console.log(err)
			}
		});
							
	});
}


app.use('/', routes);
app.use('/users', users);
app.use('/server', server);
// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
      message: err.message,
      error: err
    });
  });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.render('error', {
    message: err.message,
    error: {}
  });
});


module.exports = app;
