$(document).ready(function(){
    /* Incializacion DataTable */
    $('.table').DataTable();
    
    /* Agregar sucursal al inventario */
    $(".create").click(function(event){
        event.preventDefault();
        
        var $form = $("form");

        //Se obtiene la url del vehiculo a agergar a la sucursal
        var url = $(this).attr('href');
        alert(url);
        //Se modifica el atributo action del formulario 
        $form.attr('action',url);

        //Se cambia el titulo del modal
        $("#inventory-modal-title").html("Nuevo Vehiculo en Inventario");
        //Se activa el boton de submit
        $("#submit").show();

        //Se trae el formulario del servidor 
        $.ajax({
            type: 'GET',
            url: $form.attr('action'),
            dataType: 'json',
            success: function (data) {
                $("#inventory-modal-body").html(data.html);
                $("#inventory-modal").modal("toggle");
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
                            por favor verifique el archivo apps.sucursal.inventario.js \
                        <span class="close" data-dismiss="alert">&times;</span> \
                    </div>';

        $("#dialog-modal-body").html(html);
        $("#dialog").modal("toggle");
        
    }
});