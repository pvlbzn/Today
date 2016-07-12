## Get the Data Back
Most difficult thing in async javascript in the beginning is to design data flow. How data passed around, and how to get it back.

### Callback
Most easiest way is to achieve it via callbacks. Code is in `./cb.js`.

```
function call(url, callback) {
    require(url, (err, resp, data) => {
        let body = data.toString();
        callback(body);
        return;
    });
}
```

The point here is to take data back from async function. Callback may lead to callback hell, but it can be solved by just a code organization.

#### Error First Callback

- The first argument of the callback is reserved for an error object.
- The second argumnt of the callback is reserved for any successful response data.

What actually to do with error: it depends. Error can be trowh and whole app shut. Or, error can be propageted.

```
fs.readFile('/file.postfix', (err, data) {
    if (err) {
        if (err.fileNotFound) {
            // Handle
            return this.sendErrorMessage('file not found');
        }
        if (!err.noPermission) {
            // Propagate
            return next(err);
        }
    }
    ;
}
```

### Other Solutions

- Promise
- Event Emitter
- Stream
- Generator
