#### Anonymous Closure

Self calling function, which provides privacy and state:

```
(function() {
    console.log(1);
}());
```

Function is wrapped into `()` because it creates function expression, not a function declaration.

#### Global Import

JS has an *implied globals* feature. If no variable found in the scope chain the variable is assumed to be global. We can pass globals as parameters to function.

```
(function ($) {
    // Now here is access to globals jQuery
}(jQuery));
```

#### Module Export

```
var Module = (function () {
    var m = {};
    var pVar = 1;
    var pMethod = function () {
        // Block
    }

    m.mProp = 15;
    m.mMethod = function() {
        // Block
    };

    return m;
}());
```
