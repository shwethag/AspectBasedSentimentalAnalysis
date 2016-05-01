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
  
 var query = schema.graph.find().where('subjectEntity').regex(new RegExp(subject,'i')).where('objectEntity').regex(new RegExp(object,'i'));

  console.log('constructed query:');
  var qres;
  query.exec(function(err,resp){
  	console.log('queried!!');
  	if(err){
  		console.log('Error in query');  
  	}else{
  		for(var i=0;i<resp.length;i++){
  			console.log(resp[i]);
  			console.log("----------------------------");
  		}
  		res.render('result',{'params':resp});
  	}
  });

  
 
});



module.exports = router;