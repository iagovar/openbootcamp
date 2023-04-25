package main.java.com.midominio;

// Esto importa todas las clases que están dentro de ./SmartStuff
// No es una buena práctica, pero beh
import main.java.com.midominio.SmartStuff.*;

public class Main {

    // El constructor de la clase Main, en java, es obligatorio en cualquier programa,
    // y se usa como punto de entrada del mismo. No se puede obviar.
    // RECUERDA PONER EL PUNTO DE ENTRADA ESTÁTICO PARA PODER EJECUTARLO!
    public static void main(String[] args) {

        // Vamos a crear un objeto SmartDevice, y luego jugar con sus propiedades.
        // En este caso una board similar a RaspBerri Pi.

        SmartDevice myDevice = new SmartDevice(
                "GenericBoard",
                "GenericModel",
                6.5,
                true,
                true,
                true,
                true,
                true,
                true);


        // No podemos acceder a sus atributos desde Main, porque están "protected", asi que
        // tenemos que hacerlo desde los getters y setters

        // Imprimimos y luego cambiamos el nombre
        System.out.println("Obtenemos el nombre de SmartDevice\n");
        System.out.println(myDevice.getName());
        System.out.println("Cambiamos el nombre a RaspBerri Pi\n");
        myDevice.setName("RaspBerri", "Pi");
        System.out.println(myDevice.getName());

        // Encendemos el dispositivo, y luego consultamos su estado
        System.out.println("Vamos a ver en qué estado eestá el dispositivo: " + myDevice.geTurnedOn());
        System.out.println("\nVamos a encenderlo: " + myDevice.setTurnedOn(true));;
        System.out.println("\nVolvemos a consultar su estado: "+ myDevice.geTurnedOn());


        // Vamos a crear un smartphone y jugar con los getters y setters
        SmartPhone myPhone = new SmartPhone(
                "Poco",
                "F1",
                6.18,
                true,
                true,
                true,
                true,
                true,
                true,
                "Android",
                64,
                // El tamaño de la Ram es 6 GigaBytes, así que 6*1024
                6*1024,
                3,
                true);

        // Consultemos la memoria ram
        System.out.println("\nVamos a consultar la memoria RAM: " + myPhone.getRamSize());

        // Vamos a conectarlo por LTE y luego consultar su estado general de conexión
        System.out.println("\nVamos a conectarlo por LTE: " + myPhone.setMobileConnected(true));
        System.out.println("\nVamos a consultar su estado general de conexión: " + myPhone.getConnected());

        // Haremos lo mismo con un SmartWatch
        SmartWatch myWatch = new SmartWatch(
                "Xiaomi",
                "Band",
                2,
                false,
                true,
                true,
                false,
                false,
                false,
                true,
                true);

        // Vamos a cargarlo
        System.out.println("Poniendo el nivel de batería en: " + myWatch.setBatteryLevel(50));

        // Vamos a conectarlo y consultar su estado de conexión después
        System.out.println("Conectado Bluetooth: " + myWatch.setBluetoothConnected(true));
        System.out.println("El estado general de conexión es: " + myWatch.getConnected());

        // Vamos a encender el modo de carga
        System.out.println("Vamos a encender el modo de carga: " + myWatch.setCharging(true));;

    }

}
