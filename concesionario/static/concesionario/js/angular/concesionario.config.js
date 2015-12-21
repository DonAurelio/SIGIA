(function(){
	'use strict';

	angular
	.module('concesionario.config')
	.config(config);

	config.$inject = ['$locationProvider'];

	function config($locationProvider){
		$locationProvider.html5Mode(false); /* You need to put <base href="/"> into the head of your html code  to avoid erros*/
		$locationProvider.hashPrefix('!');
	}
})();