caseApp.factory('CasesFactory', function (djResource) {
    return djResource('/api/cases/', {}, {
        query: { method: 'GET', isArray: true },
        create: { method: 'POST' }
    })
});

caseApp.factory('CaseFactory', function ($resource) {
    return $resource('/api/cases/:id/', {}, {
        show: { method: 'GET' },
        update: { method: 'PUT', params: {id: '@id'} },
        delete: { method: 'DELETE', params: {id: '@id'} }
    })
});