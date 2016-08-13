## Express Framework
Express is a kind of flask or sinatra in the world of nodejs platrofm. It's great for small things, which consumes not that much memory with a great CPU utilization due to event loop.

### Node HTTP
A simple http server using node js API

```
const http = require('http')

const app = http.createServer((req, resp) => {
    resp.writeHead(200, {
        "Content-Type": "text/plain"
    })
    resp.end("Hi")
})

app.listen(25000, 'localhost')
```




