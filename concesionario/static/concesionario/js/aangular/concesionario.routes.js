(function (){
	'use strict';

	angular
	.module('concesionario.routes')
	.config(config);

	config.$inject = ['$routeProvider'];

	function config($routeProvider){
		$routeProvider.
		when('/', {
			templateUrl:'/static/concesionario/templates/index.html',
			controller:'IndexController'
		});
	}
})();