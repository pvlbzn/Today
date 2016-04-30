###Go Proverb

> Don't just check error, handle them gracefully

<br>

Source: [Dave Cheney blog](http://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully).

####Three Strategies

- Sentinel errors
- Error types
- Opaque errors

<br>

####error Type

By convention, error is the last return value with a type `error`. `errors.New` constructs a basic `error` value with a given message.

```
// Bad example:
func f(n int) (int, error) {
    if n > 0 {
        return -1, errors.New("must be 0 or negative")
    }
    return n, nil
}
```

Its possible to use custom types as `errors` by implementing the Error() method.

```
type customError struct {
    arg     int
    prob    string
}

func (e *customError) Error() string {
    return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f(n int) (int, error) {
    if n > 0 {
        return -1, &customError(n, "must be 0 or negative")
    }
    return n, nil
}
```



