###Java Sockets

Recently I learned basics on *sokets* in Unix as host OS, and some OO implementation in Python. Now I want to see how this things works in Java.

####Echo Server

```
import java.net.*;
import java.io.*;

public class EchoServer {

	psvm main(String[] args) throws IOException {
		int port = Integer.parseInt(args[0]);
		
		try (
			ServerSocket ss = new ServerSocket(Integer.parseInt(args[0]));
			Socket cs = ss.accept();
			PrintWriter out = new PrintWriter(cs.getOutputStream(), true);
			BufferedReader in = new BufferedReader(new InputStreamReader(cs.getInputStream()));
			) {
				String input;
				while ((input = in.readLine()) != null)
					out.println(input);
			} catch (IOException e) {
				System.out.println("Port: " + port);
				System.out.println(e.getMessage());
		}
	}
}

```

Compile it, run it with some port, like 25000 and

```
nc localhost 25000

Echo?				// My request
Echo?				// Server response
```
