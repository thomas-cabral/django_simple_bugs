/**
 * Created by Thomas on 5/23/14.
 */
function CaseDetailResource($scope, $resource, $routeParams) {
    var Case = $resource('/api/cases/:caseId');
    Case.get({caseId: $routeParams.caseId}, function(data) {
        $scope.case_detail = data;
    });
}

function CaseDetail($scope, $routeParams, $http) {
    $http.get('/api/cases/' + $routeParams.caseId).success(function(data) {
        //console.log(data);
        $scope.case_detail = data;
    });
}

function CaseList($scope, $routeParams, $http, $location) {
    if($routeParams.search !== undefined) {
        $http.get('/api/cases/?search=' + $routeParams.search).success(function(data) {
        //console.log(data);
        $scope.case_detail = data;
    });
    }
    else {
        $http.get('/api/cases/').success(function(data) {
        //console.log(data);
        $scope.case_detail = data;
    });
    }

    $scope.location = $location;
    $scope.$watch('location.search()', function() {
        $scope.target = ($location.search());
    }, true);

    $scope.changeTarget = function(name) {
        $location.search('search', name);
    }
}

function CaseNew($scope, $http, $location) {
    $scope.formData = {};
    $scope.formData.closed = false;
	$scope.save = function() {
		$http.post('/api/cases/', $scope.formData).success(function(data) {
		    $scope.formData = {}; // clear the form so our user is ready to enter another
			$scope.todos = data;
            $location.path('/detail/' + data.pk);
			//console.log(data);
			}).error(function(data) {
				console.log('Error: ' + data);
                $scope.error = data
			});
};
}