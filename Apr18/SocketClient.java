import java.io.*;
import java.net.Socket;

/**
 * Created by pvlbzn on 4/18/16.
 */
public class SocketClient {

    public static void main(String[] args) {

        String server = args[0];
        String path   = args[1];

        try {
            // 80: http
            Socket sock = new Socket(server, 80);
            // Create streams to read/write
            PrintStream out = new PrintStream(sock.getOutputStream());
            BufferedReader in = new BufferedReader(new InputStreamReader(sock.getInputStream()));

            out.println("GET " + path + " HTTP/1.0");
            out.println("Host: " + server);
            out.println("Connection: Close");
            out.println();

            String ln = in.readLine();
            while (ln != null) {
                System.out.println(ln);
                ln = in.readLine();
            }

            in.close();
            out.close();
            sock.close();
        } catch (IOException ioe) {
            System.err.println(ioe.getMessage());
        }
    }

}
