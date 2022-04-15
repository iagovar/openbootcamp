public class Main {

  public static float sumArbitraryParams(float param1, float param2, float param3) {
    float resultado = param1 + param2 + param3;
    return resultado;
  }

  public static void main(String[] args) {
    /*
    Primera parte.
    Crear una función con tres parámetros que sean números que se suman entre sí.
    Llamar a la función en el main y darle valores..
    */
    float resultado = sumArbitraryParams(20,20,20);
    System.out.println("El resultado de la suma de parámetros es: " + resultado);

    /*
    Segunda parte.

    Crear una clase coche con una variable que contenga el número de puertas,
    y una función/método que permita agregar puertas a la instancia.

    Después crear un nuevo objeto "miCoche" en el main y añadirle una puerta.

    A continuación, mostrar en consola el número de puertas del coche.
    */

    Coche miCoche = new Coche();
    miCoche.incrementarPuertas(2);
    System.out.println("El número de puertas es " + miCoche.puertasCoche);

  }
}


public class Coche {

  int puertasCoche = 5;

  public void incrementarPuertas(int masPuertas) {
    this.puertasCoche += masPuertas;
  }

}