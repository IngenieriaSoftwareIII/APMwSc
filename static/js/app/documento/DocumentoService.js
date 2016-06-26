scrumModule.service('documentoService', ['$q', '$http', function($q, $http) {

    this.ACrearDocumento = function(fDocumento) {
        return  $http({
          url: "documento/ACrearDocumento",
          data: fDocumento,
          method: 'POST',
        });
    //    var labels = ["/VCrearDocumento", "/VProducto", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearDocumento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'documento/VCrearDocumento',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);