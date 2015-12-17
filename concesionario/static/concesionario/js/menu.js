$("div > ul > li > a").click(function (event) {
	event.preventDefault();
    var addressValue = $(this).attr("href");
    $.get(addressValue, function(data, status){
		$("#content").html(data);
	});
});


