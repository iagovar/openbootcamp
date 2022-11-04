

const miNombre = "Iago";
const miApellido = "Var";

const miNombreApellido = {nombre: miNombre, apellido: miApellido};

// Almacenamos los datos


// Lo pasamos a JSON primero para evitar que nos ponga "object" al almacenarlo
// https://www.w3schools.com/js/js_json.asp
paraInput = JSON.stringify(miNombreApellido);


// https://www.w3schools.com/jsref/prop_win_sessionstorage.asp
sessionStorage.setItem("Persona", paraInput);
localStorage.setItem("Persona", paraInput);

// Creamos una cookie que caduque en 2 minutos con los datos del objeto anterior
// https://www.w3schools.com/js/js_cookies.asp
// https://www.w3schools.com/js/js_dates.asp

function setCookie(usuario, expira) {
    // Espera un nombre de usuario y fecha de expiración (en minutos)
    // Crea una cookie con ello

    const fecha = new Date();

    fecha.setMinutes(fecha.getMinutes() + expira);

    stringFecha = fecha.toUTCString();

    document.cookie = "username=" + usuario.nombre + " " + usuario.apellido +"; expires=" + stringFecha + "; path=/"
}

setCookie(miNombreApellido, 2)