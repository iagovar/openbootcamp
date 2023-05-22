import java.util.ArrayList;

// Generamos las interfaces
interface Publisher {
    public void notifySubscribers();
    public void addSubscriber(Subscriber suscriptor);
    public void removeSubscriber(Subscriber suscriptor);
}
interface Subscriber {
    public void getNotified(Publisher context);
}

// Creamos las clases publicadoras / suscriptoras
class CanalDeYoutube implements Publisher {
    // Implementamos la interfaz
    private ArrayList<Subscriber> listaDeSuscriptores = new ArrayList<>();

    @Override
    public void addSubscriber(Subscriber suscriptor) {
        listaDeSuscriptores.add(suscriptor);
    }
    @Override
    public void removeSubscriber(Subscriber suscriptor) {
        listaDeSuscriptores.remove(suscriptor);
    }
    @Override
    public void notifySubscribers() {
        for (Subscriber elemento: listaDeSuscriptores) {
            elemento.getNotified(this);
        }
    }

    // Lógica principal del canal
    private String nombreDelCanal;
    public CanalDeYoutube(String nombreDelCanal) {
        this.nombreDelCanal = nombreDelCanal;
    }

    public String getNombreDelCanal() {
        return this.nombreDelCanal;
    }
}
class Suscriptor implements Subscriber {
    String miNombre;
    public Suscriptor(String miNombre) {
        this.miNombre = miNombre;
    }
    public void getNotified(Publisher context) {
        // Obtener el nombre del canal, haciendo casting de clase Publisher a CanalDeYoutube,
        // ya que el método getNombreDelCanal() no está en la interfaz, sino en la implementación
        String nombreDelCanal = ((CanalDeYoutube) context).getNombreDelCanal();
        System.out.println("Soy el suscriptor\t" + this.miNombre + "\ty estoy siendo notificado desde\t" + nombreDelCanal);
    }
}



// Simulación de lógica
public class Main {
    // Constructor
    public static void main(String[] args) {
        // Creamos un canal de Youtube
        CanalDeYoutube miCanalDeYoutube = new CanalDeYoutube("unCanalCualquiera");

        // Creamos un par de suscriptores
        Suscriptor primerSuscriptor = new Suscriptor("primerSuscriptor");
        Suscriptor segundoSuscriptor = new Suscriptor("SegundoSuscriptor");

        // Añadimos los suscriptores al canal de YT
        miCanalDeYoutube.addSubscriber(primerSuscriptor);
        miCanalDeYoutube.addSubscriber(segundoSuscriptor);

        // Indicamos al canal que notifique a los suscriptores
        miCanalDeYoutube.notifySubscribers();

        // Quitamos uno de los suscriptores y notificamos de nuevo
        miCanalDeYoutube.removeSubscriber(primerSuscriptor);
        miCanalDeYoutube.notifySubscribers();

    }
}
