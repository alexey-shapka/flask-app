$(document).ready(function () {
    $(`#${page}`).addClass("active-header");

    $(".header-navigation").click(function() {
        $(".active-header").removeClass("active-header");
        $(this).addClass("active-header");
    });
});