$(function() {
    $( "#id_origin" ).catcomplete({
        source: "/api/get_cities/",
        minLength: 0,
    });
    $( "#id_destinations" ).catcomplete({
        source: "/api/get_cities/",
        minLength: 0,
    });
});


