$("button").click(function(event){
	event.preventDefault();
    $.post("/sucursal/crear",
    {
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        nombre:$("#id_nombre").val(),
        direccion:$("#id_direccion").val(),
        telefono:$("#id_telefono").val(),
        ciudad:$("#id_ciudad").val(),
        habilitado:$("#id_habilitado").val(),
    }
    ,
    function(data, status){
        $("#content").html(data);
    }).done(function() {
        alert( "La peticion post se realizo con exito" );
    })
    .fail(function() {
        alert( "Ha ocurrido un error al hacer la peticion post" );
    });
    //.always(function() {
    //    alert( "finished" );
    //});
});