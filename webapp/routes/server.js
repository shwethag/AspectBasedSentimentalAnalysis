var exports = module.exports = {};
var express = require('express');
var path = require('path');

var router = express.Router();
var dbName = 'project';
var mongoose = require('mongoose');
var schema = require('../model/dbschema')

router.route('/').get(function(req, res){
  res.render('layout', {
    title: 'Home'
  });
});

router.route('/result').post(function(req, res){
  console.log("Result page");
  var subject = req.body.subject;
  var object = req.body.object;
  where = {'subjectEntity':{$regex:new RegExp("/.*" + subject + ".*/i")}};
  console.log("entity 1 " + req.body.subject);
  console.log("entity 2 " + req.body.object);
  schema.graph.find(where,function(err,result){
  	if(err){
  		console.log("Error in fetching data");

  	}else{
  		console.log("Queried successfully");
  		console.log(result);
  		//res.json(result);
  	}
  });
 // var query = schema.graph.find().where('subjectEntity').equals(subject).where('objectEntity').equals(object);
 /*var reg = new RegExp('.*'+$subject+'.*',i);
 console.log("Regex constructed" + reg);
 var query = schema.graph.find().where('subjectEntity').regex(reg);

  console.log('constructed query:');

  query.exec(function(err,res){
  	console.log('queried!!');
  	if(err){
  		console.log('Error in query');  
  	}else{
  		console.log(res);
  	}
  });
 */

});



module.exports = router;