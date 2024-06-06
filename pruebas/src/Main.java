class UsuarioPedros {
    String nombre;
    String apellidos;
    String Tamano;
    int edad;
    String direccion;
    String telefollo;
}



public class Main {
    public static void main(String[] args) {
        UsuarioPedros marta_ostia = new UsuarioPedros();
        marta_ostia.nombre  = "Marta";
        marta_ostia.apellidos = "Perez Ferrandiz";
        marta_ostia.Tamano = "Muy grande";
        marta_ostia.edad = 50;
        marta_ostia.direccion = "Pedrosa de Valdelucio";
        marta_ostia.telefollo = "600695836";

        UsuarioPedros francisco_ostia = new UsuarioPedros();
        francisco_ostia.nombre  = "Francisco";
        francisco_ostia.apellidos = "Barriuso Bravo";
        francisco_ostia.Tamano = "Null";
        francisco_ostia.edad = 48;
        francisco_ostia.direccion = "San Pedro de Ojeda";
        francisco_ostia.telefollo = "660287895";

        System.out.println(marta_ostia.nombre);
        System.out.println(marta_ostia.apellidos);

        System.out.println(francisco_ostia.nombre);
        System.out.println(francisco_ostia.apellidos);

        for (int i = 0; i <= 30; i = i + 3){
            System.out.println("el peine me mide: " + i + " Cm");
        }

        System.out.println("no hay peine");
    }
}
