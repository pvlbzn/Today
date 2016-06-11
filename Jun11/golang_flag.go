## `flag`

Package flag implements command-line flag parsing.

```
var ip = flag.Int("fname", 555, "help")


// Or bind it to the variable
var fvar int

func init() {
	flag.IntVar(&fvar, "fname", 555, "help")
}

// After declaration call
flag.Parse()
```

Sample program `./flag.go`
