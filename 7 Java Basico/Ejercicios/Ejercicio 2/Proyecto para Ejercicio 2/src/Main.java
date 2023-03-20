import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // Solicita introducir un precio al usuario
            // Create a scanner object
            Scanner input = new Scanner(System.in);

            // Read user input
            double precio;

            while (true) {
                try {
                    System.out.println("Introduce un precio");
                    precio = input.nextDouble();
                    break;
                } catch (Exception e) {
                    System.out.println("El valor debe ser numérico");
                    input.nextLine(); // Limpiar el buffer de scanner
                }
            }

        // Solicita introducir una cantidad de productos al usuario

        double cantidad;

        while(true) {
            try {
                System.out.println("Introduce una cantidad de productos");
                cantidad = input.nextDouble();
                break;
            } catch (Exception e) {
                System.out.println("El valor debe ser numérico");
                input.nextLine(); // Limpiar el buffer de scanner
            }
        }

        // Imprime el precio total de los productos incluyendo el IVA
        double precioTotalSinIVA = precio * cantidad;
        double precioTotalConIVA = calcularIVA(precioTotalSinIVA);

        System.out.println("El precio total con IVA es: " + precioTotalConIVA);

    }

    // Recibe un precio y calcula su IVA
    public static double calcularIVA(double precio) {
        return precio * 1.21;
    }
}
