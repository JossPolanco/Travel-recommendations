document.addEventListener('DOMContentLoaded', function() {
    // data of origin
    var optionsOrigin = {
        data:{
            "Chihuahua": '/static/img/low_quality/low_chihuahua.jpg',
        }
    }
    // data of places to go
    var optionsDestiny = {
        data:{
            "CDMX": null,
            "Monterrey": null,
            "Puebla": null,
            "Cancun": '/static/img/low_quality/low_cancun.jpg',
        }
    }
    var origin_autocomplete = document.querySelectorAll('.origin_autocomplete');
    var destiny_autocomplete = document.querySelectorAll('.destiny_autocomplete')

    var instances = M.Autocomplete.init(origin_autocomplete, optionsOrigin);
    var instances = M.Autocomplete.init(destiny_autocomplete, optionsDestiny);

    // --------------------------------------------------//
    var style = {
        format: 'yyyy-mm-dd',
        i18n: {
            cancel: 'Cancel',
            clear: 'Clear',
            done: 'Done',
            months: ['January', 'February', 'March', 'April', 'May', 'Jun', 'July',
                'August', 'September', 'October', 'November', 'Dicember'
            ],
            monthsShort: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Agu',
                'Sep', 'Oct', 'Nov', 'Dec'
            ],
            weekdays: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday'
            ],
            weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'],
            weekdaysAbbrev: ['D', 'L', 'M', 'M', 'J', 'V', 'S']
        }
    }
    var datePicker = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(datePicker, style);
});