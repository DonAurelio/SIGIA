(function(){
	'use strict';

	angular
		.module('concesionario.controllers')
		.controller('IndexController',IndexController)
		.controller('SucursalController',SucursalController);

	IndexController.$inject = ['$location','$scope'];

	function IndexController($location, $scope){
		$scope.name = "Hola Mundo angular";
	}


	SucursalController.$inject = ['$location','$scope'];

	function SucursalController($location, $scope){
		$scope.name = "Hola Mundo angular 2";
	}
})();