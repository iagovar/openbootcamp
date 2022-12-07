
// Metemos el formulario en memoria para trabajar con él
let miFormulario = document.getElementById("miFormulario")

// Creamos un evento para el formulario
// https://www.w3schools.com/jsref/met_element_addeventlistener.asp
//
// El handler del evento (e) se tiene que pasar a través de una función anónima,
// no se puede pasar como argumento de una función simplemente.

miFormulario.addEventListener("click", e => funcionParaEjecutar(e));

function funcionParaEjecutar(e) {
        console.log(e)     // Imprimimos el evento
        e.preventDefault() // Evitamos que se recarge la pag para mostrar el console.log
}