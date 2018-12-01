$(function() {
  $("#start").bind('click', function(event) {
    event.preventDefault();
    var formData = $('input[name=keyword]').val();
    var url = '/search/';
    $.ajax({
      method: 'POST',
      url: url,
      data: formData,
      dataType: 'json',
      success: function(res) {
        console.log('success message >>>' + res);
      },
      error: function(res) {
        console.log('failed message >>>' + res);
      }
    })
  });
});
