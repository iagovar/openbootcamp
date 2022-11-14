// Tajertas
    // Metemos en memoria
const tarjetas = document.querySelectorAll(".tarjeta");

    // Les asignamos draggable=true como propiedad html
    // También los listeners
let contador = 1;
tarjetas.forEach(tarjeta => {

    // Identificamos cada párrafo con id diferente
    tarjeta.setAttribute('id', `tarjeta-${contador}`);
    contador += 1;

    // El atributto draggable no aparecerá al examinar el código con el navegador
    // pero se interpretará como tal
    tarjeta.setAttribute('draggable', true);

    // Con el addeventlistener no hay que poner "ondragstart" sino "dragstart"
    tarjeta.addEventListener("dragstart", (evento) => {
        evento.dataTransfer.setData('id', tarjeta.id)
    })
})

// Secciones

const sections = document.querySelectorAll(".section");

    // Asignamos atributos y selectores
sections.forEach(section => {
    section.addEventListener("dragover", evento => {
        evento.preventDefault();
        evento.dataTransfer.dropEffect = "copy";
    })

    section.addEventListener("drop", evento => {
        const identificador = evento.dataTransfer.getData('id');
        const tempTarjeta = document.getElementById(identificador);

        // Esto ya borra de una sección y lo mete en otro
        section.appendChild(tempTarjeta)
    })
})

// Papelera

const papelera = document.querySelector('#papelera');

    // Agregamos atributos y eventos
papelera.addEventListener("dragover", evento => {
    // ¿Necesario para que funcione el drop?
    evento.preventDefault();
    evento.dataTransfer.dropEffect = "move";
})

papelera.addEventListener("drop", evento => {
    const identificador = evento.dataTransfer.getData('id');
    const tempTarjeta = document.getElementById(identificador);

    tempTarjeta.remove()
})

papelera.addEventListener("dragenter", evento => {
    const identificador = evento.dataTransfer.getData('id');
    const tempTarjeta = document.getElementById(identificador);
    tempTarjeta.classList.add('borde-rojo')
})

papelera.addEventListener("dragleave", evento => {
    const identificador = evento.dataTransfer.getData('id');
    const tempTarjeta = document.getElementById(identificador);
    tempTarjeta.classList.remove('borde-rojo')
})