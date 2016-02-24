angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope) {})

.controller('ChatsCtrl', function($scope, Chats) {
  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  };
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('LoginCtrl', function($scope, validateService, $location) {
    $scope.data = {};
 
    $scope.login = function() {
        // $scope.data.email = validateService.validate($scope.data.email, $scope.data.identificacion);
        validateService.validate($scope.data.email, $scope.data.identificacion).then(success, error);

        function success(data) {
            
            console.log("success");
            console.log(data.data);
            if (data.data.valido == true){

              $location.url("/account");
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
