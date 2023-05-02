

public class Main {
    public static void main(String[] args) {

        // Creamos un objeto cocheCRUD
        CocheCRUD cocheCRUD = new cocheCRUDImplement();

        // Creamos un Coche
        Coche miCoche = new Coche(
                "Ford",
                "Mustang",
                2020,
                50000,
                "Rojo");

        // Mostramos los atributos del objeto Coche
        System.out.println(miCoche);

        // Guardamos el coche en la lista
        System.out.println(cocheCRUD.save(miCoche));

        // Vamos a crear un segundo coche para que luego usar findAll() salgan dos
        Coche miCoche2 = new Coche(
                "Fiat",
                "Panda",
                2020,
                70000,
                "Negro");

        // Guardamos el segundo coche en la lista
        System.out.println(cocheCRUD.save(miCoche2));

        // Imprimimos todos los coches (deberían salir dos)
        System.out.println(cocheCRUD.findAll());

        // Los arraylist en Java lo que contiene son referencias a memoria, no copias,
        // de manera que cambiar los atributos de, por ejemplo, miCoche2, debería reflejarse
        // al imprimir todo el contenido del arraylist.

        // Cambiamos la marca de miCoche2 de fiar a Ferrari
        miCoche2.setMarca("Ferrari");

        // Imprimimos todos los coches (deberían reflejarse los cambios en el segundo objeto)
        System.out.println(cocheCRUD.findAll());

        // Borramos el primer objeto, y debería desaparecer de la lista
        // ya que se pasa por referencia
        System.out.println(cocheCRUD.delete(miCoche));
        System.out.println(cocheCRUD.findAll());

    }
}