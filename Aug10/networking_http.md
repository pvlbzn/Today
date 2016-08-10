## How It Looks Like
A simple python server will echo everything what it receives. Postman app will be used to generate requests. While raw theory is great, it is always better to look at what actually server takes.

#### GET

Request:

```
GET localhost:25000/api
```

Response: (meaningless data is omited)

```
GET /api HTTP/1.1
Host: localhost:25000
Connection: keep-alive
Cache-Control: no-cache
Accept: */*
```


#### POST
By design, the POST request method requests that a web server accepts and stores the data enclosed in the body of the request message.

There are 4 options how to POST data: form-data, x-www-form-urlencoded, raw, binary.

Difference between form-data and x-www-form-urlencoded is unclear, lets dig in.

> The moral of the story is, if you have binary (non-alphanumeric) data or a significantly sized payload to transmit, use `miltipart/form-data`. Otherwise, use `application/x-www-form-urlencoded`.

In `application/x-www-form-urlencoded` the body of the HTTP message sent to the server in one giant query string.

```
POST /api HTTP/1.1
Host: localhost:25000
Connection: keep-alive
Content-Length: 67
Cache-Control: no-cache
Content-Type: application/x-www-form-urlencoded

some_
key=some_value&another_key=another_value&non_alphanumeric=third_%23%24%25%5E%26
``` 

This thing with non-alphanumeric characters is a literally a big deal with binary data because payload will be trippled.

That is why `multipart/form-data` exists.

```
POST /api HTTP/1.1
Host: localhost:25000
Connection: keep-alive
Content-Length: 266
Cache-Control: no-cache
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary0CDyln1uDJBESJOr


------WebKitFormBoundary0CDyln1uDJBESJOr
Content-Disposition: form-data; name="some_key"

some_value
------WebKitFormBoundary0CDyln1uDJBESJOr
Content-Disposition: form-data; name="non_alphanumeric"

third_#$%^&*()
------WebKitFormBoundary0CDyln1uDJBESJOr--
```

Values arrived correctly in sense of 1 byte as 1 byte. However there are a lot of header files inside which will outweight profit from non encoded data.


#### `application/json`
There is an option to build this communication using JSON.

```
POST / HTTP/1.1
Host: localhost:25000
User-Agent: curl/7.43.0
Accept: */*
Content-Type: application/json
Content-Length: 20

{"name":"user_name"}
```

For example:

```
POST /auth?username=uname

{
    "value": "user_password"
}
```