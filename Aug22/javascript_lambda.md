# Lambda or Anonymous Function
Anonymous function means a function without a name. In lambda calculus all lambdas are anonymous. In JS not all lambdas are anonymous, and not all anonymous function are lambdas.

## Lambda Isn't an Anonymous Function
Lambda expression is used as data. The function is passed as an argument to another function, returned as a value from a function, or assigned to variables or data structures. This is the definition of a first class functions and in JS any function can be used as a lambda because functions are first class.

If function is not used as data - it is not used as a lambda.

```
const foo = [1, 2, 3, 4, 5];
const bar = foo.map(function bar (n) {
    return n * 2;
});
```

`bar` is a lambda, but it is not anonymous, while

```
(msg) => {
    const fmt = JSON.stringify({
        time: Date.now(),
        msg
    });
    console.log(fmt)
}('foo');
```

is an anonimous function, but not a lambda.

