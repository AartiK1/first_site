

// FUNCTIONS TO BE RUN AFTER PAGE HAS LOADED
$(document).ready(function() {   



/* LHS nav scrolls only to top of footer. Doesn't overlap */
var doc = $(document); 
doc.scroll(function () {
     // make sure to wrap yours entire footer in some css selector
    var footer = $('#whole-ft');
    var p = $('#nav-fixed');
    var s = $('#left-nav-position');

    var top = doc.scrollTop() + s.offset().top  * 1.95 + p.height();
    var footerTop = footer.offset().top;

    var offset = footerTop - top;

    if (offset < 0) {
        p.css({'margin-top': '' + offset + 'px'});
    } else {
        p.css({'margin-top': 0});
    }
});
/* End of LHS nav scroll */


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


//FUNCTIONS TO BE RUN BEFORE PAGE HAS LOADED

//Allows only numbers
//charCode values can be found here: http://stevehardie.com/2009/09/character-code-list-char-code/ 
//Used charCode to limit input to only numbers and + symbol
// || means OR
// && means AND
function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if ((charCode > 31 && charCode < 43) || (charCode > 43 && (charCode < 48 || charCode > 57)))
        return false;
    return true;
}

//Allows only letters
//Used charCode to limit input to only letters and hyphens
function isAlphaKey(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if ((charCode > 32 && charCode < 45) || (charCode > 45 && charCode < 65) || (charCode > 90 && charCode < 97) || (charCode > 122))
        return false;
    return true;
}
