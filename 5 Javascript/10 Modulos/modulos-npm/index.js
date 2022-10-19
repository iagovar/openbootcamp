//
// Vamos a importar "axios" de npm para trabajar con una api
//
// Este es el paquete: https://www.npmjs.com/package/axios
// Esta es la API: https://pokeapi.co/


// Ejecutamos "npm init -y" y metemos "type: 'module'" en el package.json

// Ejecutamos "npm install axios" en el directorio actual

// importamos el módulo. En la documentación muestran el método
// para CommonJS, pero usaremos el método ES6

import axios from "axios";


// Hacemos una consulta a la API usando el código de ejemplo
// que muestran en npm

// Make a request for a user with a given ID
axios.get('https://pokeapi.co/api/v2/pokemon/ditto')
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });

// Ahora ya está funcionando