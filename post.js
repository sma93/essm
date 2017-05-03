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
})
