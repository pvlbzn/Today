# `filter`, `map`, `reduce`
These functions came from a world of functional languages. JS supports them natively, they are speceficated in ECMA-262. The good part in JS that JS supports functional programming paradigm. This is not unique to languages (for example Python also supports kind of functional style) but in JS it is natural, more natural than OOP at least.

These three functions defined on arrays. Each will be implemented separately for the understanding purpose. However it is always better to use buitl-in or standard library because of the fact that language by itself is a useless set of syntatix rules and constractions. Language only makes sence together with its 'execution platform'. In case of JS most likely that platform is V8. V8 is a virtual machine which applies its optimizations during execution (complicated topic actually). To allow to a virtual machine do its work in a best possible way better always use standard language features.


## `filter`
Filter is a simple function on a dataset. It filters out the data which is not satisfy a filter condition and returns the data which passed the condition.

```
const arr = [1, 2, 3, 4, 5]

function isEven(n) {
    return n % 2 === 0
}

const evenArr = arr.filter(isEven);
```

`evenArr` now has `[2, 4]` state.

Filter function might be implemented is the following way

```
function filter(data, condition) {
  const res = [];

  for (let item in data) {
    if (condition(data[item]))
      res.push(data[item]);
  }

  return res;
}
```

'Functional' style functions is a *pure* kind of functions. They return new data, they dont mutate an existing data.


## `map`
`map` is mapping each dataset element to the function. Since it is a functional function it returns a new array.

```
function map(data, fn) {
  const res = [];

  for (let item in data)
    res.push(fn(data[item]));

  return res;
}
```


## `reduce`
`reduce` is reducing a dataset to a single value.

```
function reduce(data, typeResolution, fn) {
  let red = typeResolution;

  for (let item in data)
    red = fn(red, data[item]);

  return red;
}
```

`typeResolution` is a naive hack for easier implementation.
