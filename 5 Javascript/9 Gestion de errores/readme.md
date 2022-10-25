# Gestión de errores con throw, try, catch, etc

Ver el archivo throw-try-catch.js

# Gestionar logs en nodejs

- Creamos el proyecto de node con `npm init -y`.
- Modificamos el *package.json* para adaptarlo a nuestras necesidades.
- Instalamos la librería [*winston*](https://www.npmjs.com/package/winston) con `npm install winston`.

Desde ./index.js estamos importando ./logger/, que es donde hemos definido el comportamiento del logger. En ./logger/index.js hay comentarios indicando cómo está configurado.


Con esta librería básicamente podemos crear logs para no tener que revisar los errores en directo.