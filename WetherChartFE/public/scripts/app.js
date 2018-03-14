angular.module('readingController',[]);

angular.module("routerApp", [
	'readingController','ngRoute','chart.js',
	])


.config(['$routeProvider',function ($routeProvider) {

	$routeProvider
		.when('/readings',{
		controller:'readingController',
		templateUrl:'./modules/home/views/index.html',
	})

	.otherwise({redirectTo:'/readings'});
}])