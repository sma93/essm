$(function() {
  $("#test").click(function() {
    $(".test").modal('show');
  });
  $(".test").modal({
    closable: true
  });
});
$('#my-button').click(function() {
  $.post('blog_posts', function(data) {
    console.log(data);
  });
})
//$("#write").delay(5000).show(0);
$(document).ready(function() {
  setTimeout(function() {
    $("#write").show();
  }, 2000);
});

var dummy_data = {
  Items: [{
    Attributes: [{
      Name: "last-modified",
      Value: "1489703867.53"
    }, {
      Name: "author",
      Value: "da big boss"
    }, {
      Name: "text",
      Value: "It's a Sunday afternoon, you are sitting at home pondering the question of how does one master the art of self-expression, as usual. You decide that you want to create a website about yourself, because you feel the need to share how excited you get when the food cart comes towards you on an airplane or share how unsustainably nice your handwriting is on the first page of a new notebook. These are things the world deserves to know. Unfortunately, you do not know anything about website design. Words like css and javascript makes you feel like you just want to forget about this whole thing and search up some funny challenge videos on Youtube. Fortunately, your coolest pal E calls you up and by miracle happens to be interested in web design as well. Thus begins the journey of two young souls..."
    }, {
      Name: "title",
      Value: "I want to make a website - the origin story"
    }]
  }]
}
$.get('dummy', function(data) {
  //TODO: create separate templates/urls for testing with/without actual db calls
  //$.get('blog_posts', function(data) {
  console.log(data);
  data = dummy_data;
  //data = data;
  console.log(data);

  var lastModDate = data.Items["0"].Attributes["0"].Value,
    author = data.Items["0"].Attributes["1"].Value,
    text = data.Items["0"].Attributes["2"].Value,
    title = data.Items["0"].Attributes["3"].Value;
  //display get results on the page
  //TODO: do not display rest of page until this is ready...remove jarring UI somehow
  $('#test-header').html(title);
  $('#test-content').html(text);
  $('#author-date').html('author: ' + author + '</br>last mod: ' + lastModDate);
})
