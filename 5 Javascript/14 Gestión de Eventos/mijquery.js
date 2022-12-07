let CONTADOR = 0; // Usada para contabilziar y concatenar

$(document).ready(function(){
    // Metemos el texto del contador en memoria
    const miContador = $("#contador").text()

    $(".anadir").click(() => {
        // Botón de añadir
        CONTADOR += 1;
        $("#contador").text(miContador + ": " + CONTADOR)
    })

    $(".restar").click(() => {
        // Botón de restar
        CONTADOR -= 1;
        $("#contador").text(miContador + ": " + CONTADOR)
    })
});