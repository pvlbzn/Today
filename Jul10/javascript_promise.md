## Promise

Promise is a special object, which contains a *state*. First promise pending, when promise is fulfilled (success) or rejected (error).

```
                +-----------+
promise         | fulfilled |
+---------+     +-----------+
| pending |
+---------+     +-----------+
                | rejected  |
                +-----------+
```

General syntax is

```
const promise = new Promise((resolve, reject) => {
    // Will be called automatically.
    // Async stuff goes here
});

promise.then(onFulfilled, onRejected);

// or, alternatively
promise.then(onFulfilled);

promise.then(null, onRejected);
promies.catch(onRejected);
```

`throw` will trigger reject.

An example:

```
const promise = new Promise((res, rej) => {
    // Will trigger fulfilled with result 'result'
    setTimeout(() => { res("result"); }, 1000);
});

// Listeners
promise.then(
    result => {
        console.log("Fulfilled: ${result}");
    },
    error => {
        console.log("Rejected: ${error}");
    }
);
```

Promise is kind of one use only. It can not change its mind. If promise is *resolve* than it is for ever. So, only one state.

#### Promissify

```
function httpGET(url) {
    return new Promise((res, rej) => {
        let xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        
        xhr.onload = () => {
            if (this.status == 200) {
                res(this.response);
            } else {
                let err = new Error(this.statusText);
                err.code = this.status;
                rej(err);
            }
        };
        
        xhr.onerror = () => {
            rej(new Error("Network Error"));
        };
    });
}

// Usage

httpGet("/api/req").then(
    response => console.log("Fulfilled: ${response}"),
    error => console.log("Rejected: ${error}")
);
```


