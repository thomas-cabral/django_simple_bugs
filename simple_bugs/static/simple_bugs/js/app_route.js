/**
 * Created by Thomas on 5/23/14.
 */
var caseApp = angular.module('caseApp', ['ngRoute', 'ngAnimate', 'ngSanitize', 'ngResource']);

	// configure our routes
    caseApp.config(function($routeProvider, $locationProvider) {
		$routeProvider.
			// route for the home page
            when('/', {
                templateUrl : '/socool/pages/list',
                controller : 'CaseList'
            }).

			// route for the about page
			when('/detail/:caseId', {
				templateUrl : '/socool/pages/detail',
				controller  : 'CaseDetailResource'
			}).

            //route for new page
            when('/new', {
                templateUrl : '/socool/pages/new',
                controller : 'CaseNew'
            }).

            otherwise({redirectTo: '/'});

        //$locationProvider.html5Mode(true);
	});