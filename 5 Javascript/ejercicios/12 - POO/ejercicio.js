/*
Crea un nuevo fichero JS que contenga las siguientes líneas

- Una clase llamada "Estudiante" que tenga:

- Una variable llamada nombre

- Otra variable lista llamada asignaturas con 3 asignaturas: Javascript, HTML, CSS

- Un método "obtenDatos" que devuelva un objeto con las propiedades nombre y asignaturas

- Crea una nueva instancia de "Estudiante"

- Haz la llamada al método obtenDatos
*/

class Estudiante {
  constructor(nombre, asignaturas) {
    this.nombre = nombre;
    this.asignaturas = asignaturas;
  }

  obtenDatos() {
    const miDiccionario = {
      nombre: this.nombre,
      asignaturas: this.asignaturas
    }

    return miDiccionario
  }
}

// Instanciamos la clase

miAlumno = new Estudiante("Fulanito", ["Javascript", "HTML", "CSS"])

// Llamamos al getter

const unDiccionario = miAlumno.obtenDatos()

for (elemento in unDiccionario) {
  console.log(elemento + ": " + unDiccionario[elemento])
}