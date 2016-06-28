## Objects
JS has built-in objects such as Date, Array, Object, etc.

When we initialize new object, for example using a object literal notation `var obj = {};`, it will already own some properties. `obj` inherit these properties from `Object`.

```
{}.__proto__.toStrign();
> "[object Object]"
```

1. `var obj = {}` is equals to `var obj = new Object`, where `Object` is a built-in constructor function for objects. Therefore `Object` is a constructor, not an object.
2. On `new Object` new object's `__proto__` is from its constrcutor `prototype`, which is `Object.prototype`.
3. On `obj.toString()` function will be looked in `obj`, and when not found in `Objet.prototype`.

```
typeof Object
> "function"

typeof Object.prototype
> "object"

var N = function() {
	this.f = function() { console.log('hi'); }
}

typeof N
"function"

typeof N.prototype
"object"

var o = {}
o.__proto__ == Object.prototype
> true
```

An example:

```
var Cup = function(type, volume) {
	var empty = true;
	this.type = type;
	this.volume = volume;
	this.pour = function() {
		empty = false;
		console.log('The cup is full.');
	}
	this.drink = function() {
		empty = true;
		console.log('The cup is empty.');
	}
}

/* Cup.prototype is an object with two paramenters: constructor function,
 * and __proto__ object.
 */

var cupObj = new Cup('water', '300');

cupObj.__proto__ === Cup.prototype;
> true

cupObj.__proto__.constructor === Cup;
> true
```

#### Object.prototype.__proto__ === null
This means that Object.prototype object is a last object in inheritance. This is why all objects inherits form the Object (Object in meaning Object.prototype, because Object is a constructor).




