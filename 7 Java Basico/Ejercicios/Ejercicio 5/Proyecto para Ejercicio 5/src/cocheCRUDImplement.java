import java.util.ArrayList;

public class cocheCRUDImplement implements CocheCRUD {

    // Lista de coches
    protected ArrayList<Coche> coches = new ArrayList<Coche>();

    @Override
    public String save(Coche coche) {
        coches.add(coche);
        return "Coche guardado";
    }

    @Override
    public String update(Coche coche) {
        // Actualizamos el coche en la lista
        coches.set(coches.indexOf(coche), coche);
        return "Coche actualizado";
    }

    @Override
    public String delete(Coche coche) {
        // Borramos el coche de la lista coches
        coches.remove(coche);
        return "Coche eliminado";
    }

    @Override
    public ArrayList<Coche> findAll() {
        return coches;
    }
}