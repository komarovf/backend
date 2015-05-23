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
$(document).ready(function() {
$('.menu').addClass('open');
$('.bt-nav').click( function() {
$(this).parent().toggleClass( function() {
if ( $(this).hasClass('open') ) {
return 'close';
} else
if ( $(this).hasClass('close') ) {
return 'open';
}
});
});
//plavnoe perelist
$(document).on('click', '#new', function () {
$('html, body').animate({ scrollTop: $('#new__contant').offset().top }, 3000 );
return false;
});
});
// *** конец скрипта "Плавное перелистывание"
// FORM VALIDATION
$(document).ready(function() {
function validate() {
$('.js-validate').each(function(){
if ($(this).length > 0) {
$(this).validate({
errorClass: 'has-error',
rules: {
username: {
minlength: 2
},
any: {
minlength: 2
},
password: {
minlength: 5
},
confirm_password: {
minlength: 5,
equalTo: '#password'
},
email: {
email: true
},
tel: {
minlength: 5,
},
address: {
minlength: 2
},
message: {
minlength: 4
},
field: {
required: true
},
text_area:{
minlength: 4
}
// fruit: {
// required: true
// }
},
messages: {
firstname: 'Вас так зовут?',
lastname: 'У вас такая фамилия?',
fathername: 'У вас такое отчество?',
password: {
required: 'Введите пароль',
minlength: 'Минимум 5 символов'
},
confirm_password: {
required: 'Пароли не совпадают',
minlength: 'Минимум 5 символов',
equalTo: 'Пароли не совпадают'
},
email: '* Неверный формат',
address: 'Это Ваш адрес?',
any: 'Заполните поле',
company: 'Заполните поле',
tel: {
required: '* Введите Ваш терефон',
minlength: 'Минимум 5 символов'
},
username: {
required: '* Введите Ваше имя',
},
message: {
required: 'Заполните поле',
minlength: 'Заполните поле',
},
text_area: {
required: '* Заполните поле',
minlength: 'Заполните поле'
}
}
});
}
});
}
validate();
});
// end FORM VALIDATION
// селект
$(document).ready(function() {
$(document).click(function() {
$(".js-drop ul").hide();
$(".js-select-list").hide();
$(".js-select").removeClass("is-active");
});
function drop_list() {
var drop = $(".js-drop");
drop.bind("click", function(event) {
$(this).find("ul").slideToggle("fast");
event.stopPropagation();
});
drop.find("li").bind("click", function(){
var id = $(this).attr("data-id");
var text = $(this).text();
$(this).parents(drop).find("button span").text(text);
$(this).parents(drop).find("input").val(id);
});
};
drop_list();
});
// ***** слайдер проворачивающий экземпляры сайтов ****
console.log($('body').html());
});
$(document).ready(function(){
$('.js-carousel').slick({
slidesToShow: 1,
slidesToScroll: 1,
arrows: false,
fade: true,
asNavFor: '.js-carousel-preview',
responsive: [
{
breakpoint: 758,
settings: {
slidesToShow: 1,
slidesToScroll: 1,
dots: true,
fade: false,
}
}
]
});
$('.js-carousel-preview').slick({
slidesToShow: 4,
slidesToScroll: 4,
asNavFor: '.js-carousel',
dots: false,
arrows: true,
infinite: true,
centerMode: false,
focusOnSelect: true,
responsive: [
{
breakpoint: 980,
settings: {
slidesToShow: 6,
slidesToScroll: 6
}
}
]
});
$(".js-carousel-preview .slick-slide").on("click",function (){
$(this).parent().find(".slick-slide").removeClass("is-active");
$(this).addClass("is-active")
return false;
});
});
// ##### Карта start ######
var myMap;
// Дождёмся загрузки API и готовности DOM.
ymaps.ready(init);
function init () {
// Создание экземпляра карты и его привязка к контейнеру с
// заданным id ("map").
myMap = new ymaps.Map('map', {
// При инициализации карты обязательно нужно указать
// её центр и коэффициент масштабирования.
center: [55.746993, 37.608284], // Москва
zoom: 17
});
// document.getElementById('destroyButton').onclick = function () {
// // Для уничтожения используется метод destroy.
// myMap.destroy();
// };
}
// смотри js/yandexMapInit.js