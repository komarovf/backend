head.ready(function() {
// $(document).on("click", function(){
// $(".js-popup").hide();
// });
// function scrollFixedElements() {
// var scroll_left = $(this).scrollLeft();
// $(".fixed-element").css({
// left: -scroll_left
// });
// }
// scrollFixedElements();
// $(window).scroll(function(){
// scrollFixedElements()
// });
(document).ready(function() {
$('.menu').addClass('open');
('.bt-nav').click( function() {
$(this).parent().toggleClass( function() {
if ( $(this).hasClass('open') ) {
return 'close';
} else
if ( $(this).hasClass('close') ) {
return 'open';
}
});
});
});
console.log($('body').html());
});