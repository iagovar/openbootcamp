class Main {
	public static void main(String[] args) {
		// Creamos cliente
		Cliente fulanito = new Cliente();
		fulanito.nombre = "Fulanito";
		fulanito.edad = 30;
		fulanito.telefono = "0034600100200";
		fulanito.setCredito(3000);

		// Creamos trabador
		Trabajador menganito = new Trabajador();
		menganito.nombre = "Menganito";
		menganito.edad = 31;
		menganito.telefono = "0034600100200";
		menganito.setSalario(3500);

		// Mostramos toda la vaina
		System.out.println(
			"Nuestro cliente se llama " + fulanito.nombre
			+ ", tiene " 				+ fulanito.edad
			+ ", su teléfono es " 		+ fulanito.telefono
			+ " y su crédito es " 		+ fulanito.getCredito()
			);

		System.out.println(
			"Nuestro Trabajador se llama " 	+ menganito.nombre
			+ ", tiene " 					+ menganito.edad
			+ ", su teléfono es " 			+ menganito.telefono
			+ " y su salario es " 			+ menganito.getSalario()
			);
		
	}
}

class Persona {
	String nombre;
	int edad;
	String telefono;

	// Lo dejamos sin get y set por probar a modificar sin fns
}

class Cliente extends Persona {
	private int credito;

	public int getCredito() {return this.credito;}
	public void setCredito(int inputCredito) {this.credito = inputCredito;}
}

class Trabajador extends Persona {
	private int salario;

	public int getSalario() {return this.salario;}
	public void setSalario(int inputSalario) {this.salario = inputSalario;}
}