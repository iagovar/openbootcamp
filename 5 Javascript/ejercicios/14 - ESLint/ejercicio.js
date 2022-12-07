let nombre = "Iago";
let apellido = "Var";
let estudiante = nombre + " " + apellido;
let estudianteMayus = estudiante.toLocaleUpperCase();
let estudianteMinus = estudiante.toLocaleLowerCase();
let numCharsEstudiante = estudiante.length;
let primeraLetraNombre = nombre.slice(0,1);
let ultimaLetraApellido = apellido.slice(apellido.length - 1, apellido.length);
let estudianteSinEspacios = estudiante.replace(/ /g,""); // Trim sólo reemplaza de los extremos
let estaNombreEnEstudiante = estudiante.includes(nombre);

console.log(estaNombreEnEstudiante);