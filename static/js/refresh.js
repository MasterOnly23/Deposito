var idleTime = 0;

$(document).ready(function () {
    // Incrementar el contador de tiempo inactivo cada minuto.
    var idleInterval = setInterval(timerIncrement, 60000); // 1 minuto

    // Reiniciar el contador de tiempo inactivo al mover el mouse o presionar una tecla.
    $(this).mousemove(function (e) {
        idleTime = 0;
    });
    $(this).keypress(function (e) {
        idleTime = 0;
    });
});

function timerIncrement() {
    idleTime += 1;
    if (idleTime >= 2) { // 2 minutos de inactividad
        // Redirigir o recargar la página actual
        location.reload(true);
    }
}
