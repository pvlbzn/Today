## Types

JavaScript has 5 primitive types:
- null
- boolean
- string
- number

Everything else is an object. These types actually can be an object too.

```
// Boolean primitive type
> var bool1 = true
> typeof(bool1)
'boolean'

// Bolean object type
> var bool2 = new Boolean(false)
> typeof(bool2)
'object'
```

## String
It is a set of elements of 16-bit unsigned integer values. Strings are immutable.

#### Primitive and Object
There are two types of the string: object and primitive.

```
var prim = 'I am a primitive.'
var obje = new String('I am an object.')

prim
'I am a primitive.'

obje
String {0: "I", 1: " ", 2: "a", 3: "m", 4: " ", 5: "a", 6: "n", 7: " ", 8: "o", 9: "b", 10: "j", 11: "e", 12: "c", 13: "t", 14: ".", length: 15, [[PrimitiveValue]]: "I am an object."}
```

JS automatically converts primitives to `String` objects when `String` methods are used on primitives.
