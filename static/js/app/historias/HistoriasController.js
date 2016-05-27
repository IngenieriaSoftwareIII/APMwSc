scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VHistorias/:idPila', {
                controller: 'VHistoriasController',
                templateUrl: 'app/historias/VHistorias.html'
            }).when('/VCrearHistoria/:idPila', {
                controller: 'VCrearHistoriaController',
                templateUrl: 'app/historias/VCrearHistoria.html'
            }).when('/VHistoria/:idHistoria', {
                controller: 'VHistoriaController',
                templateUrl: 'app/historias/VHistoria.html'
            }).when('/VPrelaciones/:idPila', { // CAMBIO idPila -> idHistoria
                controller: 'VPrelacionesController',
                templateUrl: 'app/historias/VPrelaciones.html'
            }).when('/VPrioridades/:idPila', {
                controller: 'VPrioridadesController',
                templateUrl: 'app/historias/VPrioridades.html'
            }).when('/VDiagramaPrelaciones/:idPila', {
                controller: 'VDiagramaPrelacionesController',
                templateUrl: 'app/historias/VDiagramaPrelaciones.html'
            });
});

scrumModule.controller('VHistoriasController',
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'ngTableParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, flash, $routeParams, ngTableParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      historiasService.VHistorias({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var VHistoria0Data = $scope.res.data0;
              if(typeof VHistoria0Data === 'undefined') VHistoria0Data=[];
              $scope.tableParams0 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VHistoria0Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VHistoria0Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });


      });
      $scope.VCrearHistoria1 = function(idPila) {
        $location.path('/VCrearHistoria/'+idPila);
      };
      $scope.VProducto2 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };
      $scope.VPrioridades3 = function(idPila) {
        $location.path('/VPrioridades/'+idPila);
      };
      $scope.VLogin4 = function() {
        $location.path('/VLogin');
      };

      $scope.VHistoria0 = function(idHistoria) {
        $location.path('/VHistoria/'+((typeof idHistoria === 'object')?JSON.stringify(idHistoria):idHistoria));
      };

    }]);
scrumModule.controller('VCrearHistoriaController',
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      $scope.fHistoria = {};

      historiasService.VCrearHistoria({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VHistorias0 = function(idPila) {
        $location.path('/VHistorias/'+idPila);
      };
      $scope.VCrearActor2 = function(idPila) {
        $location.path('/VCrearActor/'+idPila);
      };
      $scope.VCrearAccion3 = function(idPila) {
        $location.path('/VCrearAccion/'+idPila);
      };
      $scope.VCrearObjetivo4 = function(idPila) {
        $location.path('/VCrearObjetivo/'+idPila);
      };
      $scope.VLogin5 = function() {
        $location.path('/VLogin');
      };

      $scope.fHistoriaSubmitted = false;
      $scope.ACrearHistoria1 = function(isValid) {
        $scope.fHistoriaSubmitted = true;
        if (isValid) {

          historiasService.ACrearHistoria($scope.fHistoria).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
scrumModule.controller('VHistoriaController',
   ['$window', '$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'ngTableParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService', 'pruebasService',
    function ($window, $scope, $location, $route, $timeout, flash, $routeParams, ngTableParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService, pruebasService) {
      $scope.msg = '';
      $scope.fHistoria = {};

      historiasService.VHistoria({"idHistoria":$routeParams.idHistoria}).then(function (object) {
        $scope.res = object.data;
        $scope.idHistoria = $routeParams.idHistoria;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var VTarea2Data = $scope.res.data2;
              if(typeof VTarea2Data === 'undefined') VTarea2Data=[];
              $scope.tableParams2 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VTarea2Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VTarea2Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });
              var VPrueba2Data = $scope.res.pruebas;
              if(typeof VPrueba2Data === 'undefined') VPrueba2Data=[];
              $scope.tableParams3 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VPrueba2Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VPrueba2Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });
      });
      $scope.VHistorias3 = function(idPila) {
        $location.path('/VHistorias/'+idPila);
      };
      $scope.VLogin4 = function() {
        $location.path('/VLogin');
      };
      $scope.VCrearTarea5 = function(idHistoria) {
        $location.path('/VCrearTarea/'+idHistoria);
      };
      $scope.VCrearActor6 = function(idPila) {
        $location.path('/VCrearActor/'+idPila);
      };
      $scope.VCrearAccion7 = function(idPila) {
        $location.path('/VCrearAccion/'+idPila);
      };
      $scope.VCrearObjetivo8 = function(idPila) {
        $location.path('/VCrearObjetivo/'+idPila);
      };
      $scope.AElimHistoria9 = function(idHistoria) {

        historiasService.AElimHistoria({"idHistoria":((typeof idHistoria === 'object')?JSON.stringify(idHistoria):idHistoria)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};


      $scope.VDesempeno10 = function(idHistoria) {
        $location.path('/VDesempeno/'+idHistoria);
      };
      $scope.VCrearPrueba11 = function(idHistoria) {
        $location.path('/VCrearPrueba/'+idHistoria);
      };
      $scope.fHistoriaSubmitted = false;
      $scope.AModifHistoria0 = function(isValid) {
        $scope.fHistoriaSubmitted = true;
        if (isValid) {

          historiasService.AModifHistoria($scope.fHistoria).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

      $scope.ACompletarHistoria = function(idHistoria) {
        historiasService.ACompletarHistoria({idHistoria: idHistoria}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });
      };
      $scope.AIncompletarHistoria = function(idHistoria) {
        historiasService.AIncompletarHistoria({idHistoria: idHistoria}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });
      };

      $scope.VTarea2 = function(idTarea, idHistoria) {
          $location.path('/VTarea/'+((typeof idTarea === 'object')?JSON.stringify(idTarea):idTarea)+'/'+((typeof idHistoria === 'object')?JSON.stringify(idHistoria):idHistoria));
      };

      $scope.downloadAcceptanceTest = function (url) {
          $window.location = '/anexo/ADescargar/' + url;
      };

      $scope.AElimPrueba2 = function(idPrueba) {
        pruebasService.AElimPrueba(idPrueba).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();})
          ;};
      }]);
scrumModule.controller('VHistoriasController',
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'ngTableParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, ngTableParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      historiasService.VHistorias({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }


              var VHistoria0Data = $scope.res.data0;
              if(typeof VHistoria0Data === 'undefined') VHistoria0Data=[];
              $scope.tableParams0 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VHistoria0Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VHistoria0Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });


      });
      $scope.VCrearHistoria1 = function(idPila) {
        $location.path('/VCrearHistoria/'+idPila);
      };
      $scope.VProducto2 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };
      $scope.VPrioridades3 = function(idPila) {
        $location.path('/VPrioridades/'+idPila);
      };
      $scope.VLogin4 = function() {
        $location.path('/VLogin');
      };
      $scope.VPrelaciones5 = function(idPila) {  // CAMBIO idPila -> idHistoria
        $location.path('/VPrelaciones/'+idPila);
      };
      $scope.VHistoria0 = function(idHistoria) {
        $location.path('/VHistoria/'+((typeof idHistoria === 'object')?JSON.stringify(idHistoria):idHistoria));
      };

    }]);
scrumModule.controller('VPrelacionesController',
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      $scope.fPrelaciones = {};

      historiasService.VPrelaciones({"idPila":$routeParams.idPila}).then(function (object) { // CAMBIO idPila -> idHistoria
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }

$scope.agrPrelacion = function () {
  $scope.fPrelaciones.lista.push({antecedente:null, consecuente:null})
}
$scope.elimPrelacion = function (index) {
  $scope.fPrelaciones.lista.splice(index, 1);
}

      });

      $scope.VDiagramaPrelaciones6 = function(idPila) { 
        $location.path('/VDiagramaPrelaciones/'+idPila);
      };

      $scope.VHistorias1 = function(idPila) {
        $location.path('/VHistorias/'+idPila);
      };

      $scope.fPrelacionesSubmitted = false;
      $scope.APrelaciones0 = function(isValid) {
        $scope.fPrelacionesSubmitted = true;
        if (isValid) {

          historiasService.APrelaciones($scope.fPrelaciones).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
scrumModule.controller('VDiagramaPrelacionesController',
    ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'ngTableParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, ngTableParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      historiasService.VDiagramaPrelaciones({"idPila":$routeParams.idPila}).then(function (object) { 
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }

              var VHistoria3Data = $scope.res.data;
              if(typeof VHistoria3Data === 'undefined') VHistoria3Data=[];
              $scope.tableParams3 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VHistoria3Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VHistoria3Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });

      });

      $scope.VPrelaciones1 = function(idPila) {
        $location.path('/VPrelaciones/'+idPila);
      };
      $scope.VLogin4 = function() {
        $location.path('/VLogin');
      };

    }]);


scrumModule.controller('VPrioridadesController',
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      $scope.fPrioridades = {};

      historiasService.VPrioridades({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VHistorias1 = function(idPila) {
        $location.path('/VHistorias/'+idPila);
      };
      $scope.VLogin2 = function() {
        $location.path('/VLogin');
      };

      $scope.fPrioridadesSubmitted = false;
      $scope.ACambiarPrioridades0 = function(isValid) {
        $scope.fPrioridadesSubmitted = true;
        if (isValid) {

          historiasService.ACambiarPrioridades($scope.fPrioridades).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
