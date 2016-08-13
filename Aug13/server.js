const http = require('http')

const app = http.createServer((req, resp) => {
    resp.writeHead(200, {
        "Content-Type": "text/plain"
    })
    resp.end("Hi")
})

app.listen(25000, 'localhost')