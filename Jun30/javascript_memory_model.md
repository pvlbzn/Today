## Life Cycle
JS values are allocated when things (objects, strings, etc) are created and GCed after a while. 

1. Allocate the memory
2. Use the allocted memory (r/w)
3. Release the allocated memory

Usually third part is explicit in low-level languages.

#### I. Allocation in JS
```
// Allocates memory for a number
var num = 512;
// Allocates memory for a string
var str = "Me?";

// Allocates memory for an object and its values
var obj = {
    a: 1,
    b: null
};

// Allocates memory fot the array and its values
var arr = [1, null, 'str'];

// Allocates a callable object
function f(n) {
    return n;
}

/*
*  Some fucntion calls result in object allocation
*/

// Allocates a Date object
var today = new Date();

// Allocates a DOM element
var dom = document.createElement('div');
```

#### II. Using the allocated memory
Every time when variable is read or written.

#### III. Release the allocated memory
The hardest thing is to find when the allocated memory is not needed any longer. In in low level languages this point is straightforward in JS it is not. Higher level languages embed a piece of software - GC.

## GC
GC rely on references. For instance JS object has a reference to its prototype (implicit ref) and to its properties values (explicit reference). In this context, the notion of object is extended to broader than in regular JS and also contains function scopes.

#### Reference Counting
Idea is simple: if there is pointer to the object - this object is in use, otherwise GC this object. If object has 0 references which pointing it, it will be GCed.

```
var obj = {
    prop1: {
        prop2:
    }
}

var objProp1 = obj.prop1
// No more pointer to the obj
obj = null

// However it can not be GCed because there is a reference
// which point to the prop1 preperty of the obj
objProp1 = null
// Now the whole thing can be GCed
```

#### Mark-and-sweep
Mark-and-sweep: an object is unreachable. Periodically GC, starting from the roots (root is a global object), find all object that are referenced from these roots, then all object referenced from these and et cetera. Starting from the roots, the FC will thus find all **reachable** objects and collect all non-reachable objects.
