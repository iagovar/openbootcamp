
// Crea un archivo llamado fechas.js que contenga las siguientes líneas

// - La fecha de hoy

const hoy = new Date()

// - La fecha de tu nacimiento

const miNacimiento = new Date("1987-12-27")

console.log(miNacimiento)

// - Un variable que indique si hoy es más tarde (>) que la fecha de tu nacimiento

const masTarde = hoy > miNacimiento

// - Una variable que contenga el día de tu nacimiento

const diaNacimiento = miNacimiento.getDay()

// - Una variable que contenga el mes de tu nacimiento (recuerda que Enero es mes 0)

const mesNacimiento = miNacimiento.getMonth()

// - Una variable que contenga el año de tu nacimiento (con 4 dígitos)

const miAnho = miNacimiento.getFullYear()

console.log(miAnho)
