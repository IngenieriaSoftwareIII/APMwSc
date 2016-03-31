scrumModule.service('sprintService', ['$q', '$http', function($q, $http) {

    this.ACrearSprint = function(fSprint) {
        return  $http({
          url: "sprint/ACrearSprint",
          data: fSprint,
          method: 'POST',
        });
    //    var labels = ["/VSprints", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACriterioHistoria = function(fCriterioHistoria) {
        return  $http({
          url: "sprint/ACriterioHistoria",
          data: fCriterioHistoria,
          method: 'POST',
        });
    //    var labels = ["/VSprint", "/VCriterioHistoria", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AElimCriterioHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/AElimCriterioHistoria',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VSprint", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AElimSprint = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/AElimSprint',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VSprints", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AElimSprintHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/AElimSprintHistoria',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VSprint", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AElimSprintTarea = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/AElimSprintTarea',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VSprint", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AModifSprint = function(fSprint) {
        return  $http({
          url: "sprint/AModifSprint",
          data: fSprint,
          method: 'POST',
        });
    //    var labels = ["/VSprints", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AResumenHistoria = function(fResumenHistoria) {
        return  $http({
          url: "sprint/AResumenHistoria",
          data: fResumenHistoria,
          method: 'POST',
        });
    //    var labels = ["/VSprint", "/VResumenHistoria", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ASprintHistoria = function(fSprintHistoria) {
        return  $http({
          url: "sprint/ASprintHistoria",
          data: fSprintHistoria,
          method: 'POST',
        });
    //    var labels = ["/VSprint", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ASprintTarea = function(fSprintTarea) {
        return  $http({
          url: "sprint/ASprintTarea",
          data: fSprintTarea,
          method: 'POST',
        });
    //    var labels = ["/VSprint", "/VSprint", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearSprint = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/VCrearSprint',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCriterioHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/VCriterioHistoria',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VResumenHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/VResumenHistoria',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VSprint = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/VSprint',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VSprintHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/VSprintHistoria',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VSprintTarea = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/VSprintTarea',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VSprints = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'sprint/VSprints',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);