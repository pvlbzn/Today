import java.io.IOException;
import java.net.InetAddress;

/*
 * Find an IP address of a given host.
 */
public class JDig {

    public static void main(String[] args) throws IOException {
        String hostname = args[0];
        try {
            InetAddress addr = InetAddress.getByName(hostname);
            System.out.println("IP address: " + addr.getHostAddress());
        } catch (IOException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }

}
