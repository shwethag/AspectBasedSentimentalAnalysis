var mongoose = require('mongoose');
var schema = mongoose.Schema;

var graphSchema = new schema({
	polarity : {type: Number,default:0},
	title : {type:String},
	URL : {type:String},
	objectEntity : {type : String},
	source : {type: String},
	articleId : {type: String},
	subjectEntity : {type:String}
});

var graph = mongoose.model('graph',graphSchema);

module.exports = {
	graph : graph
};