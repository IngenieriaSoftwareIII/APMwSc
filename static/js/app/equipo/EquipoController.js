scrumModule.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/VEquipo/:idPila', {
                controller: 'VEquipoController',
                templateUrl: 'app/equipo/VEquipo.html'
            });
}]);

scrumModule.controller('VEquipoController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'equipoService', 'prodService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, equipoService, prodService) {
      $scope.msg = '';
      $scope.fEquipo = {};

      equipoService.VEquipo({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        $scope.fEquipo = $routeParams.fEquipo;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }

      });
      $scope.VProducto1 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };

      $scope.fEquipoSubmitted = false;
      $scope.AActualizarEquipo0 = function(isValid) {
        $scope.fEquipoSubmitted = true;
        if (isValid) {
          
          equipoService.AActualizarEquipo($scope.fEquipo).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
