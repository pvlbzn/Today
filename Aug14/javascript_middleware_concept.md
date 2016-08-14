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
app.get('/some/path/:uname', (req, res, next) => {
    if (req.params.uname == 'whoever') next('route');
    else next();
```
