scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VProductos', {
                controller: 'VProductosController',
                templateUrl: 'app/prod/VProductos.html'
            }).when('/VProducto/:idPila', {
                controller: 'VProductoController',
                templateUrl: 'app/prod/VProducto.html'
            }).when('/VCrearProducto', {
                controller: 'VCrearProductoController',
                templateUrl: 'app/prod/VCrearProducto.html'
            });
});

scrumModule.controller('VProductosController',
   ['$scope', '$location', '$route', 'flash', 'ngTableParams', 'accionService', 'actorService', 'catesService', 'historiasService', 'identService', 'objetivoService', 'prodService',
    function ($scope, $location, $route, flash, ngTableParams, accionService, actorService, catesService, historiasService, identService, objetivoService, prodService) {
      $scope.msg = '';
      prodService.VProductos().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var VProducto0Data = $scope.res.data0;
              if(typeof VProducto0Data === 'undefined') VProducto0Data=[];
              $scope.tableParams0 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VProducto0Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VProducto0Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });


      });
      $scope.VCrearProducto1 = function() {
        $location.path('/VCrearProducto');
      };
      $scope.VCategorias2 = function() {
        $location.path('/VCategorias');
      };
      $scope.VLogin3 = function() {
        $location.path('/VLogin');
      };

      $scope.VProducto0 = function(idPila) {
        $location.path('/VProducto/'+((typeof idPila === 'object')?JSON.stringify(idPila):idPila));
      };

      $scope.ARespaldo = function(idPila) {
        prodService.ARespaldo(idPila).then(function (object) {
          console.log('Success')
          var json = JSON.parse(object.data.respaldo)
          var url = 'data:application/octet-stream;charset=utf8,' + encodeURIComponent(object.data.respaldo);
          var link = document.createElement("a");
          link.href = url;

          //set the visibility hidden so it will not effect on your web-layout
          link.style = "visibility:hidden";
          link.download = "Respaldo - " + json.nombre + ".json";

          //this part will append the anchor tag and remove it after automatic click
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        })
      }

    }]);
scrumModule.controller('VProductoController',
   ['$window', '$timeout', '$scope', '$location', '$route', 'flash', '$routeParams', 'ngTableParams', 'accionService', 'actorService', 'catesService', 'historiasService', 'identService', 'objetivoService', 'prodService',
    function ($window, $timeout, $scope, $location, $route, flash, $routeParams, ngTableParams, accionService, actorService, catesService, historiasService, identService, objetivoService, prodService) {
      $scope.msg = '';
      $scope.fPila = {};

      prodService.VProducto({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        $scope.backlogId = $routeParams.nombrePila;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var VActor3Data = $scope.res.data3;
              if(typeof VActor3Data === 'undefined') VActor3Data=[];
              $scope.tableParams3 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VActor3Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VActor3Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });

              var VAccion5Data = $scope.res.data5;
              if(typeof VAccion5Data === 'undefined') VAccion5Data=[];
              $scope.tableParams5 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VAccion5Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VAccion5Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });

              var VObjetivo7Data = $scope.res.data7;
              if(typeof VObjetivo7Data === 'undefined') VObjetivo7Data=[];
              $scope.tableParams7 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VObjetivo7Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VObjetivo7Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });

              // estos son los files
              var VFiles9Data = $scope.res.data9;
              if(typeof VFiles9Data === 'undefined') VFiles9Data=[];
              $scope.tableParams9 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VFiles9Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VFiles9Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });


      });
      $scope.VProductos1 = function() {
        $location.path('/VProductos');
      };
      $scope.VLogin8 = function() {
        $location.path('/VLogin');
      };
      $scope.VCrearActor9 = function(idPila) {
        $location.path('/VCrearActor/'+idPila);
      };
      $scope.VCrearAccion10 = function(idPila) {
        $location.path('/VCrearAccion/'+idPila);
      };
      $scope.VCrearObjetivo11 = function(idPila) {
        $location.path('/VCrearObjetivo/'+idPila);
      };
      $scope.VHistorias12 = function(idPila) {
        $location.path('/VHistorias/'+idPila);
      };
      $scope.VAnexo13 = function(idPila) {
        $location.path('/VAnexo/'+idPila);
      };
      $scope.VSprints14 = function(idPila) {
        $location.path('/VSprints/'+idPila);
      };
      $scope.VEquipo15 = function(idPila) {
        $location.path('/VEquipo/'+idPila);
      };
      $scope.VCrearDocumento16 = function(idPila) {
        $location.path('/VCrearDocumento/'+idPila);
      };

      $scope.fPilaSubmitted = false;
      $scope.AModifProducto0 = function(isValid) {
        $scope.fPilaSubmitted = true;
        if (isValid) {

          prodService.AModifProducto($scope.fPila).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

      $scope.VActor3 = function(idActor) {
        $location.path('/VActor/'+((typeof idActor === 'object')?JSON.stringify(idActor):idActor));
      };
      $scope.VAccion5 = function(idAccion) {
        $location.path('/VAccion/'+((typeof idAccion === 'object')?JSON.stringify(idAccion):idAccion));
      };
      $scope.VObjetivo7 = function(idObjetivo) {
        $location.path('/VObjetivo/'+((typeof idObjetivo === 'object')?JSON.stringify(idObjetivo):idObjetivo));
      };

    }]);
scrumModule.controller('VCrearProductoController',
   ['$scope', '$location', '$route', 'flash', 'accionService', 'actorService', 'catesService', 'historiasService', 'identService', 'objetivoService', 'prodService',
    function ($scope, $location, $route, flash, accionService, actorService, catesService, historiasService, identService, objetivoService, prodService) {
      $scope.msg = '';
      $scope.fPila = {};

      prodService.VCrearProducto().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VProductos1 = function() {
        $location.path('/VProductos');
      };
      $scope.VLogin2 = function() {
        $location.path('/VLogin');
      };

      $scope.fPilaSubmitted = false;
      $scope.ACrearProducto0 = function(isValid) {
        $scope.fPilaSubmitted = true;
        if (isValid) {

          prodService.ACrearProducto($scope.fPila).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
