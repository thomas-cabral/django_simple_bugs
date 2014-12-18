caseApp.run( function run($http, $cookies ){
    // Grab the CSRF Token
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});


caseApp.controller('CaseDetail', ['$scope', 'CaseFactory', '$routeParams',
    function ($scope, CaseFactory, $routeParams) {
        $scope.case = CaseFactory.show({id: $routeParams.id});
}]);

caseApp.controller('CaseList', ['$scope', '$routeParams', 'CasesFactory',
    function ($scope, $routeParams, CasesFactory) {
        $scope.cases = CasesFactory.query();
    }
]);