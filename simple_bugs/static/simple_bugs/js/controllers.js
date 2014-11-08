caseApp.factory('CasesFactory', function (djResource) {
    return djResource('/api/cases/', {}, {
        query: { method: 'GET', isArray: true },
        create: { method: 'POST' }
    })
});

caseApp.factory('CaseFactory', function (djResource) {
    return djResource('/api/conversation/:id/', {}, {
        show: { method: 'GET' },
        update: { method: 'PUT', params: {id: '@id'} },
        delete: { method: 'DELETE', params: {id: '@id'} }
    })
});

caseApp.run( function run($http, $cookies ){
    // Grab the CSRF Token
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});


function CaseDetail($scope, $routeParams, $http) {
    $http.get('/api/cases/' + $routeParams.caseId).success(function(data) {
        //console.log(data);
        $scope.case_detail = data;
    });
}

caseApp.controller('CaseNew', ['$scope', 'CasesFactory',
    function ($scope, CasesFactory) {
        $scope.save = function () {
            CasesFactory.create($scope.case);
        };
    }
]);

caseApp.controller('CaseList', ['$scope', '$routeParams', '$http', 'CaseFactory', 'CasesFactory', '$location',
    function ($scope, $routeParams, $http, CaseFactory, CasesFactory) {

        $scope.save = function () {
            CaseFactory.update($scope.conversation);
        };

        $scope.search = function () {
        if($scope.search_query != null) {
            $http.get('/api/cases/?search=' + $scope.search_query).success(function(data) {
            //console.log(data);
            $scope.cases = data.results;
        });
        }
        else {
            $http.get('/api/cases/').success(function (data) {
                //console.log(data);
                $scope.cases = data.results ;
            });
        }};



        // create a comment without a parent
        $scope.createNewComment = function () {
            $scope.comment.conversation = $scope.conversation.id;
            CommentsFactory.create($scope.comment, function(data){
                $scope.comments.push(data);
                $scope.comment = null;
                $scope.error = null;
            }, function(error) {
                $scope.error = error
            });
        };

        $scope.refresh = function () {
            $scope.comments = CasesFactory.query({id: $routeParams.id});
            console.log($scope.comments);
        };

        $scope.cases = CasesFactory.query();
    }
]);