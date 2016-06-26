#### Prototype-based
This is an OOP model that doesn't use classes, instead in accomplishes the behavior of any class and then reuses it by decorating existing *prototype* object. This is not most popular OOP model and this is an interesting thing about JS.

#### Namespace
In JS a namespace is just another object containing methods, properties, objects. Create one global object and all stuff inside will be namespaced.

```
// If app exists - use this global object, or create a new one
// which will encapsulate everything.
var APP = APP || {
	...
};
```

Instead of

```
function addListener(foo, bar, baz) {
	// Stuff
}
```

Use this approach

```
APP.event = {
	addListener: function(foo, bar, baz) {
		// Stuff
	}
	removeListener: function(foo, bar, baz) {
		// Stuff
	}
}

APP.common = {
	validateName: function(name) {
		// Validate.
	}
	validatePhone: function(phone) {
		// Validate.
	}
}

APP.common.validateName("Jess1ca");
```

With this approach functions and methods are namespaced and they are free from name collisions.


#### Custom Object
**Every** object in JS on an instance of the `Object`.

```
// empty Person constructor
var Person = function () {
	console.log('instantiated');
};

var p1 = new Person();
> "instantiated"
var p2 = new Person();
> "instantiated"
```

Every action declared in the class gets executed at the time of instantiation.

Properties are variables contained in the class. They can be accessed using `namespace.propName` dot notation, or using `this` which points onto namespace.

Methods are functions which follows the properties logic.

```
var Person = function(name) {
	this.name = name;
};

Person.prototype.hey = function() {
	console.log("Hey, I'm " + this.name);
};

var p3 = new Person("Eiek");
p3.hey();
> "Hey, I'm Eiek"

// Methods are just regular functions, which are objects, so
var stollenFunc = p3.hey;
stollenFunc();
> "Hey, I'm	"			// This part depends on environment
var name = 'global namespace';
stollenFunc();
> "Hey, I'm global namespace"

stollenFunc.call(p3);
> "Hey, I'm Eiek"
```

#### call()

`stollenFunc.call(p3)` expression is interesting one. From documentation: the `call()` method calls a function with a given `this` value and argumentds provided individually.

`func.call(this, arg1, arg2, ...)`

`call()` is useful for constructor chain.

```
function Product(name, price) {
	this.name = name;
	this.price = price;
}

// Product called usign call method, which called agaist a Paper
// object, thus name and price will be set to the Paper object.
function Paper(name, price) {
	Product.call(this, name, price);
	this.category = 'goods';
}

var a4 = new Paper('A4 paper', 11);
a4
> Paper {name: "A4 paper", price: 11, category: "goods"}
```

Or an another use: invoke an anonymous function

```
var collection = [
	{ foo: 'bar', bar: 'baz'};
]

for (var i = 0; i < collection.length; i++) {
	(function(i) {
		this.print = function() {
			console.log(this.foo, this.bar);
		};
		this.print();
	}).call(collection[i], i);
}
```