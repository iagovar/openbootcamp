import java.util.List;

public interface CocheCRUD {

    public String save(Coche coche);

    public String update(Coche coche);

    public String delete(Coche coche);

    public List<Coche> findAll();
}
