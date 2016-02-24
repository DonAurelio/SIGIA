angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope) {})

.controller('WorkOrderCtrl', function($scope, ValidateService, WorkOrdersService, Chats) {
  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //
  //$scope.$on('$ionicView.enter', function(e) {
  //});
  $scope.client = ValidateService;
  console.log($scope.client.id);

  WorkOrdersService
    .getWorkOrders($scope.client.id)
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
  console.log($scope.chats);
  $scope.remove = function(chat) {
    Chats.remove(chat);
  };
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('LoginCtrl', function($scope, ValidateService, $location) {
    $scope.data = {};
    $scope.client = ValidateService;
 
    $scope.login = function() {
        // $scope.data.email = validateService.validate($scope.data.email, $scope.data.identificacion);
        ValidateService
          .validate($scope.data.email, $scope.data.identificacion)
          .then(success, error);

        function success(data) {
            
            console.log("success");
            console.log(data.data);
            if (data.data.valido == true){
              //$scope.cliente_id = data.data.cliente_id;
              $scope.client.id = data.data.cliente_id;
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