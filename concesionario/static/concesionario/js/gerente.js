/* Get HTML data form menu items using the href atrribute of the clicked button */
/*$("li > a").click(function (event) {
	event.preventDefault();
    var addressValue = $(this).attr("href");
    $.get(addressValue, function(data, status){
		$("#content").html(data);
	});
});
*/
$("a").click(function (event) {
	event.preventDefault();
    var addressValue = $(this).attr("href");
    $.get(addressValue, function(data, status){
		$("#content").html(data);
	});
});

$("button").click(function(event){
	event.preventDefault();
    $.post("/sucursal/crear",
    $("#content").html()
    ,
    function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });
});