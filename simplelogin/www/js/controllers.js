angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope) {})

.controller('WorkOrderCtrl', function($scope, WorkOrdersService, Chats, $localstorage) {
  WorkOrdersService
    .getWorkOrders($localstorage.get('cliente_id'))
    .then(success,error);

  function success(data) {
    console.log("success");
    $scope.orders = data.data;
    console.log($scope.orders);
  };
  function error(data) {
      //your code when fails
      console.log("error");
      
  };
  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  };
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('LoginCtrl', function($scope, $location, $localstorage, ValidateService) {
    $scope.data = {};

    $scope.login = function() {
        // $scope.data.email = validateService.validate($scope.data.email, $scope.data.identificacion);
        ValidateService
          .validate($scope.data.email, $scope.data.identificacion)
          .then(success, error);
        function success(data) {
            console.log("success");
            console.log(data.data);
            if (data.data.valido == true){
              // To add to local storage
              $localstorage.set('cliente_id', data.data.cliente_id);
              $location.url("/tab/workorder");
            }
        };
        function error(data) {
            //your code when fails
            console.log("error");

        };
    }
})

.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };


});
