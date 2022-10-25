const miLogger = require('./logger');


//miLogger.log("Esto es un mensaje normal por consola") .log no está incluída en la librería winston
miLogger.info("Mensaje informativo")
miLogger.debug("Esto es un mensaje de debug")
miLogger.warn("esto es una advertencia")
miLogger.error("Esto es un error")