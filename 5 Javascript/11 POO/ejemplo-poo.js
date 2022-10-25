// Ruler en 42 para postear sin line-break

class Coche {
  /* 
  Los atributos privados han de definirse
  así primero.

  Esta sintaxis sólo es válida a partir de
  ES10. Si la pruebas en tu máquina local
  y no funciona es posible que tengas que
  actualizar tu versión de NodeJS.
  
  NO ES NECESARIO PARA MÉTODOS
  */

  #robado;
  #encendido;

  // Este tipo de atributos son protegidos
  // privados, pero por convención, JS no
  // los respeta.
  _isdeveloper = "Privada por convención";


  constructor(marca, modelo, cc) { 
    // Declaramos el constructor
    this.marca = marca;
    this.modelo = modelo;
    this.cc = cc;

    // Atributos privados
    this.#robado = false;
    this.#encendido = false;
  }

  girarContacto() {
  // Un método público cualquiera
    if (this.#getEncendido() == false) {
      this.#setEncendido(true) 
    } else { 
      this.#setEncendido(false) 
    }
    console.log("Cambiando el estado del motor a: " + this.#getEncendido())
    return "Cambio del estado del motor con éxito"
  }




  // Métodos privados
  #getEncendido() {
    return this.#encendido
  }
  #setEncendido(boolean) {
    this.#encendido = boolean
  }
}


// Instanciación de clase
let miCoche = new Coche(
  "Fiat", "Panda", 1500
  )

// Probando método público
  // Usando el return
console.log(miCoche.girarContacto())

  // Sin usar el return
miCoche.girarContacto()


// Probando atributos y métodos privados

  // Probamos primero los métodos

  try {
    miCoche.getEncendido()
    // Uncaught TypeError:
    // miCoche.getEncendido
    // is not a function
  
    // miCoche.#getEncendido()
    // Syntax Error, que no se pude
    // recoger con catch
    console.log(
      "Se ejecuto el try en métodos"
      )
  }
  catch {
    // Los métodos que hemos definido no
    // se pueden llamar porque JS respeta
    // #metodo()
    console.log(
      "Se ejecutó el except en métodos"
      )
  }

  // Probamos los atributos

  console.log(miCoche.robado)
  // Devuelve undefined


  // console.log(miCoche.#robado)
  // Devuelve syntax error, JS sí lo 
  // respeta

  console.log(miCoche._isdeveloper)
  // Sí devuelve su valor porque sólo es
  // una convención




// Probando Herencia
// Sobre el uso de la keyword "super":
// https://www.w3schools.com/Jsref/jsref_class_super.asp

class Todoterreno extends Coche {
  constructor(marca, modelo, cc, traccion) {
    super(marca, modelo, cc); // Referencia a la clase padre
    this.traccion = traccion;
    // Extiende la clase padre
  }

  // Probando polimorifsmo

  girarContacto() {
    super.girarContacto()
    console.log("Esta es una clase extendida y modificada")
  }

  /*
  Esto no se puede hacer porque los
  métodos privados se heredan pero no
  extienden.

  #getEncendido() {
    console.log("Obteniendo el estado del motor")
    super.getEncendido()
  }
  */
}



// Instanciamos una nueva clase
const nissanPatrol = new Todoterreno("Nissan", "Patrol", 3000, "4x4");

// Imprimimos el objeto para observar
// los cambios
console.log(nissanPatrol)

// Probamos método extendido
nissanPatrol.girarContacto()
nissanPatrol.girarContacto()