angular.module('testService', [])//Declaramos el modulo
	.factory('testRequest', function($http) { //declaramos la factory
		// var path = "http://jsonplaceholder.typicode.com/";//API path
		var path = "http://localhost:8000/";//API path
		return {
			//Login
			posts : function(institucion){ //Retornara la lista de posts
				global = $http.get(path+institucion);
				return global;
			},
			post : function(id,nom){ //retornara el post por el id
				global = $http.get(path+nom+id);
				return global;	
			},
      add_post : function(nomInst,informacion){ //retornara el post por el id
				global = $http.post(path+nomInst,informacion);
				return global;	
			},
	  upda_post : function(nomInst1,id,informacion){ //retornara el post por el id
				global = $http.put(path+nomInst1+id+"/",informacion);
				return global;	
			},
		delete_post : function(id,nom){ //retornara el post por el id
				global = $http.delete(path+nom+id+"/");
				return global;	
			}


		}
	});
