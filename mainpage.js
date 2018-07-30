window.myWidgetParam ? window.myWidgetParam : window.myWidgetParam = [];
window.myWidgetParam.push({
    id: 5,
    cityid: '4930956',
    appid: '64e1289a90c76ae161b66981615e5d2d',
    units: 'imperial',
    containerid: 'openweathermap-widget-5',
});
(function() {
    var script = document.createElement('script');
    script.async = true;
    script.charset = "utf-8";
    script.src = "https://openweathermap.org/themes/openweathermap/assets/vendor/owm/js/weather-widget-generator.js";
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(script, s);
    s.style.textAlign = 'center';
})();
