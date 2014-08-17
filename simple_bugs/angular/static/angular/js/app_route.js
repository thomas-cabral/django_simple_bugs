/**
 * Created by Thomas on 5/23/14.
 */
var caseApp = angular.module('caseApp', ['ngRoute', 'ngAnimate', 'ngSanitize', 'ngResource', 'ngCookies', 'djangoRESTResources']);

	// configure our routes
    caseApp.config(function($routeProvider, $locationProvider) {
		$routeProvider.
			// route for the home page
            when('/', {
                templateUrl : '/angular/pages/list',
                controller : 'CaseList'
            }).
			// route for the about page
			when('/detail/:caseId', {
				templateUrl : '/angular/pages/detail',
				controller  : 'CaseDetail'
			}).
            //route for new page
            when('/new', {
                templateUrl : '/angular/pages/new',
                controller : 'CaseNew'
            }).

            otherwise({redirectTo: '/'});

        //$locationProvider.html5Mode(true);
	});