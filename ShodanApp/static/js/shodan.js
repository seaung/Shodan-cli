$(function() {
    $('#search-btn').bind('click', function(event) {
        event.preventDefault();
        var $url = "/search";
        var $value = $('#kw').val();
        var $data = {keyword: $value};
        var $dataType = "json"
        var $method = "POST";
        $.ajax({
            type: $method,
            url: $url,
            data: $data,
            dataType: $dataType,
            success: function(data) {
                console.log('success =>', data);
            },
            error: function(data) {
                console.log('errors =>', data);
            }
        });
    });
});
