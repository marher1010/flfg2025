$(document).ready(function () {

    if (window.location.hash === "#open") {
        $('header').addClass('open');
        $('.background-video').get(0).play();
        $(".discover-button").addClass("hidden");

    }

    $("#forward").click(function () {
        $(".discover-button").addClass("hidden");
        $("header").addClass("open");
        $('.background-video').get(0).play();
    });
    $("#back").click(function () {
        $("header").removeClass("open");
        $(".discover-button").removeClass("hidden");
        $("#back").removeClass("custom-cursor--action");
        $("#advisors").removeClass("custom-cursor--action");
        $("#services").removeClass("custom-cursor--action");
        history.replaceState(null, null, " ");

    });



    // open the modal
    $('.about-button').click(function () {
        var buttonId = $(this).attr('id');
        var modalContainer = $('#modal-container[modal-id="' + buttonId + '"]');
        modalContainer.removeAttr('class').addClass(buttonId);
    });

    // close the modal
    $('[modal-id="about-one"], [modal-id="about-two"], [modal-id="about-three"]').on('click', function (event) {
        if (!$(event.target).closest('.modal').length) {
            $('[modal-id="about-one"], [modal-id="about-two"], [modal-id="about-three"]').addClass('out');
        }

    });


});