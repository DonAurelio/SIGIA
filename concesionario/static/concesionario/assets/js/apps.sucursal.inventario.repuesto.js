function listeners(){
  /* Incializacion DataTable */
  $('.table').DataTable();

  /* Agregar repuesto al inventario de una sucursal*/
  $("body").on('click', ".create", function(event){
      event.preventDefault();

      var $form = $("form");
      var url = $(this).attr('href');

      $form.attr('action',url);
      $("#replacement-modal-title").html("Nuevo Repuesto en Inventario");
      $("#submit").show();

      $.ajax({
          type: 'GET',
          url: $form.attr('action'),
          dataType: 'json',
          success: function (data) {
              $("#replacement-modal-body").html(data.html);
              $("#replacement-modal").modal("toggle");
          },
          error: error
      });
  });

  /* Actualización de un repuesto del inventario de la sucursal */
  $("body").on('click',".update", function(event){
      event.preventDefault();

      var $form = $("form");
      $form.attr('action',$(this).attr("href"));
      $("#replacement-modal-title").html("Actualizar Repuesto en Inventario");
      $("#submit").show();

      $.ajax({
          type: 'GET',
          url: $(this).attr("href"),
          dataType: 'json',
          success: function (data) {

              $("#replacement-modal-body").html(data.html);
              $("#replacement-modal").modal("toggle");
          },
          error: error
      });
  });

  /* submit del formulario */
  $("#submit").click(function(event){
      event.preventDefault();
      var $form = $("form");
      $form.ajaxSubmit({
          url: $form.attr('action'),
          dataType: 'json',
          success: function(response, status, xhr, $form) {
              if(response.status==true){
                  $("#section-content").html(response.html);
                  $('.table').DataTable();
                  $("#replacement-modal").modal("toggle");
              }else{
                  $("#replacement-modal-body").html(response.html);
              };
          },
          error: error
      });
  });



  /* Aviso de error  */
  var error = function (data) {
      var html = '<div class="alert alert-danger fade in m-b-15"> \
                      <strong>Error!</strong> \
                          Se ha presentado un error al intentar obtener información del servidor, \
                          por favor verifique el archivo apps.sucursal.inventario.repuesto.js \
                      <span class="close" data-dismiss="alert">&times;</span> \
                  </div>';

      $("#dialog-modal-body").html(html);
      $("#dialog").modal("toggle");

  }
}

$(document).ready(function(){
  listeners();
});
