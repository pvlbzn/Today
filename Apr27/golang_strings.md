###Strings

Strings are read-only slices of bytes with a bit of extra syntatic support from the language.

```
slash := "/usr/name"[0]

// Take a normal slice of bytes and create a string out of it:
str := string(slice)

// Or
slice := []byte(usr)
```

Important consequence of slice-like design is that creating a substring is ver efficient.

TODO: [read](https://blog.golang.org/strings).
