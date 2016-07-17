// FUNCTIONS TO BE RUN AFTER PAGE HAS LOADED
$(document).ready(function() {   

//TEXT CHARACTER COUNT
var text_max = 500;
$('#count_message').html(text_max + ' characters remaining');
$('#msg').keyup(function() {
    var text_length = $('#msg').val().length;
    var text_remaining = text_max - text_length;
    $('#count_message').html(text_remaining + ' characters remaining');
});
//END OF CHARACTER COUNT

// BACK TO TOP BUTTON
// browser window scroll (in pixels) after which the "back to top" link is shown
var offset = 100,
  //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
  offset_opacity = 2000, //1200px??
  //duration of the top scrolling animation (in ms)
  scroll_top_duration = 700,
  //grab the "back to top" link
  $back_to_top = $('.cd-top');

//hide or show the "back to top" link
$(window).scroll(function(){
  ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
  if( $(this).scrollTop() > offset_opacity ) { 
    $back_to_top.addClass('cd-fade-out');
  }
});

//smooth scroll to top
$back_to_top.on('click', function(event){
  event.preventDefault();
  $('body,html').animate({
    scrollTop: 0 ,
    }, scroll_top_duration
  );
});
// END OF BACK TO TOP BUTTON
        
});
// END OF FUNCTIONS TO BE RUN AFTER PAGE LOADS