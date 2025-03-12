document.addEventListener('DOMContentLoaded', function () {
    // data of origin
    var optionsOrigin = {
        data: {
            "Aguascalientes": null,
            "Baja California": null,
            "Baja California Sur": null,
            "Campeche": null,
            "Chiapas": null,
            "Chihuahua": null,
            "Ciudad de México": null,
            "Coahuila": null,
            "Colima": null,
            "Durango": null,
            "Estado de México": null,
            "Guanajuato": null,
            "Guerrero": null,
            "Hidalgo": null,
            "Jalisco": null,
            "Michoacán": null,
            "Morelos": null,
            "Nayarit": null,
            "Nuevo León": null,
            "Oaxaca": null,
            "Puebla": null,
            "Querétaro": null,
            "Quintana Roo": null,
            "San Luis Potosí": null,
            "Sinaloa": null,
            "Sonora": null,
            "Tabasco": null,
            "Tamaulipas": null,
            "Tlaxcala": null,
            "Veracruz": null,
            "Yucatán": null,
            "Zacatecas": null
        }
    }
    // data of places to go
    var optionsDestiny = {
        data: {
            "Playa": null,
            "Resort": null,
            "Ciudad": null,
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
            "Sitio histórico": null,            
            "Centro cultural": null,
            "Pueblo mágico": null,
            "Pueblo minero": null,
            "Metrópolis": null,
            "Zona Arqueológica": null,
            "Cascadas Petrificadas": null,
            "Manantiales": null,
            "Formación Natural": null,
            "Canales": null,
            "Patrimonio Mundial": null,
            "Zona Natural": null,
            "Pueblo Pesquero": null,
            "Reserva de la Biosfera": null,
            "Centro Minero": null,
            "Cueva": null,
            "Atracción Turística": null,
            "Ruta Puuc": null,
            "Parque de Aventura": null,
            "Mirador": null,
            "Caverna Submarina": null,
            "Atracción Natural": null,
            "Pueblo de Montaña": null,
            "Sierra": null,
            "Destino Ecoturístico": null,
            "Pueblo Costero": null,
            "Destino Surfista": null,
            "Área Natural Protegida": null,
            "Isla": null,
            "Reserva Natural": null,
            "Lagos": null,
            "Centro Histórico": null,
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