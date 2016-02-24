angular.module('starter.services', [])

.factory('ValidateService', function( $http ) {
  client = {};
  client.id = null;
  client.validate = validate;

  return client

  function validate(email, id) {
    //http://stackoverflow.com/questions/22476273/no-access-control-allow-origin-header-is-present-on-the-requested-resource-i
    var url = ("http://127.0.0.1:8000/validar/"+email+"/"+id+"/");
    return $http({method: 'GET', url: url});
  }
})

.factory('WorkOrdersService',function( $http ){
  client = {};
  client.getWorkOrders = getWorkOrders;

  return client

  function getWorkOrders(id){
    var url = ("http://127.0.0.1:8000/ordenesdetrabajo/"+id+"/json/");
    return $http({method: 'GET', url: url});
  }
  
})



.factory('Chats', function() {
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var chats = [{
    id: 0,
    name: 'Ben Sparrow',
    lastText: 'You on your way?',
    face: 'img/ben.png'
  }, {
    id: 1,
    name: 'Max Lynx',
    lastText: 'Hey, it\'s me',
    face: 'img/max.png'
  }, {
    id: 2,
    name: 'Adam Bradleyson',
    lastText: 'I should buy a boat',
    face: 'img/adam.jpg'
  }, {
    id: 3,
    name: 'Perry Governor',
    lastText: 'Look at my mukluks!',
    face: 'img/perry.png'
  }, {
    id: 4,
    name: 'Mike Harrington',
    lastText: 'This is wicked good ice cream.',
    face: 'img/mike.png'
  }];

  return {
    all: function() {
      return chats;
    },
    remove: function(chat) {
      chats.splice(chats.indexOf(chat), 1);
    },
    get: function(chatId) {
      for (var i = 0; i < chats.length; i++) {
        if (chats[i].id === parseInt(chatId)) {
          return chats[i];
        }
      }
      return null;
    }
  };
});
