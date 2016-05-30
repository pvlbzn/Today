## URI
A Uniform Resource Identifier that identifies an abstract or physical resource, as apecified by [RFC 2396](http://www.ietf.org/rfc/rfc2396.txt).

`http://username:password@host:8080/directory/file?query#fragment` URI recipe

```
COMPONENT		EXAMPLE
Scheme			http
Scheme-specific	//username:password@host:8080/directory/file?query#fragment
Authority		username:password@host:8080
User Info		username:password
Host 			host
Port 			8080
Path 			/directory/file
Query 			query
Fragment 		fragment
```

**Absolute**: `http://android.com/somefile.txt`

**Relative**: `somefile.txt`



### Adndroid URI and Uri
Android has it's own implementation `android.net.Uri`, Java has it's own `java.net.URI`. The difference is that android's version is more forgiving, and performs less checks, hence more porformant.

`anroid.net.Uri` class `public abstract class Uri` is immutable, Java's implementation of RFC 2396 is mutable.