angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope) {})

.controller('WorkOrderCtrl', function($scope, WorkOrdersService, $localstorage) {
  WorkOrdersService
    .getWorkOrders($localstorage.get('cliente_id'))
    .then(success,error);
  function success(data) {
    $scope.orders = data.data;
    $localstorage.setObject('orders', data.data);
    console.log(data.data);
  };
  function error(data) {
    var alertPopup = $ionicPopup.alert({
      title: 'Error',
      template: 'Se ha producido un error inesperado. Por favor, compruebe su conexión',
      buttons: [{
        text:'Aceptar',
        type: 'button-assertive'
      }]
    });
  };
})

.controller('WorkOrderDetailCtrl', function($scope, $stateParams, $localstorage, WorkOrdersService) {
  order = WorkOrdersService.getByID($localstorage.getObject('orders'),$stateParams.orderId);
  $scope.order = order;
})

.controller('LoginCtrl', function($scope, $location, $localstorage, ValidateService, $ionicPopup) {
    $scope.data = {};
    $scope.login = function() {
        // $scope.data.email = validateService.validate($scope.data.email, $scope.data.identificacion);
        ValidateService
          .validate($scope.data.email, $scope.data.identificacion)
          .then(success, error);
        function success(data) {
            if (data.data.valido == true){
              console.log("Success");
              console.log(data.data.cliente_id);
              $localstorage.set('cliente_id', data.data.cliente_id);
              $location.url("/tab/workorder");
            }
            else {
              var alertPopup = $ionicPopup.alert({
               title: 'Alerta!',
               template: 'No coincide el email y/o número de identificación',
               buttons: [{
                  text:'Aceptar',
                  type: 'button-balanced'
                }]
             });
            }
        };
        function error(data) {
          console.log("Error");
          console.log(data.data);
          var alertPopup = $ionicPopup.alert({
            title: 'Error',
            template: 'Se ha producido un error inesperado. Por favor, compruebe su conexión',
            buttons: [{
              text:'Aceptar',
              type: 'button-assertive'
            }]
          });
        };
    };
});
