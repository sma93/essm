$(function() {
	$.get( "http://api.adviceslip.com/advice", function( data ) {
	  data = JSON.parse(data);
	  $( "#advice-section" ).html(data.slip.advice);
	})
	$.get( "http://api.adviceslip.com/advice", function( data ) {
	  data = JSON.parse(data);
	  $( "#advice-section-2" ).html(data.slip.advice);
	})

	$('.top.menu .item').tab();
});
