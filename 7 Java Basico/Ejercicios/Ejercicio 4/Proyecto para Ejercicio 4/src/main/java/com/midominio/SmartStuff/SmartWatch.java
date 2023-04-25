package main.java.com.midominio.SmartStuff;

public class SmartWatch extends SmartDevice {

    // Atributos de capacidad
    protected boolean heartRateMonitor;
    protected boolean sleepMonitor;

    // Atributos de estado
    protected int stepsCounter;

    /*
    El siguiente bloque de código es TREMENDO SPAGUETTI!

    Los argumentos del constructor de SmartPhone son todos los que necesita esta clase y
    el contructor de la clase padre (SmartDevice), por eso son una pila de ellos.

    Luego parte de estos se pasan con super() al constructor de la clase padre para que
    haga sus cositas.

    */
    public SmartWatch(String Brand,
                      String Model,
                      double screenSize,
                      boolean hasWifi,
                      boolean hasBluetooth,
                      boolean hasGPS,
                      boolean hasMobileConnection,
                      boolean hasUsb,
                      boolean hasCamera,
                      boolean heartRateMonitor,
                      boolean sleepMonitor) {
        // Llamamos al constructor padre y le pasamos los argumentos que necesita
        super(Brand,
                Model,
                screenSize,
                hasWifi,
                hasBluetooth,
                hasGPS,
                hasMobileConnection,
                hasUsb,
                hasCamera);

        // Hay argumentos que no existen en la clase padre, pero sí en esta, la hija, y hay
        // que inicializarlos también, para que los tenga el objeto.
        this.heartRateMonitor = heartRateMonitor;
        this.sleepMonitor = sleepMonitor;

        System.out.println("Se ha creado un objeto de clase SmartWatch");
    }

    // Getters y Setters

    public boolean getHeartRateMonitor() {return heartRateMonitor;}
    public String setHeartRateMonitor(boolean heartRateMonitor) {
        this.heartRateMonitor = heartRateMonitor;
        return "Heart rate monitor is on status" + heartRateMonitor;
    }

    public boolean getSleepMonitor() {return sleepMonitor;}
    public String setSleepMonitor(boolean sleepMonitor) {
        this.sleepMonitor = sleepMonitor;
        return "Sleep monitor is on status" + sleepMonitor;
    }

    public int getStepsCounter() {return stepsCounter;}
    public String setStepsCounter(int stepsCounter) {
        this.stepsCounter = stepsCounter;
        return "Steps counter is " + stepsCounter;
    }
}
