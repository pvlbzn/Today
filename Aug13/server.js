const http = require('http');

// Initial
const app = http.createServer((req, resp) => {
    let respStr = `req url: ${req.url} method: ${req.method}\n` + 
                  `headers: ${JSON.stringify(req.headers)}`;
    resp.writeHead(200, {
        "Content-Type": "text/plain"
    });
    resp.end(respStr);
});

app.listen(25000, 'localhost');

// Routing
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

// Express
const express = require('express');
const xapp = express();

xapp.use((req, res) => {
  res.writeHead(200, {
    "Content-Type": "text/plain"
  });
  res.end("Hi.");
});

xapp.listen(25002, 'localhost');

// Middleware
const yapp = express();

function logger(req, res, next) {
  console.log(`logging: ${req.method} ${req.url}`);
  next();
}

yapp.use(logger);
yapp.get('/', (req, res) => {
  res.end('see console');
});

yapp.listen('25004', 'localhost');

