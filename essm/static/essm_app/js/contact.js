$(function() {
  $("#test").click(function() {
    $(".test").modal('show');
  });
  $(".test").modal({
    closable: true
  });
});
$('#my-button').click(function() {
  $.post('comments', function(data) {
    console.log(data);
  });
})

// var dummy_data = {
//   Items: [{
//     Attributes: [{
//       Name: "submit_date",
//       Value: "1489703867.53"
//     }, {
//       Name: "text",
//       Value: "This is the coolest website ever!"
//     }]
//   }]
// }
//
// $.get('dummy', function(data) {
//   //TODO: create separate templates/urls for testing with/without actual db calls
//   //$.get('blog_posts', function(data) {
//   console.log(data);
//   data = dummy_data;
//   //data = data;
//   console.log(data);
//
// var commentDate = data.Items["0"].Attributes["0"].Value,
//   commentText = data.Items["0"].Attributes["1"].Value,
// //display get results on the page
// //TODO: do not display rest of page until this is ready...remove jarring UI somehow
// $('#test-content').html(commentText);
// $('#author-date').html('</br>submit Data: ' + commentDate);
// })
