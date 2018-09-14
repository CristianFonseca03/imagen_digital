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