public class Coche {

    protected String marca;
    protected String modelo;
    protected int anio;
    protected double precio;
    protected String color;

    public Coche(String marca, String modelo, int anio, double precio, String color) {
        this.marca = marca;
        this.modelo = modelo;
        this.anio = anio;
        this.precio = precio;
        this.color = color;
    }

    // Creamos getters y setters para todos los atributos
    public String getMarca() {return marca;}
    public String setMarca(String marca) {
        this.marca = marca;
        return "Ahora la marca es " + marca;
    }

    public String getModelo() {return modelo;}
    public String setModelo(String modelo) {
        this.modelo = modelo;
        return "Ahora el modelo es " + modelo;
    }

    public int getAnio() {return anio;}
    public String setAnio(int anio) {
        this.anio = anio;
        return "Ahora el año es " + anio;
    }

    public double getPrecio() {return precio;}
    public String setPrecio(double precio) {
        this.precio = precio;
        return "Ahora el precio es " + precio;
    }

    public String getColor() {return color;}
    public String setColor(String color) {
        this.color = color;
        return "Ahora el color es " + color;
    }

    @Override
    public String toString() {
        return "Coche{" + "marca=" + this.marca + ", modelo=" + this.modelo + ", anio=" + this.anio + ", precio=" + this.precio + ", color=" + this.color + '}';
    }
}
