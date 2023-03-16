package miPaquete;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;

public class miClase {
    public static void main(String[] args) {
        // Esta es la clase main del ejercicio 1

        byte unByte = 122; // Valores de -127 a 127
        System.out.println("La var tipo byte tiene el valor " + unByte + ", pero admite desde -127 a 127");

        short unShort = 12978; // Valores de ~-30k a ~30k
        System.out.println("Los tipo short admiten desde -32.768 a +32.768, en este caso: "+ unShort);

        int unInt = 56987234;
        System.out.println("Los int admiten -2,147,483,648 a 2,147,483,647, en este caso: " + unInt);

        long unLong = 10398102983L;
        System.out.println("Los long admiten dígitos tela de largos, pero ocupan 8 bytes siempre. En este caso el valor es: " + unLong);

        float unFloat = 99.0000001F;
        System.out.println("El float es: " + unFloat);

        double unDouble = 912391.19231239890923123D;
        System.out.println("El double es: " + unDouble);

        char unChar = 'a';
        System.out.println("Los char deben ir dentro de comillas simples '', en este caso: " + unChar);

        // PROBANDO ARRAYS

        // Probando la copia de arrays para modificar longitud
        int[] miArray = {1,2,3,4,5,6}; // El array que copiaremos, longitud 6
        //int[] miArrayAmpliado = new int[miArray.length +1]; // Iniciamos uno nuevo, con longitud 6

        int[] miArrayAmpliado = Arrays.copyOf(miArray, miArray.length +1); // Copiamos el array original indicando su nueva longitud

        System.out.println("\nLa longitud del nuevo array es " + miArrayAmpliado.length);

        miArrayAmpliado[miArrayAmpliado.length -1] = 7;

        for(int i : miArrayAmpliado){
            System.out.println(i);
        }

        // PROBANDO ARRAYLIST
        // Igual que los arrays, hay que importarlo
        //
        // En los arraylist todas las colecciones son objetos. Por ello hay que usar wrapper objects para poder usar
        // primitivos, ver: https://www.w3schools.com/java/java_wrapper_classes.asp
        //
        // La ventaja principal de los arraylist es que su longitud es dinámica, no como los arrays normales de Java.

        ArrayList<Integer> miArrayList = new ArrayList<>();
        miArrayList.add(1);
        miArrayList.add(2);
        miArrayList.add(3);
        miArrayList.add(4);
        miArrayList.add(5);
        miArrayList.add(6);
        miArrayList.add(7);
        miArrayList.add(8);
        miArrayList.add(9);
        miArrayList.add(10);

        System.out.println("\nImprimiendo un ArrayList: ");

        for(int i : miArrayList){
            System.out.println(i);
        }


        // Probando HASHMAP
        // Un HashMap es una colección de claves y valores.

        HashMap<Integer, String> miHashMap = new HashMap<>();
        miHashMap.put(1, "Hola");
        miHashMap.put(2, "Mundo");
        miHashMap.put(3, "!");
        miHashMap.put(4, "?");
        miHashMap.put(5, "¿");
        miHashMap.put(6, "Esto es un string largo");

        System.out.println("\nImprimiendo un HashMap: ");

        for(int i : miHashMap.keySet()){
            System.out.println(i + ": " + miHashMap.get(i));
        }






    }
}
