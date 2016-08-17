## Arrow Function
An arrow function expression has a shorter syntax compared to function expressions and lexically binds the `this`. Last thing is important one:

```
function User(uname) {
    this.uname = uname;
}

User.prototype.getName = () => {
    return this.uname;
}
```

Call to `User.getName()` will return `undefined` because it is `undefined` since arrow function does not create its own `this` context, rather it captures the `this` value of the enclosing context. If this case there is no `uname` in global context, thus `undefined` is returned.

```
function User() {
    this.accessLevel = 0;

    setInterval(function foo() {
        this.accessLevel++;
        console.log(this.accessLevel);
    }, 500);
}

const u = new User();
```

This example will be printing `NaN` for ever. `NaN` because function `foo` has its own `this`.

```
function User() {
    const that = this;
    this.accessLevel = 0;

    setInterval(function foo() {
        that.accessLevel++;
        console.log(that.accessLevel);
    }, 500);
}

const u = new User();
```

This example will print 1, 2, 3, 4, 5 etc because now it has a proper contextual pointer.

Since *arrow function* doesn't has its own `this`

```
function User() {
    this.accessLevel = 0;

    setInterval(() => {
        this.accessLevel++;
        console.log(this.accessLevel);
    }, 500);
}

const u = new User();
```

it will print 1, 2, 3, 4, 5 etc as expected.

Therefore *arrow function* is not drop in replacement for a *function expression*, it behaves differently.
