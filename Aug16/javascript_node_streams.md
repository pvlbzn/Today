# Stream
Conceptually *streams* is nothing new, it is a Unix streams, like `cat .bash_history | grep 127.0.0.1`, which main goal is to connect small components and build a big thing out of them. In unixes streams are implemented by the shell `|` pipe. In node [stream](https://nodejs.org/docs/latest/api/stream.html) module is used by the core libs. Like a unix pipes node's streams can be pluged (output of one stream goes to an input of another).

> A stream is an abstract interface for working with streaming data in Node.js. The stream module provides a base API that makes it easy to build objects that implement the stream interface.


## Why
Consider following code:

```
const server = http.createServer((req, res) => {
    fs.readFile(__dirname + '/file.txt', (err, data) => {
        res.end(data);
    });
});
```

And the same thing using streams.

```
const server = http.createServer((req, res) => {
    const stream = fs.createReadStream(__dirname + 'file.txt');
    stream.pipe(res);
});
```

These examples performs one task but differently. 

**First** example isn't great because it buffers all `file.txt` into the memory for each request. If this file will be large enough it will consume considerable amount of memory (especially on users with slow connections) and user will wait until data is buffered. 

**Second** example pipes file to the `res`. `res` and `req` are both streams, which means that `fs.create[kind]Stream()` can be used.

https://github.com/substack/stream-handbook