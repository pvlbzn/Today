## [Promise](https://github.com/v8/v8/blob/c7eb436d09d5fa10ef41a3312edea2d7a2680126/src/js/promise.js)

Promise is a special object, which contains a *state*. First promise pending, when promise is fulfilled (success) or rejected (error). Promise [spec](http://www.ecma-international.org/ecma-262/6.0/index.html#sec-promise-objects).

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

#### In Depth
`new Promise(executor)` has 4 properties

- PromiseState *state on pending*
- PromiseResult *result*
- PromiseFulfillReactions *list of the functions*
- PromiseRejectReactions *list of the functions*

```
new Promise(executor)
    PromiseState:               "pending"
    PromiseResult:              undefined
    PromiseFulfillReactions:    []
    PromiseRejectReactions:     []
```

```
const promise = new Promise((res, rej) => res(1));
promise.then((res) => { console.log(res); return 'listener 1' });
promise.then((res) => { console.log(res); return 'listener 2' });

> 1
> 1
> Promise {[[PromiseStatus]]: "resolved", [[PromiseValue]]: "listener 2"}

promise.then((res) => { console.log(res); return 'listener 1'; })
       .then((res) => { console.log(res); return 'listener 2'; });

> 1
> listener 1
> Promise {[[PromiseStatus]]: "resolved", [[PromiseValue]]: "listener 2"}
```


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

#### Chaining
Imagine a task: download user data from the server (async), request his data from github (async), when it will be ready - show user's profile picture (async).. and make a chain easy to edit or add features. Yes, promise chain.

```
httpGet('/user/id')
    .then(response => {
        console.log(response);
        let user = JSON.parse(response);
        return user;
    })
    .then(user => {
        console.log(user);
        return httpGet('https://api.github.com/users/${user.name}');
    })
    .then(githubUser => {
        console.log(githubUser);
        githubUser = JSON.parse(githubUser);
        let img = new Image();
        img.src = githubUser.avatar_url;
        img.className = "promise";
        document.body.appendChild(img);
        
        // setTimeout(() => img.remove(), 3000);
        
});
```

Every following .then chain got a result from a previous .then chain. If previous promise returns promise then *result* will be passed, not a promise.

#### Errors
On error, encountered error goes into the closest `onReject`. 

```
httpGet()
    .then()
    .then()
    .then()
    .catch(err -> {
        console.log(err);
    });
```

If error somewhat critical it thowed and catched. That behaviour is similar to try..catch.
