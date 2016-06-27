## Property

```
0. var person = Object.create(null);
1. var person = {};
```

What is a property, named data property, looks like? It has a name (String) and a value. Property can be enumerable, configurable, wtirable. If value is enumerable, it will show up when enumerating over an object using a `for(key in obj)`. If writable - you can replace it. If configurable - you can delete it or change attrs.

```
var person = Object.create(null);

Object.defineProperty(person, 'fname', {
    value: "Yehuda",
    writable: true,
    enumerable: true,
    configurable: true
});

Object.defineProperty(person, 'lname', {
    value: "Katz",
    writable: true,
    enumerable: true,
    configurable: true
});
```

The `Object.defineProperty(object, property, descriptor)` method defines a new property directly on an object, or modifies an existing property on an object and return the object.

```
var conf = {
    writable: true,
    enumerable: true,
    configurable: true
};

var defProp = function (obj, prop, value) {
    conf.value = value;
    Object.defineProperty(obj, prop, conf);
};

var person = Object.create(null);
defProp(person, 'fname', "Yehuda");
defProp(person, 'lname', "Katz");
```

## Prototype
JS object has one extra attribute - a pointer to another object. This pointer is called a `prototype`. If you will try to access property which is not attached to the object, JS will look for it in the prototype. It will follow the *prototype chain* until it sees a `null` value. If `null` is reached it returns `undefined`.

Note: there is `__proto__` and `prototype`. First is the actual object that is used in the lookup chain to resolve methods, etc. Second is the object that is used to build `__proto__` whe you create an object with `new`.





#### Source
Based on Yehuda Katz [article](http://yehudakatz.com/2011/08/12/understanding-prototypes-in-javascript/).