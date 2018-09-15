function randomNumber(min, max) {
    return Math.round(Math.random() * (max - min) + min);
}
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
$("#menuDropdown").click(function (e) {
    if ($("#collapseMenu").hasClass('show')) {
        $("#button-dropdown").addClass("fa-angle-double-down");
        $("#button-dropdown").removeClass("fa-angle-double-up");
    } else {
        $("#button-dropdown").addClass("fa-angle-double-up");
        $("#button-dropdown").removeClass("fa-angle-double-down");
    }
});
$(window).resize(function () {
    var i = $(window).width()
    if (i < 768) {
        $("#wrapper").removeClass("toggled");
    }
    if ($("#wrapper").hasClass('toggled')) {
        $("#button-menu").addClass("fa-angle-double-left");
        $("#button-menu").removeClass("fa-angle-double-right");
    } else {
        $("#button-menu").addClass("fa-angle-double-right");
        $("#button-menu").removeClass("fa-angle-double-left");
    }
});
$(document).ready(function () {
    const colors = ["bg-primary","bg-danger","bg-success","bg-info","bg-purple","bg-pink"]
    $("#color-1").addClass(colors[randomNumber(0,5)]);
    $("#color-2").addClass(colors[randomNumber(0,5)]);
    $("#color-3").addClass(colors[randomNumber(0,5)]);
    var i = $(window).width()
    if (i > 768) {
        $("#wrapper").addClass("toggled");
    }

});
