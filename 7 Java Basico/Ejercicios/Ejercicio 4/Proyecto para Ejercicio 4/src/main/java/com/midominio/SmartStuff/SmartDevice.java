package main.java.com.midominio.SmartStuff;

public class SmartDevice {

    // Definimos primero los atributos, y los ponemos protected porque
    // así sólo los pueden usar la clase que los define y sus clases hijas,
    // que en este caso serán SmartPhone y SmartWatch.

    // Atributos de capacidad
    protected String Brand;
    protected String Model;
    protected double ScreenSize;

    protected boolean hasWifi;
    protected boolean hasBluetooth;
    protected boolean hasGPS;
    // hasMobileConnection se refiere sólo a su capacidad, no si está o no conectado.
    protected boolean hasMobileConnection;
    protected boolean hasUsb;
    protected boolean hasCamera;

    // Atributos de estado
    protected boolean isTurnedOn = false;
    protected boolean isConnected = false;
    protected boolean isWifiConnected = false;
    protected boolean isBluetoothConnected = false;
    protected boolean isMobileConnected = false;
    protected boolean isCharging = false;
    protected double batteryLevel = 0;

    // Constructor de la clase SmartDevice en formato multilínea
    public SmartDevice(String Brand,
                       String Model,
                       double screenSize,
                       boolean hasWifi,
                       boolean hasBluetooth,
                       boolean hasGPS,
                       boolean hasMobileConnection,
                       boolean hasUsb,
                       boolean hasCamera) {
        // Pasamos los parámetros del constructor a los atributos del objeto
        this.Brand = Brand;
        this.Model = Model;
        this.ScreenSize = screenSize;
        this.hasWifi = hasWifi;
        this.hasBluetooth = hasBluetooth;
        this.hasGPS = hasGPS;
        this.hasMobileConnection = hasMobileConnection;
        this.hasUsb = hasUsb;
        this.hasCamera = hasCamera;
    }
    // Getters y Setters
    public String getName() {
        return this.Brand + " " + this.Model;
    }
    public String setName(String Brand, String Model) {
        this.Brand = Brand;
        this.Model = Model;
        return "Now the device is: " + this.Brand + " " + this.Model;
    }

    public double getScreenSize() {return this.ScreenSize;}
    public String setScreenSize(double ScreenSize) {
        this.ScreenSize = ScreenSize;
        return "Now the screen size is: " + this.ScreenSize;
    }

    public boolean geTurnedOn() {return this.isTurnedOn;}
    public String setTurnedOn(boolean isTurnedOn) {
        this.isTurnedOn = isTurnedOn;
        return "Now the device is turned on status: " + this.isTurnedOn;
    }

    public boolean getConnected() {return this.isConnected;}
    public String setConnected(boolean isConnected) {
        return "You cant connect this device with this method directly, use a method intended for a specific interface";
    }

    public boolean getWifiConnected() {return this.isWifiConnected;}
    public String setWifiConnected(boolean isWifiConnected) {
        this.isWifiConnected = isWifiConnected;
        this.isConnected = isWifiConnected;
        return "Now the device is wifi connected on status: " + this.isWifiConnected;
    }

    public boolean getBluetoothConnected() {return this.isBluetoothConnected;}
    public String setBluetoothConnected(boolean isBluetoothConnected) {
        this.isBluetoothConnected = isBluetoothConnected;
        this.isConnected = isBluetoothConnected;
        return "Now the device is bluetooth connected on status: " + this.isBluetoothConnected;
    }

    public boolean getMobileConnected() {return this.isMobileConnected;}
    public String setMobileConnected(boolean isMobileConnected) {
        this.isMobileConnected = isMobileConnected;
        this.isConnected = isMobileConnected;
        return "Now the device is mobile connected on status: " + this.isMobileConnected;
    }

    public boolean getCharging() {return this.isCharging;}
    public String setCharging(boolean isCharging) {
        this.isCharging = isCharging;
        return "Now the device is charging on status: " + this.isCharging;
    }

    public double getBatteryLevel() {return this.batteryLevel;}
    public String setBatteryLevel(double batteryLevel) {
        this.batteryLevel = batteryLevel;
        return "Now the battery level is: " + this.batteryLevel;
    }

}
