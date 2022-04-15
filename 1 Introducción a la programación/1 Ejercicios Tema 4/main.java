public class Main {

	public static void main(String[] args) {
		float numeroIf = -5;

		if (numeroIf > 0) {
			System.out.println("numeroIf es positivo");
		} else if (numeroIf == 0) {
			System.out.println("numeroIf es cero");
		} else {
			System.out.println("numeroIf es negativo");
		}

		while (numeroIf < 3) {
			numeroIf++;
			System.out.println("El nuevo valor de numeroIf es: " + numeroIf);
		}

		int i = 0;
		do {
			i++;
			numeroIf++;
			System.out.println("El nuevo valor de numeroIf es: " + numeroIf);
		}
		while (i < 1);

		for (int numeroFor = 0; numeroFor <= 3; numeroFor++) {
			System.out.println("El nuevo valor de numeroFor es: " + numeroFor);
		}

		String estacion = "Primavera";

		switch(estacion) {
		case "Primavera":
			System.out.println("La estación es: " + estacion);
			break;
		case "Verano":
			System.out.println("La estación es: " + estacion);
			break;
		case "Otoño":
			System.out.println("La estación es: " + estacion);
			break;
		case "Invierno":
			System.out.println("La estación es: " + estacion);
			break;
		default:
			System.out.println("No se ha establecido una estacion");
			break;
		}
	}

}