// accessor without function callbacks
window.API = window.API || {};

API.prototype = (function(){
	var name = "Hello World";
	
	//
	setName : function(newName){
		name = newName;
		return this
	},
	
	//
	getName : function(){
		return name;
	}
})();

// accessor with function callbacks
window.API2 = window.API2 || {};
API2.prototype = (function(){
	var name "Hello World";
	
	//
	setName : function(newName){
		name = newName;
		return this
	},
	
	//
	getName : function(callback){
		callback.call(this, name);
		return this;
	}
})();






