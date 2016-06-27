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

```
var man = Object.create(null);
defProp(man, 'sex', "male");

var u = Object.create(man);
defProp(u, 'fname', "Yehuda");
defProp(u, 'lname', "Katz");

u
> Object {fname: "Yehuda", lname: "Katz"}

for (prop in u) { console.log(prop); }
> fname
> lname
> sex

u.sex
> male
u.fname
> Yehuda
u.lname
> Katz

Object.getPrototypeOf(u);
> Object {sex: "male"}
```

#### Seting Props
The same things from above can be achieved in a simplier way:

```
var person = Object.create(null);
person.fullName = function() {
	return this.fname + ' ' + this.lname;
};
var man = Object.create(person);
man.sex = 'male';

var u = Object.create(man);
u.fname = "Yehuda";
u.lname = "Katz";

u.sex;
> male
u.fullName()
> Yehuda Katz
```

#### Object Literal
```
// Literal notation
var person = {
	fname: 'Kate',
	lname: 'Johnson'
}

// Which is approximate sugar for
var person = Object.create(Object.prototype);
person.fname = 'Kate';
person.lname = 'Johnson';
```

Object literals always set the newly created objects prototype to an object located at `Object.prototype`. The default `Object.prototype` dictionary comes with a number of the methods, which can later be overriden.

```
var john = { fname: 'John', lname: 'Swonson'};
john.toString();
> "[object Object]"

var john = {
	fname: 'John',
	lname: 'Swonson',
	toString: function() { 
		return this.fname + " " + this.lname;
	}
};

john.toString()
> "John Swonson"
```

However literal object syntax can inherit only `Object.prototype`.

## Native OO
```
// This is a constructor AND an object ot use as the prototype
// for new objects.
var Person = function(fname, lname) {
	this.fname = fname;
	this.lname = lname;
};

Person.prototype = {
	toString: function() {
		return this.fname + " " + this.lname;
	}
};

var mark = new Person("Mark", "Miller");
mark.toString();
> "Mark Miller"
```

In essence, a JS class is just a function object that serves as a constructor plus an attached prototype objects. 


#### Source
Based on Yehuda Katz [article](http://yehudakatz.com/2011/08/12/understanding-prototypes-in-javascript/).