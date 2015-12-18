'use strict';

/* Controlers */

var concesionarioControllers = angular.module('concesionarioControllers',[]);

concesionarioControllers.controller('IndexCtrl',['$scope','$http',
	function($scope, $http){
		$scope.name = "Funciona ";
	}]);