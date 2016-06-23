## Functions

Functions is a good thing about JS. In the following example different scopes is present. Scope may have some folding layers.

```
var landscape = function() {
  var result = "";
  var flat = function(size) {
    for (var i = 0; i < size; i++)
      result += "_";
  };
  var hill = function(size) {
    result += "/";
    for (var i = 0; i < size; i++)
      result += "'";
    result += "\\";
  };
};
```

This scoping is useful:

```
var count = function() {
  var i = 0;
  return function() {
    i += 1;
    return i;
  }
}
```

After `var c = count()` assignment of the function to `c`, `c` will own its instance of local variable `i`. `i` is a state of the `c`. Call to `c()` will trigger a one more function, which will mutate state of the `i` and return in.

The difference between function declaration, using a variable or using a named function definition is in the script initialization. The long story short:

```
say_func();
say_var();

var say_var = function() {
  console.log("Hi");
};

function say_func() {
  console.log("Hello.");
};
```

Will produce:

```
"Hello."
"error"
"TypeError: say_var is not a function
``` 

Function declaration is not a part of top-to-bottom control flow.


Arguments. Well, JS is open minded:

```
var f = function(x) {
  console.log(x);
};

f(5,4,3,2,11);
f();
```

Will produce `5` and `undefined`. That's it. No errors, no crashes, no worries.

Reqursion:

```
function find(n) {
  function find(start, history) {
    if (start == n)
      return history;
    else if (start > n)
      return null;
    else
      return find(start + 5, "(" + history + " + 5)") ||
             find(start * 3, "(" + history + " * 3)");
  }
  return find(1, "1");
}
```

`console.log(find(99));` -> `"((((1 + 5) + 5) * 3) * 3)"`

Or, to screw a performance:

```
function isEven(n) {
    if (n === 0)
      return true;
    else if (n === 1 || n === -1)
      return false;
    else
      if (n > 0) 
        return isEven(n - 2);
      else 
        return isEven(n + 2);
}
```

## Data Structure

JS has objects and arrays.

```
l = [1,2,3];
console.log(l.length)

console.log(l[-1])				// Error
console.log(l[0:2])				// Error

console.log(l.slice(0, 2))		// OK
```

Yes, no slicing, no negative indexes.

```
l = [1,2,3];
len = "len";
ght = "gth";
console.log(l[len + ght])
```

Example from above actually legit. `l[len+ght]` is the same to `l.lenght`. Oh my.



