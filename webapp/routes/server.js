var exports = module.exports = {};
var express = require('express');
var path = require('path');

var router = express.Router();


router.route('/').get(function(req, res){
  res.render('layout', {
    title: 'Home'
  });
});

router.route('/newpage').get(function(req, res){
  res.render('anotherpage', {
    title: 'Home'
  });
});

module.exports = router;