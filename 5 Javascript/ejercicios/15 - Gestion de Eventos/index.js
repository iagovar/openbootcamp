// Metemos el botón en memoria

const miBoton = document.querySelector("#miBoton");

// Vinculamos un evento click y generamos la alerta

miBoton.addEventListener("click", () => {
    alert("Click en el botón")
})


// Creamos evento click con JQuery que muestre msg por consola

$(document).ready(() => {
    $("#miBoton").click(() => {console.log("Estoy usando Jquery")});
});