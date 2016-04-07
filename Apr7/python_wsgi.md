###WSGI
-
####Web Servers and Software
**Web servers** serve up responses. Client process sends a request, server sends response back, and sit around waiting to the next request. Web server is in charge of serving. **Software** doesnt sit around, it only exists at execution time.

####WSGI
[PEP 3333](https://www.python.org/dev/peps/pep-3333/). Python Web Server Gateway Interface is a simple and universal interface between web servers and Python web applications or frameworks. Basically WSGI is a solution to problem that there are lots of a frameworks, and Web Server Gateway Interface makes that every WSGI framework can work on every WSGI server.

Java has many web app frameworks available, Java's *servlet* API makes it possible for apps written with any Java web app framework to run in any web server that supports the servlet API.

WSGI specifies two interfaces:
	- Web server interface to communicate with the application
	- Application interface to communicate with the webserver

Thats pretty much it. I'll dig into the detail later, after sockets.

