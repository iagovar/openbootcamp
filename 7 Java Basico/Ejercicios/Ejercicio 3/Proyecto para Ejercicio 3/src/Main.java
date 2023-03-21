import java.util.Scanner;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        System.out.println("Ejercicio que permite concatenar n textos");

        // arraylist de strings a concatenar (Vacía)
        ArrayList<String> lista = new ArrayList<String>();

        // Bucle que pregunta por strings a concatenar
        while (true) {
            System.out.print("Ingrese una palabra o una lista de palabras separadas por un espacio: ");
            String palabra = new Scanner(System.in).nextLine();

            // Añade la palabra ingresada a la lista
            lista.add(palabra);

            // Pregunta si quiere finalizar la introducción, y sale del bucle si es así
            System.out.println("¿Desea continuar? (S/N)");
            String respuesta = new Scanner(System.in).nextLine();
            if (respuesta.equalsIgnoreCase("N")) {
                break;
            }


        }

        // Imprime la lista de palabras
        System.out.println("Lista de palabras: ");
        System.out.println(concatenar(lista));
    }

    public static String concatenar(ArrayList<String> lista) {
        String resultado = "";
        for (int i = 0; i < lista.size(); i++) {
            resultado += lista.get(i);
        }
        return resultado;
    }

}