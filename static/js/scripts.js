$("#menu-toggle").click(function (e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
    if ($("#wrapper").hasClass('toggled')) {
        $("#button-menu").addClass("fa-angle-double-left");
        $("#button-menu").removeClass("fa-angle-double-right");
    } else {
        $("#button-menu").addClass("fa-angle-double-right");
        $("#button-menu").removeClass("fa-angle-double-left");
    }
});
$(window).resize(function () {
    var i = $(window).width()
    if (i < 768) {
        $("#wrapper").removeClass("toggled");
    } if (i > 768) {
        $("#wrapper").addClass("toggled");
    }
});
$(document).ready(function () {
    var i = $(window).width()
    if (i > 768) {
        $("#wrapper").addClass("toggled");
    }
});