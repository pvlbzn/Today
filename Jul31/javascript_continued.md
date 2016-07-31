### Immediately Invoked Function Expressions

```
const y = 15;

let x = (() => {
    console.log('hi');
    return y * 2;
}) ();
> hi

x
> 30
```

Or with arguments

```
let [n1, n2] = [15, 15];
((a, b) => { return a + b; }) (n1, n2);
> 30
```

### Modules
Modules helps to define private implementation details that are hidden from the outside world, while public API is accessible from the outside.

```
function User() {
    let uname, password;

    function login(user, pw) {
        uname = user;
        password = pw;
    }

    function getName() {
        return uname;
    }

    const publicAPI = {
        login,
        getName
    };

    return publicAPI
}

// Yes, User without new. User is just a function, not a class.
let u1 = User();
u1.login('Dude', 'dude_on_sequrity);

u1.getName();
> Dude

u1.password
> undefined
```

The whole thing works because of *lexical scoping*, which is the part of *closure* concept. `login` and `getName` owns a closure over `uname` and `password`. This means that `login` and `getName` still can access `uname` and `password` after `User` quits. `publicAPI` is an object with two references `login` and `getName`.

`u1` holds references of `login` and `getName` and they has pointers to the `uname` and `password` therefore they are can not be GC'ed.

