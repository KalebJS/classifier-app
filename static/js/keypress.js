$(document).keypress(function (e) {
    if (e.which === 106) {
        $('button#accept').click();
        return false;
    } else if (e.which === 108) {
        $('button#reject').click();
        return false;
    }
});