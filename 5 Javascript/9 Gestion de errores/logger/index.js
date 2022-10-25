
// Copiapega de la documentación
const winston = require('winston');

const logger = winston.createLogger({
  level: 'debug', // Cambiamos el nivel de info a debug
  format: winston.format.json(),
  defaultMeta: { service: 'user-service' },
  transports: [
    //
    // - Write all logs with importance level of `error` or less to `error.log`
    // - Write all logs with importance level of `info` or less to `combined.log`
    //
    new winston.transports.Console(), // Agregamos consola para el output de los errores
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
  ],
});


// exportamos este modulo para que se pueda usar en otros archivos
module.exports = logger;