## Not Same But Identical

```
type stack []uintptr

func callers() stack {
    return make([]uintptr, 20)
}
```

This will work because the underlying type in identical. Thus, `stack` is not the same as `make([]uintptr, 20)` but identical.

```
type first []uintptr
type second []uintptr

func c1() first {
    return make([]uintptr, 20)
}

func c2() second {
    return second(c1())
}

func main() {
	fmt.Println(c1())	
	fmt.Println(c2())	
}
```

Will print two empty arrays with a lenght of 20.