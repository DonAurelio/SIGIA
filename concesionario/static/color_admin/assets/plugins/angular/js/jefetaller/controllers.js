var concesionarioApp = angular.module('concesionarioApp',[]);

concesionarioApp.controller('ordentrabajoCtrl', function ($scope,$http) {
  $scope.text = "Hello";
  // Simple GET request example:
  $http({
    method: 'GET',
    url: '/ordenesdetrabajo/'
  }).then(function successCallback(response) {
      // this callback will be called asynchronously
      // when the response is available
      alert(response.data[0].fields.vehiculo);
      $scope.ordenes = response.data;
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
      alert("Error");
    });

});
