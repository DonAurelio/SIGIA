$(document).ready(function(){
    /* Incializacion DataTable */
    $('.table').DataTable();
    
    /* Creacion de sucursal */
    $("#btn-nuevo").click(function(event){
        event.preventDefault();
        
        var $form = $("form");
        $form.attr('action','/sucursal/crear');
        $("#sucursal-modal-title").html("Nueva Sucursal");
        $("#submit").show();

        $.ajax({
            type: 'GET',
            url: $form.attr('action'),
            dataType: 'json',
            success: function (data) {

                $("#sucursal-modal-body").html(data.html);
                $("#sucursal-modal").modal("toggle");
            },
            error: error
        });
    });

    /* Actualización de sucursal */
    $(".update").click(function(event){
        event.preventDefault();

        var $form = $("form");
        $form.attr('action',$(this).attr("href"));
        $("#sucursal-modal-title").html("Actualizar Sucursal");
        $("#submit").show();
        
        $.ajax({
            type: 'GET',
            url: $(this).attr("href"),
            dataType: 'json',
            success: function (data) {

                $("#sucursal-modal-body").html(data.html);
                $("#sucursal-modal").modal("toggle");
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
                    $("#sucursal-modal").modal("toggle");
                }else{
                    $("#sucursal-modal-body").html(response.html);
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
                            por favor verifique el archivo apps.sucursal.js \
                        <span class="close" data-dismiss="alert">&times;</span> \
                    </div>';

        $("#dialog-modal-body").html(html);
        $("#dialog").modal("toggle");
        
    }
});