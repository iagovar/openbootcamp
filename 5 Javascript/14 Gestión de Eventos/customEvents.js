// Metemos el elemento del DOM que queremos manipular en memoria

const hTexto = document.getElementById("h-texto");

// Vinculamos elemento del DOM a un evento

hTexto.addEventListener("cambioDeTexto", evento => {
    hTexto.innerText = evento.detail.texto;
    hTexto.style.color = evento.detail.color;
})

// creamos un evento personalizado

function cambiarTexto(nuevoTexto, color) {
    // Usamos CustomEvent()
    // https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent/CustomEvent

    const tempEvento = new CustomEvent("cambioDeTexto", {
        detail: {texto: nuevoTexto, color}
    })

    // Ejecutamos el evento
    hTexto.dispatchEvent(tempEvento)
}

// Asignamos llamadas a la función personalizada a los botones,
// para poder interactuar

const botonRojo = document.querySelector("#botonRojo");
botonRojo.onclick = () => {cambiarTexto("Está en rojo", "red")}

const botonAzul = document.querySelector("#botonAzul");
botonAzul.onclick = () => {cambiarTexto("Está en azul", "blue")}

