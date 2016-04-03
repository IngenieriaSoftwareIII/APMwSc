// Creación del módulo de la aplicación
var scrumModule = angular.module('scrum', ['ngRoute', 'ngAnimate', 'ngTable', 'textAngular', 'flash','googlechart']);
scrumModule.config(function ($routeProvider) {
    $routeProvider
        .when('/', {
                controller: 'VLoginController',
                templateUrl: 'app/ident/VLogin.html'
            });
});
scrumModule.controller('scrumController_',  ['$scope', '$http', '$location',
function($scope) {
    $scope.title = "APMwSc:\nA supporting tool the process of\nAgile Project Management with Scrum";
}]);
scrumModule.directive('sameAs', [function () {
    return {
        restrict: 'A',
        scope:true,
        require: 'ngModel',
        link: function (scope, elem , attrs, control) {
            var checker = function () {
                //get the value of the this field
                var e1 = scope.$eval(attrs.ngModel); 
 
                //get the value of the other field
                var e2 = scope.$eval(attrs.sameAs);
                return e1 == e2;
            };
            scope.$watch(checker, function (n) {
 
                //set the form control to valid if both 
                //fields are the same, else invalid
                control.$setValidity("unique", n);
            });
        }
    };
}]);

scrumModule.directive('fileModel', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;
            
            element.bind('change', function(){
                scope.$apply(function(){
                    modelSetter(scope, element[0].files[0]);
                });
            });
        }
    };
}]);