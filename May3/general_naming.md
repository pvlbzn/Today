###Naming

Naming is a one of the hardest things in programming. Here is some tips. [Slides](https://talks.golang.org/2014/names.slide). Since this slides are from Andrew Gerrand (Go developer), this rules mainly applies to the Golang. However, most or the rules are just common sence and must be applied to all of the programming languages around.

####Good names

- Consistent: easy to guess
- Short: easy to type
- Accurate: easy to understand

> The greater the distance between a name's declaration and its uses, the longer the name should be.

Prefer `i` to index, `r` to reader.

<br>

####Parameters
Function parameters are like local variables.

Where the types are descriptive, they should be short. Where types are more ambiguous, the names may provide documentation.

```
func Escape(w io.Writer, s []byte)

func Unix(sec, nsec int64) Time
```

<br>

####Package-level
`bytes.Buffer` and `strings.Reader`. Not `bytes.ByteBuffer` or `strings.StringReader`.

<br>

Long variable names doesn't improve readability. Short, meaningful and concise names are much better.


