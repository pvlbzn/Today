## `curl`

`curl` - transfer a URL

`curl` is a tool to transfer data from or to a server. It supports many prolocols (see `man curl`, full manual is 2K lines). `curl` have many useful tricks like proxy, authentication, ftp uploads, etc. It powered by `libcurl`.

`curl` really helps to test your API or understand another fast and efficient. 

### URL

Multiple URLs or parts:

```
http://page.{one,two,three}.io
```

Or sequence:

```
ftp://ftp.download.com/file[0001-1000].jpg
```

### HTTP verbs

```
$ curl --request GET http://google.com
```

Request can be `GET`, `POST`, `PUT`, `DELETE`, etc, all http verbs. `GET` used by default. 

```
$ curl --request POST protocol://site.com/api/endpoint \
  --data 'username=user&password=password'
```

### Parameters
`curl` has 669 variations in 120 options. I'll try to dive into basics and most used functionality. `curl` without parameter will just download content of passed URL.

```
$ curl google.com | cat

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>302 Moved</TITLE></HEAD><BODY>
<H1>302 Moved</H1>
The document has moved
<A HREF="link">here</A>.
</BODY></HTML>
```

Automatical redirect on `302` temporary redirection and `301` moved permamently.

```
$ curl -L google.com | cat

// Prints actual google page.
```

#### Headers

To see actual request and response headers use `-v`

```
$ curl google.com -v
// Header
// Body
```

To see *only* response header use `-I`.

To modify your header use `-H`:

```
$ curl -H "Accept: application/xml" -H "Content-Type: application/xml protocol://site.io"
```


Further reading: [link](https://curl.haxx.se/docs/httpscripting.html)
