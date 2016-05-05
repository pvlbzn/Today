###Function literals

A function literal represents an anonymous function.

```
func(a, b int, z float64) bool { return a*b < int(z) }
```

It can be assigned or invoked:

```
// Assing.
f := func(x, y int) int { return x+y }

// Invoke.
func(ch chan int) { ch <- ACK }(replyChan)
```

