## Asynchronous JavaScript + XML
AJAX is a term to describe a set of web technologies on the client side to create asyc web apps. The whole thing works mainly with `XMLHttpRequest` object supported by a bunch of other normal client-side things such as markup languages, JS by itself, browser API like DOM.


#### `XMLHttpRequest` 
[`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) is an API that provides client functionality for transferring data between a client and a server.

Working with `XMLHttpRequest` feels really similar to any Java http library.

```
const req = new XMLHttpRequest();
req.onreadystatechange = () => {
    // Handle response
}
```

`XMLHttpRequest.readyState`:
- 0 uninitialized
- 1 loading
- 2 loaded
- 3 interactive
- 4 complete
