
    $(document).ready(function(){
        $('.table').DataTable();
    

    $("#btn-nuevo").click(function(event){
        event.preventDefault();
        $.ajax({
            type: 'GET',
            url: $(this).attr('href'),
            dataType: 'json',
            success: function (data) {
                $("#sucursal-modal-body").html(data.html);
                $("#sucursal-modal").modal("toggle");
            }
        });
    });

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
            }
        });
    });
});