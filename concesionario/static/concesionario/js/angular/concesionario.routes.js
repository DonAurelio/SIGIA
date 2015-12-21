(function (){
	'use strict';

	angular
	.module('concesionario.routes')
	.config(config);

	config.$inject = ['$routeProvider'];

	function config($routeProvider){
		$routeProvider.
		when('/', {
			templateUrl:'/static/concesionario/templates/view.html',
			controller:'IndexController'
		}).when('/sucursal/crear', {
			templateUrl:'/static/concesionario/templates/view.html',
		  	controller: 'SucursalController'
		}).otherwise('/');
	}
})();