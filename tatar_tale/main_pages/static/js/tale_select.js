$(document).ready(function() {
    $('.tale_1').click(function() {
        if ($('p#tale_1').is(':visible')) {
            $('p#tale_1').css('display', 'none');
        } else {
            $('p#tale_1').css('display', 'flex');
            $('p#tale_2, p#tale_3').css('display', 'none');
        }
    });

    $('.tale_2').click(function() {
        if ($('p#tale_2').is(':visible')) {
            $('p#tale_2').css('display', 'none');
        } else {
            $('p#tale_2').css('display', 'flex');
            $('p#tale_1, p#tale_3').css('display', 'none');
        }
    });

    $('.tale_3').click(function() {
        if ($('p#tale_3').is(':visible')) {
            $('p#tale_3').css('display', 'none');
        } else {
            $('p#tale_3').css('display', 'flex');
            $('p#tale_1, p#tale_2').css('display', 'none');
        }
    });
});
