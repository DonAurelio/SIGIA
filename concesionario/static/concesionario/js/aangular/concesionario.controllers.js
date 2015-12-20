(function(){
	'use strict';

	angular
		.module('concesionario.controllers')
		.controller('IndexController',IndexController);

	IndexController.$inject = ['$location','$scope'];

	function IndexController($location, $scope){
		$scope.name = "Hola Mundo angular";
	}
})();