$(function() {
  $("#test").click(function() {
    $(".test").modal('show');
  });
  $(".test").modal({
    closable: true
  });
});

$('#submit-button').click(function() {
  console.log($('#post-title').val());
  console.log($('#post-text').val());
  $.post("http://127.0.0.1:8000/essm_app/blog_posts", {
      title: $('#post-title').val(),
      author: "essm",
      text: $('#post-text').val()
    })
    .done(function(data) {
      console.log(data);
    })
})

// from https://docs.djangoproject.com/en/1.10/ref/csrf/
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});
