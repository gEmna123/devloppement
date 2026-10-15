package RMI;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) throws Exception {
        HelloImpl obj = new HelloImpl();

        LocateRegistry.createRegistry(1099);

        Naming.rebind("rmi://localhost:1099/Hello", obj);

        System.out.println("Serveur prêt !");
    }
}
