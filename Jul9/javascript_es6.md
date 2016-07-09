## let
`let` is a new `var`, kind of.

#### Block Scope
Yes, `let` has a block scope. `let` will exists only inside {..}.

```
let i = 5;

if (1)
    let i = 15;
```

`i` will be 5.

#### Initialization
While `var` is declared from the beginning, `let` isn't.

```
console.log(a1);
// undefined
var a1 = 15;

console.log(a2);
// error
let a2 = 15;

let a2 = 15;
// error. a2 was already declared
```

#### Life Span
`var` was really screwed:

```
for (var i = 0; i < 10; i++) {}
console.log(i);
// 10

for (let j = 0; j < 10; j++) {}
console.log(j);
// What? j isn't defined
```

## const
Constant.

```
const a = 5;
a = 10; // What? This is constant.
```

Sure when `const` holds a reference then object can be mutated, since it is just accessed through this immutable reference.

## Destructuring Assignment

```
let [a, b] = [1, 2];
let [, d]  = [2, 4];

let [a1, b1, ...c1] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
// c1 is [3, 4, 5, 6, 7, 8, 9, 0];

let [fname='unknown', lname = 'unknown'] = [, 'Simpson'];
// fname is unknown, lname is Simpson
```

## Object Destructuring

```
let obj = {
    a: 'field',
    b: 'field',
    c: 'field'
};

let {a, b: arg2, c: arg3, z='new one'} = obj;
// a is field, as well as b and c. z is new one.
```

A little trick

```
let a, b;
{a, b} = {a: 5, b: 15};
// No, it is not going to work because {} will be threated like a block.

({a, b} = {a: 5, b: 15});
// That is fine.
```

## Functions
Parameters passing and () => syntax.

```
// Parameters can be not only statements but expressions.
function foo(a=15, b=20) {}

// Operator spread and deconstructorisation also works well
function bar({a, b}, ...rest) {}
```

#### name

```
function Fn() {}
f.name              // Fn

let guess = () => {};
// guess.name       // guess
```


## Strings

```
let a = 5;
let b = 15;

console.log('${a} + ${b} = ${a + b}');
```

Also were added a better support of the Unicode.


## Objects

```
let a = 5;
let b = 8;

let exp = {
    a,
    b
};

let name = 'martin';
let user = {
    fname: [name]
};
```

#### getter/setter
There were `Object.getPrototypeOf(obj)`, and now there is `Object.setPrototypeOf(obj, proto)` as well.

#### .assign

```
// Object.assign(target, foo, bar, baz);
let a = { a: 5 };
let b = { b: 8 };
len n = { number: true };

Object.assign(n, a, b);
```

#### .is

```
Object.is(+0, -0);      // false
Object.is(NaN, NaN);    // true
```

#### Methods

```
let b = 15;
let a = {
    b,
    returnB() {
        return b;
    }
};

a.returnB;
```

#### `super`

`super` works through prototype. It is not really about `class`es. `super` works with `[[HomeObject]]`. Only one exception - `() => {}` function has one scope level up `super`. 

```
let animal = {
    walk() {
        console.log("walk");
    }
};

let rabbit = {
    __proto__: animal,
    // Right
    walk() {
        super.walk();
    }

    // No way.
    // walk: function() {
    //      super.wal();
    // }
    
    // Ok
    // walk() {
    //      setTimeout(() => super.walk());
    // }
};

rabbit.walk();
```

`[[HomeObject]]` is kinda immutable. Method is binded to his object for ever.

```
let walk = rabbit.walk();
walk();
// Will print
"walk"
```

Because of `walk` point to its object, `[[HomeObject]]`.


## Class

It is a syntax update, nothing new techically.

```
class ClassName [extends ParentName] {
    constructor
    methods
}
```

```
class User {
    constructor(name) {
        this.name = name;
    }
    
    greet() {
        console.log('Hi ${this.name}');
    }
}

// This is ± is an equolent to the following
function User(name) {
    this.name = name;
}

User.prototype.greet = function() {
    console.log('Hi ' + this.name);
};
```

Function `constrcutor` triggers when called using `new`. Methods are recorded into User.prototype.

However, new and old syntax has some differences. `User` from class can not be called without `new`. `class` like a `let` in case of a scope, it is visible inside a block and in child blocks.

Methods from `class` have traits. Method `greet` has an access to the `super`. All methods work in `use strict`. All methods arent enumerable (they will be absent in for..in).

#### Class Expression

Like a functions, classes can be inlined.

```
let User = class [Name] {
    greet() { console.log('Hey'); }
};
```

#### `get` and `set`

```
class User {
    constructor(fname, lname) {
        this.fname = fname;
        this.lname = lname;
    }

    get fullName() {
        return '${this.fname} ${this.lname}';
    }

    set fullName(n) {
        [this.fname, this.lname] = n.split(' ');
    }
};

// Note syntax of the get/set. No function call.

const user = new User('Jack', 'Blake');
user.fullName;
> Jack Blake
user.fullName = 'Martin Lorenzo';
> Martin Lorenzo
```

#### `static`

```
class User {
    // constructor
    static createGuest() {
        return new User("guest", "unknown");
    }
};
```


## Credits
Code samples and info from [this](https://learn.javascript.ru/) beautiful source.
