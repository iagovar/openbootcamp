public class Main {
	public static void main(String[] args) {

		Persona fulano = new Persona();
		fulano.setNombre("Fulanito");
		fulano.setEdad(30);
		fulano.setTelefono(600100200);

		String nombre = fulano.getNombre();
		int edad = fulano.getEdad();
		int telefono = fulano.getTelefono();

		System.out.println("Nombre: " + nombre + "\nEdad: " + edad + "\nTeléfono: " + telefono);
	}
}

public class Persona {
	private String nombre;
	private int edad;
	private int telefono;

	public String getNombre() {return this.nombre;}
	public int getEdad() {return this.edad;}
	public int getTelefono() {return this.telefono;}

	public void setNombre(String nombre) {this.nombre = nombre;}
	public void setEdad(int edad) {this.edad = edad;}
	public void setTelefono(int telefono) {this.telefono = telefono;}
}