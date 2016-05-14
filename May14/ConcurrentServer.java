import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ConcurrentServer {

    private static int port = 24000;

    public static void main(String[] args) {

        try {
            final ExecutorService service = Executors.newCachedThreadPool();
            ServerSocket serverSock = new ServerSocket(port);
            while (true) {
                Socket sock = serverSock.accept();
                service.submit(new AnswerHandler(sock));
            }
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    static class AnswerHandler implements Runnable {
        Socket socket;

        public AnswerHandler(Socket s) {
            socket = s;
        }

        public void run() {
            System.out.printf("Connection: %s\n", socket.getInetAddress());
            try {
                DataInputStream in   = new DataInputStream(socket.getInputStream());
                DataOutputStream out = new DataOutputStream(socket.getOutputStream());

                String msg = in.readLine();
                double x = Double.parseDouble(msg);
                out.write(toByteArr(squareIt(x)));

                socket.close();
            } catch (IOException e) {
                System.out.println(e);
            }
        }

        private double squareIt(double x) {
            return Math.pow(x, 2);
        }

        private byte[] toByteArr(double x) {
            return Double.toString(x).getBytes();
        }
    }

}
