angular.module('starter.services', [])

.factory('ValidateService', function( $http ) {
    return {
      validate: function (email, id) {
        var url = ("http://127.0.0.1:8000/validar/"+email+"/"+id+"/");
        return $http({method: 'GET', url: url});
      }
    }
})

.factory('WorkOrdersService',function( $http ){
  return {
    getWorkOrders: function(id){
      var url = ("http://127.0.0.1:8000/ordenesdetrabajo/"+id+"/json/");
      return $http({method: 'GET', url: url});
    },
    getByID: function(orders, workOrderId) {
      for (var i = 0; i < orders.length; i++) {
        if (orders[i].id === parseInt(workOrderId)) {
          return orders[i];
        }
      }
      return null;
    }
  }
})
  
.factory('$localstorage', ['$window', function($window) {
  return {
    set: function(key, value) {
      $window.localStorage[key] = value;
    },
    get: function(key, defaultValue) {
      return $window.localStorage[key] || defaultValue;
    },
    setObject: function(key, value) {
      $window.localStorage[key] = JSON.stringify(value);
    },
    getObject: function(key) {
      return JSON.parse($window.localStorage[key] || '{}');
    }
  }
}]);
