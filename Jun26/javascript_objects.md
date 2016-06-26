## Object
An object is a collenction of properties, and property is an association between a key and a value. A property's value can be a function, in which case the property is known as a method. Some objects are predefined in the browser or you can define your own objects.

```
objectName.objectProperty
```

Object property is basically the same as a regular variable, expcept that it is attached to the object.

```
var weather = new Object();
weather.temp = 31;
weather.wind = 15.5;
weather.atm = 760.9;
weather.hum = 43.8;
```

JS understands two kinds of *property accessors*: a dot notation and an array-like bracket notation. Dot notation asks for an object to access its property, while array-like notation do the same thing but in associative array approach because JS object is looks like dictionary or hashmap.

```
// Not every kind of property can be accessed using dot notation:
var weird = new Object();
weird[''] = 'Property with a name empty string';
weird['1'] = 'Or just a numeric value';
weird['this string is basically evaluated to the property name'] = 'ok.';

weird
> Object {1: "Or just a numeric value", "": "Property with a name empty string", this string is basically evaluated to the property name: "ok."}

var weirdPropName = 'this string is basically evaluated to the property name';
weird[weirdPropName];
> "ok."
```

Object, as really beeing like associative arrays, can be emunerated:
- for in loop
- Object.keys(obj)
- Object.getOwnPropertyNames(obj)


#### New Object

```
// Using new
var obj1 = new Object();

// Using literal notation
var obj2 = {};

// Or, using a constructor function
function Car(make, model, year) {
	this.make = make;
	this.model = model;
	this.year = year;
}

var car = new Car("Super", "3000", 1960);
```

Objects can be composed:

```
function Person(name, age) {
	this.name = name;
	this.age = age;
}

function Car(owner, make, model, year) {
	this.owner = owner;
	this.make = make;
	this.model = model;
	this.year = year;
}

var owner = new Person("Jeana", 31);
var car = new Car(owner, "Mazda", "zx350", 1990);
```

`Object.create()` it is useful because it let programmer to create from prototype object without having to define a constructor func.

```
var Anmal = {
	type: "Invertebrates",
	displayType : function() {
		console.log(this.type);
	}
}

var a1 = Object.create(Animal);
var a2 = Object.create(Animal);

a1.displayType();
> Invertebrates

a2.type = "Fishes"
a2.displayType();
> Fishes
``` 

All objects inherits from at least one another object. The object **inherited from** is known as the **prototype**. 

Define properties for an object:

```
var c1 = new Car("mazda", 1983);

Car.prototype.color = null;

for (param in c1) { console.log(param); }
> year
> model
> color

```

#### Methods

A method is a function associated with an object.

```
var bike = {
	drive: function(speed) {
		console.log(speed);
	} 
};

bike.drive(50);

// As from previous example
var car = new Car(owner, "Mazda", "zx350", 1990);

// Functon displayInfo
function displayInfo() {
	console.log("Owner is: " + this.owner.name + "\n" +
		"Model is: " + this.model + "\n");
}

// Now it is a method of the car object.
car.displayInfo = displayInfo;
car.displayInfo();

> Owner is: Jeana
> Model is: zx350

// Now, using a prototype
var car2 = new Car(owner, "bmw", "X6", 2012);
Car.prototype.displayInfo = displayInfo;
car2.displayInfo();

> Owner is: Jeana
> Model is: X6
```

`this` indicates and object to which the method belongs. `this` beeing called from a global execution context refers to the global object. In a function context `this` value is depend by how function is called. When a funtion is called as a method of an object, its `this` value is set to the object the method called on.


#### Get, Set

```
function O(n) {
	this.a = n;
	this.get = function() {
		return this.a * 2;
	};
	this.set = function(s) {
		this.a = s / 2;
	};
}


var o1 = new O(15);
o1.set(71);
o1.get();
> 71
```
