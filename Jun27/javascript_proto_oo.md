## __proto__
Objects in JS can be chained. If property in one object is not found, JS will look for it in another. This is possible because of `__proto__`. `__proto__` points to another object.

```
var animal = { eats: true };
var rabbit = { jumps: true };
// DEPRECATED.
rabbit.__proto__ = animal;

// Works straightforward
rabbit.jumps
> true

// rabbit has no property 'eats'. When property not found runtime
// will look down the inheritance chain, in rabbit.__proto__ which
// is the animal, and animal has property eats.
rabbit.eats
> true
Object {jumps: true}
    jumps: true
    __proto__: Object
        eats: true
        __proto__: Object
```

Prototype is an object to which `__proto__` points. In this example `animal` is `rabbit`s prototype.

```
for (prop in rabbit) {
    console.log(prop);
}
> jumps
> eats

for (prop in rabbit) {
    if (rabbit.hasOwnProperty(prop)) {
        console.log(prop);
    }
}
> jumps
```

#### Object Literal and Object.create()
```
var data1 = {};
var data2 = Object.create(null);

data1.toString();
> "[object Object]"

data2.toString();
> Uncaught TypeError: data2.toString is not a function(…)

// If just Object will be passed to create method,
// data2 will be a function, not an object.
var data2 = Object.create(Object.prototype);
data2.toString();
> "[object Object]"
```

#### prototype

There is `__proto__` and `prototype`. The `__proto__` is the actual prototype, but **don't use it**. It is slow and it is not (in modern engines) designed to be manipulated. A function's `.prototype` is actually the prototype of things made by it.

> Javascript kind-of readopted the idea of constructors and classes: every function is eligible to be a constructor by calling it with the new keyword, and by setting the .prototype property of that function, you tell Javascript that "when this function is used as a constructor, set up the object's prototype-ish field to this object." So that's not actually the prototype of the function - its prototype is, of course, Function.prototype.


To set for every new object a `__proto__` in a constructor:

```
var animal = {
    eats: true
};

function Rabbit(name) {
    this.name = name;
}

// For Rabbit prototype is animal.
Rabbit.prototype = animal;

var rabbit = new Rabbit('Snuff');
rabbit.eats
> true
```

`prototype` works only with objects and meaningfil in constructors.

#### Constructor property
Every function owns a `prototype` by default.

```
function Rabbit() {}

// Rabbit.prototype = { constructor: Rabbit };

Object.getOwnPropertyNames(Rabbit.prototype);
> ["constructor"]
```
