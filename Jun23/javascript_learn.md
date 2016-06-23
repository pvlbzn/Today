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

