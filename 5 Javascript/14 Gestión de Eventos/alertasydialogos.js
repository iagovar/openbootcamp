// Probaremos:
// alert, confirm (con operador ternario), prompt, console.table


// Probando alert
const botonAlerta = document.querySelector('#botonAlerta');

botonAlerta.addEventListener("click", () => [
    alert("Esto es una alerta")
])

// Probamos confirm
// https://www.w3schools.com/jsref/met_win_confirm.asp
// https://www.w3schools.com/jsref/jsref_operators.asp

const botonConfirm = document.querySelector("#botonConfirm");

botonConfirm.addEventListener("click", () => {

    // Confirm devuelve true o false
    unaRespuesta = confirm("Seleccina una respuesta") ? true : false;

    console.log(unaRespuesta);
})

// Probando prompt

const botonInfo = document.querySelector("#botonInfo")

botonInfo.addEventListener("click", () => {
    alert("Este es un mensaje de alerta")
})


// Probando console.table
// https://developer.mozilla.org/en-US/docs/Web/API/Console/table

const miLista = [
    {nombre: "Juan", edad: 34},
    {nombre: "Isabel", edad: 33},
    {nombre: "Fernando", edad: 30}
]

console.table(miLista)