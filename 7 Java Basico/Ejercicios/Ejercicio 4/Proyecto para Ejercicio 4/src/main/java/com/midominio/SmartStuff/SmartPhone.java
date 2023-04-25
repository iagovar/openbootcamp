package main.java.com.midominio.SmartStuff;

public class SmartPhone extends SmartDevice {

    // Atributos de capacidad
    protected String OperatingSystem;
    protected double DiskSize;
    protected double RamSize;
    protected int CamerasCount;
    protected boolean hasJack;

    // Atributos de estado

        // No se contemplan nuevos atributos de estado
    
    /*
    El siguiente bloque de código es TREMENDO SPAGUETTI!

    Los argumentos del constructor de SmartPhone son todos los que necesita esta clase y
    el contructor de la clase padre (SmartDevice), por eso son una pila de ellos.

    Luego parte de estos se pasan con super() al constructor de la clase padre para que
    haga sus cositas.

    */
    public SmartPhone(String Brand,
                      String Model,
                      double screenSize,
                      boolean hasWifi,
                      boolean hasBluetooth,
                      boolean hasGPS,
                      boolean hasMobileConnection,
                      boolean hasUsb,
                      boolean hasCamera,
                      String OperatingSystem,
                      double DiskSize,
                      double RamSize,
                      int CamerasCount,
                      boolean hasJack) {
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
        this.OperatingSystem = OperatingSystem;
        this.DiskSize = DiskSize;
        this.RamSize = RamSize;
        this.CamerasCount = CamerasCount;
        this.hasJack = hasJack;

        System.out.println("Se ha creado un objeto de clase SmartPhone");
    }

    // Getters y Setters
    public String getOperatingSystem() {return this.OperatingSystem;}
    public String setOperatingSystem(String OperatingSystem) {
        this.OperatingSystem = OperatingSystem;
        return "Now the operating system is: " + this.OperatingSystem;
    }

    public double getDiskSize() {return this.DiskSize;}
    public String setDiskSize(double DiskSize) {
        this.DiskSize = DiskSize;
        return "Now the disk size is: " + this.DiskSize;
    }

    public double getRamSize() {return this.RamSize;}
    public String setRamSize(double RamSize) {
        this.RamSize = RamSize;
        return "Now the ram size is: " + this.RamSize;
    }

    public int getCamerasCount() {return this.CamerasCount;}
    public String setCamerasCount(int CamerasCount) {
        this.CamerasCount = CamerasCount;
        return "Now the cameras count is: " + this.CamerasCount;
    }

    public boolean getHasJack() {return this.hasJack;}
    public String setHasJack(boolean hasJack) {
        this.hasJack = hasJack;
        return "Now the hasJack is: " + this.hasJack;
    }
}
