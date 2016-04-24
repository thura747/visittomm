function toggler(divId) {
//    $("#" + divId).toggle();
    $(".flyout-container").toggle();
    $(".flyout-wrapper").toggle();
}

$(function() {
  $( "#origin" ).catcomplete({
    source: "/api/get_cities/",
    minLength: 0,
  });


$(function() {
  $( "#destination" ).catcomplete({
    source: "/api/get_cities/",
    minLength: 0,
  });


});
