## Middleware
There are 5 different types of a middleware:

- Application level
- Router level
- Error handling
- Built-in
- Third-party


#### Application Level
To bind middleware to an *aplication layer* use `use()` and `METHOD()` (where method is GET/PUT/POST verbs in lowercase) on the application instance.

```
const app = express();

// Function is executed every time the app receives a request.
app.use([middleware]);

// Function is execuded for any type of HTTP req on a given path
app.use('/rest/api/path', [middleware]);

//Function is execuded for GET method on a given path
app.get('/rest/api/path', [middleware]);

// Middleware can be stacked (a middleware sub-stack)
app.use('/what/ever/path', [middleware], [middleware]);
```

There can be more than one handler for a unique path:

```
// next('route') work with middleware loaded using app.METHOD or router.METHOD
app.get('/some/path/:uname', (req, res, next) => {
    if (req.params.uname == 'whoever')
        next('route');
    else next();
}, (req, res, next) => {
    res.render('normal');
});

app.get('/some/path/:uname', (req, res, next) => {
    res.render('special');
});
```


#### Router Level Middleware
Router level middleware works similarly with app level but it is bound to an insance of `Router()`. Here is an example of the same functionality:

```
const app = express();
const router = express.Router();

// Executed for every single request
router.use((req, res, next) => {
    console.log('router middleware');
    next();
});

router.use('/some/path/:uname', (req, res, next) => {
    // First call
    next();
}, (req, res, next) => {
    // Second one
    next();
});

// Do whatever else and mount the router on the app
app.use('/', router);
```


#### Error-handling Middleware
It takes **four** arguments thus express resolves this function as a error-handling middleware by its signature.

```
app.use((err, req, res, next) => {
    console.log(err.stack);
    res.status(500).send('see console log');
});
```


#### Built-in Middleware
Express by itself has only one built-in function `static`, and its based on [serve-static](https://github.com/expressjs/serve-static?_ga=1.211798293.1024317270.1470639148). However express previously had more dependencies and functionality, now they are [here](https://github.com/senchalabs/connect#middleware).

Function signature is: `express.static(root, [options])` where `root` is an argument specifies the root directory from which to serve static assets.
Use docs to see what kind of options can be.

Application can use more than one static directory.


#### Third-party Middleware
Well, it is a middleware from third-party. Express maintains the [list](https://expressjs.com/en/resources/middleware.html) of most widely used middleware and it is good place to consult.

