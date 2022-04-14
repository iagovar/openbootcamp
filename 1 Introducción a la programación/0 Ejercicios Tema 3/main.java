public class Main {

  public static float sumArbitraryParams(float param1, float param2, float param3) {
    float resultado = param1 + param2 + param3;
    return resultado;
  }

  public static void main(string[] args) {
    /*
    Primera parte.
    Crear una función con tres parámetros que sean números que se suman entre sí.
    Llamar a la función en el main y darle valores..
    */
    float resultado = sumArbitraryParams(20,20,20);
    System.out.println("El resultado de la suma de parámetros es:\n");
    System.out.println(resultado);

  }
}
