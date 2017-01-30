angular.module('myApp', ['testService']);

angular.module('myApp').controller('testController', ['$scope','testRequest',testController]);
function testController($scope, testRequest) {
	$scope.posts={};
	$scope.mensaje="";
	$scope.getInstitucion = function(){
		$scope.unPost={};
		testRequest.post($scope.post_id,$scope.post_nom1).then(function (data){
			$scope.unPost=data.data; // Asignaremos los datos del post
			$scope.unPost.exist=1;
			$scope.posts.exist=0;
		});
	}
    $scope.crear = function(){
    datos = {'nombre': $scope.a.nombre, 'ciudad': $scope.a.ciudad, 'latitud': $scope.a.latitud, 'longitud': $scope.a.longitud}
		testRequest.add_post($scope.post_nomInst,datos).then(function (data){
			$scope.mensaje="Institucion añadida correctamente"; // Asignaremos los datos del post
      console.log(data);
		});
	}

	$scope.update = function(){
    datos = {'nombre': $scope.b.nombre, 'ciudad': $scope.b.ciudad, 'latitud': $scope.b.latitud, 'longitud': $scope.b.longitud}
		testRequest.upda_post($scope.post_nomInst1,$scope.b.id,datos).then(function (data){
			$scope.mensaje="Institucion actualizada correctamente"; // Asignaremos los datos del post
      console.log(data);
		});
	}
	$scope.delete = function(){
		$scope.unPost={};
		testRequest.delete_post($scope.id_post,$scope.post_nomInst2).then(function (data){
			$scope.unPost=data.data; // Asignaremos los datos del post
			$scope.unPost.exist=1;
			$scope.posts.exist=0;
			$scope.mensaje="Institucion Eliminada"; // Asignaremos los datos del post
      		console.log(data);
		});
	}
	$scope.getNomInstitucion = function(){
		$scope.nomPost={};
		testRequest.posts($scope.post_nom).then(function (data){
		console.log("...");
      	console.log(data.data);
			$scope.posts=data.data; // Asignaremos los datos de todos los posts
			$scope.posts.exist=1;
		});
	}
	

}

