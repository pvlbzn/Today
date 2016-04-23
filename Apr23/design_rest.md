###REST

Representational State Transfer is one of the most popular software architectures on the Internet because it is founded on well defined standards, easy to scale.

First occurence was in Roy Thomas Fielding's [dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm). This man also is a co-founder of the HTTP protocol.

*Source: [Astaxie](https://astaxie.gitbooks.io/build-web-application-with-golang/content/en/08.3.html)*.

**Resources**:
Representation Layer is actually the resource presentation layer. Resource is documents, images, etc. These documents can be located by URI.

**Representation**:
Resources are specific information entities that can be shown in a variety of ways withing the presentation layer. TXT as HTML, JSON, XML. Image as jpg, png.

**State Transfer**:
An interactive process is initiated between client and server each time you visit any page of a website. GET, POST, PUT, DELETE.

>The most important principle of web applications that implement REST is that the interaction between clients and servers are stateless; every request should encapsulate all of the required information. 


```

----------------------
	API Frontend					representation
----------------------

----------------------
	Business Logic	  				state/transfer
----------------------

----------------------
		 Data						resource
----------------------

```


![REST API scheme on scale](https://astaxie.gitbooks.io/build-web-application-with-golang/content/en/images/8.3.rest.png?raw=true)


