ymaps.ready(function () {
var myMap = new ymaps.Map('map', {
center: [55.74730, 37.6105],
zoom: 17
}),
myPlacemark = new ymaps.Placemark([55.747171, 37.60944], {
hintContent: 'Москва, Лебяжий переулок, д.8</p><p>+7 (495) 697-06-02'
}, {
// Опции.
// Необходимо указать данный тип макета.
iconLayout: 'default#image',
// Своё изображение иконки метки.
iconImageHref: 'img/location.png',
// Размеры метки.
iconImageSize: [78, 63],
// Смещение левого верхнего угла иконки относительно
// её "ножки" (точки привязки).
}, {
balloonShadow: false
});
myMap.geoObjects.add(myPlacemark);
myMap.behaviors
.disable(['rightMouseButtonMagnifier','scrollZoom'])
});