####Modules, Naming

These two topics are closely related in the Go. Here is one [article](https://blog.golang.org/package-names) in the go blog and one [chapter](https://golang.org/doc/effective_go.html#names) in the Effective Go about it.

Code from `net/http` [Write](https://github.com/golang/go/blob/master/src/net/http/request.go)

```
func (r *Request) Write(w io.Writer) error {
    return r.write(w, false, nil, nil)
}
```

Few words on parameters: short name `r` and `w` are not cryptic because `r` clearly stands for `Request` and `w` for `Writer`.

Effective Go describes `bytes` package and `encoding`. The buffer from bytes is named `Buffer` and it belongs to `bytes` package, thus, name is `bytes.Buffer` because it will be accessed as this. Name `bytes.ByteBuffer` is wrong for clear reason. Similar thing with `encoding` `base64`. Its name is `base64`, not `encodingBase64` nor `encoding_base64`, the name is `encoding/base64`.

-

Personally for me, it is a Unix-way, Unix-principle: less is more, when composition choosed over compexity. Like `cat`, `echo`, `grep` Unix command performs a one simple task, however they have huge amount of application when they combined together by pipeline.

An example:

```
echo */* | find . -type f | grep .go | wc -l
```

`echo */*` will output in stdout a all files and folders from all directories. Connected to it `find . -type f` will find all files and output it to the stdout. Connected to previous stdout `grep` will read from its stdin and outputs all files which corresponds to `.go`. Finally, `wc -l` will receive greped files, and count it by line. My $GOPATH contains 1959 .go files.

-

####Modules

Module is powerful conception wich firstly was added as extention in ALGOL and after in MODULA, which was a first "modular programming language". Not much of "modern languages" are "modular", because of popularity of OO concepts (in Java modules are packages, but the arent modules), one of them is Python. Golang was "influenced" by MODULA and Python, besides others.

`fmt` package structure: (tests are exluded)

```
go/src/fmt/
            |
            |------ doc.go
            |------ format.go
            |------ print.go
            |------ scan.go
```

And they are a `fmt` package. For example public function `ReadRune`, from `scan.go` file, can be accessed as `fmt.ReadRune()`, or function `Fprintln`, from `print.go` file, can be accessed as `fmt.Fprintln()`.

This concept is simple, but it actually require a lot of designing and understanding of your project.
