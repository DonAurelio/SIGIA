/* 
    FORM JQuery Submit 
    Copied from http://formvalidation.io/examples/ajax-submit/ 

*/
$("button").click(function ( event ){
    event.preventDefault();
    var $form = $("form");
    $form.ajaxSubmit({
        // You can change the url option to desired target
        url: $form.attr('action'),
        dataType: 'html',
        success: function(responseText, statusText, xhr, $form) {
            $("#content").html(responseText);
            // Process the response returned by the server ...
            // console.log(responseText);
        }
    });
});