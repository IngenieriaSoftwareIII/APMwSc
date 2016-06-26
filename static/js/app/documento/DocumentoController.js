scrumModule.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/VCrearDocumento/:idPila', {
                controller: 'VCrearDocumentoController',
                templateUrl: 'app/documento/VCrearDocumento.html'
            });
}]);

scrumModule.controller('VCrearDocumentoController',
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'documentoService', 'identService', 'prodService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, documentoService, identService, prodService) {
      $scope.msg = '';
      $scope.fDocumento = {};

      documentoService.VCrearDocumento({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }


      });
      $scope.VProducto0 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };
      $scope.VLogin1 = function() {
        $location.path('/VLogin');
      };

      $scope.fDocumentoSubmitted = false;
      $scope.ACrearDocumento2 = function(isValid) {
        $scope.fDocumentoSubmitted = true;
        if (isValid) {

          documentoService.ACrearDocumento($scope.fDocumento).then(function (object) {
              window.open("../../../temp/Documento-Vision.pdf")
              // var msg = object.data["msg"];
              // if (msg) flash(msg);
              // var label = object.data["label"];
              // $location.path(label);
              // $route.reload();
          });
        }
      };

    }]);
