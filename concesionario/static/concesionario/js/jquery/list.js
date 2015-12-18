/* Outside table button */
$("div > a").click(function (event) {
	event.preventDefault();
	var addressValue = $(this).attr("href");
    $.get(addressValue, function(data, status){
		$("#content").html(data);
	});
});

/* Inside Table urls */
$("td > a").click(function (event) {
	event.preventDefault();
    var addressValue = $(this).attr("href");
    $.get(addressValue, function(data, status){
		$("#content").html(data);
	});
});