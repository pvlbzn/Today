## Node HTTP
A simple http server using node js API

```
// Load built-in module http
const http = require('http')

const app = http.createServer((req, resp) => {
    let respStr = `${req.url} ${req.method} ${JSON.stringify(req.headers)}` 
    resp.writeHead(200, {
        "Content-Type": "text/plain"
    })
    resp.end(respStr)
})

app.listen(25000, 'localhost')
```

```
$ curl -X POST http://localhost:25000/some/path
/some/path POST {"host":"localhost:25000","user-agent":"curl/7.43.0","accept":"*/*"}%

$ curl http://localhost:25000/another/path
/another/path GET {"host":"localhost:25000","user-agent":"curl/7.43.0","accept":"*/*"}%
```

#### Routes
There is an obvious way to do it:

```
const nonoptimal = http.createServer((req, res) => {
    if (req.url == '/') {
        res.writeHead(200, {
            "Content-Type": "text/html"
        });
        res.end('root');
    }
    // Handle all the routes
    else {
        res.writeHead(404, {
            "Content-Type": "text/plain"
        });
        res.end('404');
    }
});

nonoptimal.listen(25001, 'localhost');
```

As a benefit there are no external dependencies. However this solution is far from neat. To solve it better some supporting functions can be built, or framework used.


## Express
The same functionality can be achieved using Express framework. Express is a routing and middleware web framework.

```
const xapp = express();

xapp.use((req, res) => {
    res.writeHead(200, {
        "Content-Type": "text/plain"
    });
    res.end("Hi.");
});
```

#### Middleware
Middleware functions are functions that have access to the `req` object, `res` object and the `next` function in application **request-response cycle**. If the current middleware function doesnt end the req-res cycle, it must call `next` function to pass control to the next middleware function.

```
function middleware(req, res, next) {
    // Do whatever you want to do with every single req-res cycle
    console.log('middleware');
    next();
}

app.use(middleware);

app.get('/', (req, res) => {
    res.end('see console');
});
```

Each request to the root path will trigger `middleware` function. The order of middleware loading is important: functions that are loaded first are also executed first.

