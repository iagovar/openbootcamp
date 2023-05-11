
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) {

        ////////////////////////////////////////////////
        // Probando reverse string
        ////////////////////////////////////////////////
        System.out.println("Probando el reverse string");

        while (true) {
            Scanner miScanner = new Scanner(System.in);
            String texto = miScanner.nextLine();
            try {
                if (texto.isEmpty()) {
                    System.out.println("Por favor introduce un texto.");
                    continue;
                } else {
                    System.out.println(reverse(texto));
                    break;
                }
            } catch (NoSuchElementException e) {
                System.out.println("Devolvió: " + e.getMessage());
            }
            miScanner.close();
        }

        ////////////////////////////////////////////////
        // Crea un array unidimensional de Strings y recórrelo, mostrando únicamente sus valores.
        ////////////////////////////////////////////////

        System.out.println("Mostrando los valores del Array unidimensional de strings:");

        String[] miPrimerArray = {"Hola", "esto", "es", "un", "array", "de", "strings"};

        for (String texto: miPrimerArray) {
            System.out.print(texto + " ");
        }

        ////////////////////////////////////////////////
        // Crea un array bidimensional de enteros y recórrelo, mostrando la posición y el valor de cada elemento en ambas dimensiones.
        ////////////////////////////////////////////////
        System.out.println("\nPintando el array bidimensional:");

        int[][] miSegundoArray = {{1,2,3}, {4,5,6}, {7,8,9}};

        for (int fila = 0; fila < miSegundoArray.length; fila++) {
            for (int columna = 0; columna < miSegundoArray[fila].length; columna++) {
                System.out.print(miSegundoArray[fila][columna] + " ");
            }
            System.out.print("\n");
        }

        ////////////////////////////////////////////////
        // Crea un "Vector" del tipo de dato que prefieras, y añádele 5 elementos. Elimina el 2o y 3er elemento y muestra el resultado final.
        ////////////////////////////////////////////////

        System.out.println("\nCreando un vector y añadiéndole 5 elementos:");

        Vector<Integer> miVector = new Vector<>(5);

        System.out.print("\nAñadido al vector:");
        for (int i = 0; i < 6; i++) {
            miVector.add(i); // Añade los cinco vectores
            System.out.print(" " + i);
        }

        System.out.print("\nAhora el vector es: " + miVector);
        System.out.print("\nEliminamos el 2o y 3er elemento con removeElementAt(indice) en el índice 1, pero haciendo dos veces la operación (al eliminar un elemento cambiarán todos los índices)");
        miVector.removeElementAt(1);
        miVector.removeElementAt(1);
        System.out.print("\nAhora el vector es: " + miVector);

        ////////////////////////////////////////////////
        // Indica cuál es el problema de utilizar un Vector con la capacidad por defecto si tuviésemos 1000 elementos para ser añadidos al mismo.
        ////////////////////////////////////////////////

        System.out.println("\nEl problema de la capacidad por defecto de los vectores\n" +
                "Es que el memory allocation cambiaría constantemente.\n" +
                "Vector usa copias en memoria de Arrays cada vez que tiene que acortarse\n" +
                "o alargarse, lo que implica duplicaciones momentáneas del espacio del array\n");

        ////////////////////////////////////////////////
        // Crea un ArrayList de tipo String, con 4 elementos. Cópialo en una LinkedList. Recorre ambos mostrando únicamente el valor de cada elemento.
        ////////////////////////////////////////////////

        String[] tempArray = {"Texto", "para", "el", "ArrayList"};
        ArrayList<String> miArrayList = new ArrayList<>(4);
        miArrayList.addAll(List.of(tempArray));

        System.out.println("Mostrando el Arraylist:");
        for (String elemento: miArrayList) {
            System.out.print(elemento + " ");
        }

        System.out.println("\nCopiando a linkedList y mostrando:");

        LinkedList<String> miLinkedList = new LinkedList<>(miArrayList);

        for (String elemento : miLinkedList) {
            System.out.print(elemento + " ");
        }

        ////////////////////////////////////////////////
        // Crea un ArrayList de tipo int, y, utilizando un bucle rellénalo con elementos 1..10. A continuación, con otro
        // bucle, recórrelo y elimina los numeros pares.
        //
        // Por último, vuelve a recorrerlo y muestra el ArrayList final.
        // Si te atreves, puedes hacerlo en menos pasos, siempre y cuando cumplas el primer "for" de relleno.
        ////////////////////////////////////////////////

        // Creamos el arraylist y lo llenamos de elementos del 1 al 10
        ArrayList<Integer> miSegundoArrayList = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            miSegundoArrayList.add(i);
        }

        System.out.println("\nArrayList con todos los enteros del 1 al 10: " + miSegundoArrayList);

        // Eliminamos los números pares del arraylist
        for (int i = 0; i < miSegundoArrayList.size(); i++) {
            if (miSegundoArrayList.get(i) % 2 == 0) {
                miSegundoArrayList.remove(i);
            }
        }

        System.out.println("\nArrayList sin los números pares: " + miSegundoArrayList);

        ////////////////////////////////////////////////////////
        // Crea una función DividePorCero. Esta, debe generar una excepción ("throws") a su llamante del tipo
        // ArithmeticException que será capturada por su llamante (desde "main", por ejemplo).

        // Si se dispara la excepción, mostraremos el mensaje "Esto no puede hacerse".
        //
        // Finalmente, mostraremos en cualquier caso: "Demo de código".

        System.out.println("Probamos a dividir un número entre cero:");

        try {
            int resultado = dividePorCero(7);
        } catch (Exception e) {
            System.out.println(e);
        }


        ////////////////////////////////////////////////////////
        // Utilizando InputStream y PrintStream, crea una función que reciba dos parámetros: "fileIn" y "fileOut".
        // La tarea de la función será realizar la copia del fichero dado en el parámetro "fileIn" al fichero dado en "fileOut".
        ////////////////////////////////////////////////////////

        String ficheroLocal = "C:\\Users\\Iagovar\\Documents\\MEGA\\MEGAsync\\apuntes\\openbootcamp\\7 Java Basico\\sandbox\\idea-projects\\ejercicios-7-8-9\\archivo-de-entrada.txt";
        String ficheroDeSalida = "C:\\Users\\Iagovar\\Documents\\MEGA\\MEGAsync\\apuntes\\openbootcamp\\7 Java Basico\\sandbox\\idea-projects\\ejercicios-7-8-9\\archivo-de-salida.txt";

        System.out.println("Probando a copiar un fichero");

        String miCopia = copiaDeFichero(ficheroLocal, ficheroDeSalida);

        System.out.println(miCopia);



    }

    public static String copiaDeFichero(String fileIn, String fileOut) {
        try {
            InputStream miInput = new FileInputStream(fileIn);
            byte[] datos = miInput.readAllBytes();

            PrintStream miOutput = new PrintStream(fileOut);
            miOutput.writeBytes(datos);

            return "Copiado fichero exitosamente";
        } catch (Exception e) {
            return e.getMessage();
        }
    }

    public static int dividePorCero(int numero) throws ArithmeticException {
        if (numero != 0) {
            throw new ArithmeticException("Esto no puede hacerse, no puedes dividir " + numero + " entre cero");
        } else {
            return 0;
        }
    }

    public static String reverse(String texto) {

        int longitud = texto.length();
        int contador = 0;
        String[] nuevoTexto = new String[longitud];

        /*
        Lo que hace este método es lo siguiente:

        Longitud = 5;

        Pos 0 = Longitud-1 (4) - contador (0); contador++;
        Pos 1 = Longitud-1 (4) - contador (1); contador++;
        Pos 2 = Longitud-1 (4) - contador (2); contador++;
        Pos 3 = Longitud-1 (4) - contador (3); contador++;
        Pos 4 = Longitud-1 (4) - contador (4); contador++;

         */
        for (int indice = 0; indice < longitud; indice++) {
            int indiceTextoOriginal = longitud - 1 - contador;
            char temporal = texto.charAt(indiceTextoOriginal);
            nuevoTexto[indice] = "" + temporal; // Type casting chungo, java es un guirigay
            contador++;
        }

        return String.join("", nuevoTexto);

    }
}
