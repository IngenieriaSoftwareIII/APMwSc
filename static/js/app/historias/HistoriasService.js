scrumModule.service('historiasService', ['$q', '$http', function($q, $http) {

    this.ACambiarPrioridades = function(fPrioridades) {
        return  $http({
          url: "historias/ACambiarPrioridades",
          data: fPrioridades,
          method: 'POST',
        });
    //    var labels = ["/VHistorias", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACrearHistoria = function(fHistoria) {
        return  $http({
          url: "historias/ACrearHistoria",
          data: fHistoria,
          method: 'POST',
        });
    //    var labels = ["/VHistorias", "/VCrearHistoria", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AElimHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/AElimHistoria',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VHistorias", "/VHistoria", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AModifHistoria = function(fHistoria) {
        return  $http({
          url: "historias/AModifHistoria",
          data: fHistoria,
          method: 'POST',
        });
    //    var labels = ["/VHistorias", "/VHistoria", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.APrelaciones = function(fPrelaciones) {
        return  $http({
          url: "historias/APrelaciones",
          data: fPrelaciones,
          method: 'POST',
        });
    //    var labels = ["/VPrelaciones", "/VPrelaciones", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACompletarHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/ACompletarHistoria',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AIncompletarHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/AIncompletarHistoria',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/VCrearHistoria',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/VHistoria',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };


    this.VHistorias = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/VHistorias',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VPrelaciones = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/VPrelaciones',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VDiagramaPrelaciones = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/VDiagramaPrelaciones',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VPrioridades = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/VPrioridades',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);
