'use strict';

/* App Module */

var concesionarioApp = angular.module('concesionarioApp',[
	'ngRoute',
	'concesionarioControllers'
]);

concesionarioApp.config(['$routeProvider',
	function($routeProvider){
		$routeProvider.
		when('/index/', {
			templateUrl:'/static/concesionario/templates/index.html',
			controller:'IndexCtrl'
		});
	}]);