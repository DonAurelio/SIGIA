$("#vincular-vehiculo").click(function (event) {
	var address = "/parciales" + window.location.pathname;
	alert(address);
    $.get(address, function(data, status){
    	$(".modal-body").html(data);
	});
});