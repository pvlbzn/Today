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

