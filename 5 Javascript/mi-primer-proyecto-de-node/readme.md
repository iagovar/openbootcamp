## Crear un nuevo proyecto de node

### npm init

Crea el package.json. Nos pedirá una serie de datos, a saber:

- Nombre del paquete
- Versión del paquete
- Descripción
- Entry point: Básicamente el índice, index.js por defecto
- Test command: Se suele usar Jest, pero por el momento lo dejaremos vacío
- Git Repository: De momento lo dejaremos en blanco
- Keywords: Si queremos subirlo a npm o github
- Autor
- Licencia

Después nos mostrará el package.json que vamos a crear, y nos pedirá confirmar o abortar.


## Determinar scripts en Package.json

Debajo del nodo `scripts` especificamos qué queremos incluír.

```
  "scripts": {
    "start": "node index.js",
    "saludar": "node hola-mundo.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
```

Corremos `npm run saludar`y debería ejecutar `hola-mundo.js`.

El script `start` se usa por convención.