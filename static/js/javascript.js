document.addEventListener('DOMContentLoaded', function () {
    // data of origin
    var optionsOrigin = {
        data: {
            "Chihuahua": '/static/img/low_quality/low_chihuahua.jpg',
        }
    }
    // data of places to go
    var optionsDestiny = {
        data: {
            "Playa": null,
            "Resort": null,
            "Ciudad turística": null,
            "Ciudad colonial": null,
            "Patrimonio UNESCO": null,
            "Ciudad histórica": null,
            "Destino cultural": null,
            "Sitio gastronómico": null,
            "Cañón": null,
            "Área natural": null,
            "Parque nacional": null,
            "Destino artístico": null,
            "Bahía": null,
            "Zona arqueológica": null,
            "Sitio histórico": null,
            "Metrópoli": null,
            "Centro cultural": null,
            "Pueblo mágico": null,
            "Pueblo minero": null,
        }
    }
    var origin_autocomplete = document.querySelectorAll('.origin_autocomplete');
    var place_autocomplete = document.querySelectorAll('.place_autocomplete')

    var instances = M.Autocomplete.init(origin_autocomplete, optionsOrigin);
    var instances = M.Autocomplete.init(place_autocomplete, optionsDestiny);

    // -------------------SELECTS---------------------------//
    var weather_select = document.querySelectorAll('.weather_select');
    var season_select = document.querySelectorAll('.season_select');
    

    var instances = M.FormSelect.init(weather_select);
    var instances = M.FormSelect.init(season_select);
});