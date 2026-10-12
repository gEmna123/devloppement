
import java.rmi.Naming;

public class Client {
    public static void main(String[] args) throws Exception {
        Hello obj = (Hello) Naming.lookup("rmi://localhost:1099/Hello");
        System.out.println(obj.sayHello("Emna"));
    }
}
