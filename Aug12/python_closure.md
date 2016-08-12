## Closure Support

How closure looks like in, say js:

```
function counter() {
    let count = 0
    function add() {
        return ++count
    }
    return add
}
```

The direct port to python will look like:

```
def counter():
    count = 0
    def add():
        count += 1
        return count
    return add
```

There is a difference - the last snippet won't work: `UnboundLocalError: local variable 'count' referenced before assignment`.

#### `nonlocal`
`nonlocal` is another scoping variable, like `global`.

```
def counter():
    count = 0
    def add():
        # Point to count
        nonlocal count
        count += 1
        return count
    return add
```

The reason for `nonlocal` existance that python automatically initialize new variables in a scope, therefore in the first example variable `count` is not in the scope. `nonlocal` introduces `count` to the current scope, thereafter everything works as intended.

