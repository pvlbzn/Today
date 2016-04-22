import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.Paths;

/*
 * Worst HTTP server ever. Learning purpose only. It was written without actual
 * API knowledge and server development experience. Most likely that everything
 * is bad or very bad.
 */
public class HelloWeb {

    public static void main(String[] args) {
        int served = 0;
        try {
            ServerSocket server = new ServerSocket(8080);
            long start = System.currentTimeMillis();
            while (true) {
                Socket client = server.accept();
                if (client != null) {
                    handleConnection(client);
                }
                client.close();
                served++;
                if ((System.currentTimeMillis() - start) > 1000) {
                    System.out.println(served);
                    served = 0;
                    start = System.currentTimeMillis();
                }
            }
        } catch (IOException ioe) {
            System.err.println(ioe);
            System.exit(1);
        }
    }

    public static void handleConnection(Socket client) {
        try {
            PrintWriter out = new PrintWriter(client.getOutputStream(), true);
            serveHeader(out);
            servePage(out);
            out.close();
        } catch (IOException ioe) {
            System.err.println(ioe);
            System.exit(1);
        }
    }

    public static void serveHeader(PrintWriter out) {
        out.print("HTTP/1.1 200 OK\r\n");
        out.print("Content-Type: text/html\r\n");
        out.print("Connection: Close\r\n\r\n");
    }

    public static void servePage(PrintWriter out) {
        try {
            String path = Paths.get("").toAbsolutePath().toString();
            BufferedReader reader = new BufferedReader(new FileReader(path + "/src/index.html"));
            String msg;
            while ((msg = reader.readLine()) != null) {
                out.printf("%s\r\n", msg);
            }
            reader.close();
        } catch (FileNotFoundException e) {
            System.err.println(e);
            System.exit(1);
        } catch (IOException ioe) {
            System.err.println(ioe);
            System.exit(1);
        }
    }

}
