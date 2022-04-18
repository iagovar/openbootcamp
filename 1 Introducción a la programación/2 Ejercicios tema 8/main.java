public class Main {
	public static void main(String[] args) {
		Persona fulano = new Persona();
		Persona.setNombre("Fulanito");
		Persona.setEdad(30);
		Persona.setTelefono(600100200);

		string nombre = Persona.getNombre();
		int edad = Persona.getEdad();
		int telefono = Persona.getTelefono();

		System.out.println("Nombre: " + nombre + "\nEdad: " + edad + "\nTeléfono: " + telefono);
	}
}

public class Persona {
	private String nombre;
	private int edad;
	private int telefono;

	public string getNombre() {return this.nombre;}
	public int getEdad() {return this.edad;}
	public int getTelefono() {return this.telefono;}

	public void setNombre(nombre) {this.nombre = nombre;}
	public void setEdad(edad) {this.edad = edad;}
	public void setTelefono(telefono) {this.telefono = telefono;}
}