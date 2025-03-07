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
            "Bosque": null,
            "Monumento": null,
            "Pueblo": null,
        }
    }
    var origin_autocomplete = document.querySelectorAll('.origin_autocomplete');
    var place_autocomplete = document.querySelectorAll('.place_autocomplete')

    var instances = M.Autocomplete.init(origin_autocomplete, optionsOrigin);
    var instances = M.Autocomplete.init(place_autocomplete, optionsDestiny);

    // -------------------SELECTS---------------------------//
    var weather_select = document.querySelectorAll('.weather_select');
    var season_select = document.querySelectorAll('.season_select');

    var optionsWeather = {
        data: {
            "Caluroso": null,
            "Frio": null,
            "Templado": null,
            "Nieve": null,
        }
    }

    var optionsSeason = {
        classes: 'custom-select',  // Clase CSS personalizada
        dropdownOptions: {
            alignment: 'right',  // Alinea el desplegable a la derecha
            autoTrigger: false,  // Evita que se abra automáticamente
            coverTrigger: false, // Permite que el desplegable sobresalga del botón
            closeOnClick: false  // No se cierra al hacer clic en una opción
        }
    }
    var instances = M.FormSelect.init(weather_select, optionsWeather);
    var instances = M.FormSelect.init(season_select, optionsSeason);
});