# Flask
Basic application example

```
from flask import Flask

app = Flask(__name__)


@app.route('/')
def user(name):
    return name

if __name__ == '__main__':
    app.run(debug=True)

```

## View Function
`@app.route([path])` is a decorator with which flask registers the decorated function as a route. This function is called a *view function*. It is expected to return *response*.

`@app.route` source code:

```
def route(self, rule, **options):
    def decorator(f):
        endpoint = options.pop('endpoint', None)
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator
```

Thus

```
# Decorated view function
@app.route('/')
def user(name):
    return name


# Regular function
def user(name):
    return name

# Connect a URL rule
app.add_url_rule('/user/<name>', 'user')
# Register user function as a handler to user URL rule
app.view_functions['user'] = user
```

`app.view_functions` is a dictionary of all views functions registered. This is how `view_functions` looks like with `about`, `index`, `user`, `views` functions registered as a view handlers:

```
{
    'static': <bound method _PackageBoundObject.send_static_file of <Flask 'main'>>,
    'about': <function about at 0x105b85ae8>,
    'index': <function index at 0x105986048>,
    'user': <function user at 0x1067de378>,
    'views': <function views at 0x1067ed6a8>
}
```

## Request Response Cycle
`request` object encapsulates some received HTTP request. Instead of passing each request as an argument to a handler function Flask uses *context* to temporarily make some objetcs globally accessible.

```
from flask import request

def index():
    return request.geaders.get('User-Agent')
```

Here the `request` object is used as s global variable. However it can not be truly a global variable because of a multithreading. Application may proccess multiple requests at the same time. Contexts enable Flask to make pre defined variables globally accessible to a thread without interfering with the other threads.

There are two contexts

- Application context
- Request context

```
# flask/globals.py

# ...

# context locals
_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()

current_app = LocalProxy(_find_app)
request = LocalProxy(partial(_lookup_req_object, 'request'))
session = LocalProxy(partial(_lookup_req_object, 'session'))
g = LocalProxy(partial(_lookup_app_object, 'g'))
```

*Application context*: `current_app`, `g`. `current_app` is the application instance for the active app. `g` is an oject that the app can use for temporary storage during one req/res cycle.

*Request context*: `requests`, `session`. `request` is the req object which encapsulates HTTP request. `seesion` is the user session which is a dictionary that the application can ise to store values that are persists between req/res cycles.

Context are pushed before dispatching a request and removed after request is handled. In between the `currept_app` and `g` are available to the thread.

## Request Dispatching
Flask looks up the URL given in the req in the app's URL map.

```
app.url_map

Map([
    <Rule '/about' (HEAD, OPTIONS, GET) -> about>,
    <Rule '/views' (HEAD, OPTIONS, GET) -> views>,
    <Rule '/' (HEAD, OPTIONS, GET) -> index>,
    <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
    <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>
])
```

Where `(HEAD, OPTIONS, GET)` are the *request methods* that are handled by the route.


## Hooks
There is a way to register common functions to be invoked before or after each request is dispatched to a view handler.

`before_first_request` registers a function to run before the first req
`before_request` registers a function to run before each request

`after_request` registers a function to run after each request (if no unhandled exception iccurred)
`teardown_request` registers a function to run after each request (no matter exception or not)

Common pattern is to communicate though `g` context variable.


# Response
View function (handler) is expected to return a valid response to a request. HTTP protocol specifies not only the body but the headers as well. Header such as *status code*. 

```
class BaseResponse(object):
    # ...
    def __init__(self, response=None, status=None, headers=None,
                 mimetype=None, content_type=None, direct_passthrough=False):
                 # Implementation
```

To perform more complicated response use response constructor

```
from flask import make_response

@app.route('/')
def index():
    resp = make_response('<h1>Cookie</h1>')
    resp.set_cookie('key', 'value')
    return resp
```

Redirects, *302* are achieved with a `redirect` function

```
from flask import redirect

@app.route('/')
def index():
    return redirect('http://www.another.url/path')
```

Special function abort:

```
from flask import abort. It doesnt return control back to the function, it gives control back to the web server by raising an exception.

@app.route('/article/<id>')
def get_article(id):
    a = load_article(id)
    if not a:
        abort(404)
    # etc
```
