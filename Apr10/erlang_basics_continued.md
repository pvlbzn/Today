####Erlang, functional perspective

**= operator**:
`X = 1` bind a value 1 to the variable X. It looks like "assign the int 1 to the var X", but this is incorrect. `=` is not an assignment operator, it's actually a *pattern matching operator*.

**Modules**:
Erlang programs are built from a number of parallel processes. Processes evaluate functions that are defined in modules. Modules are files with the extension `.erl` and must be compiled before they can be run.

Compilation. See `hi.erl`.

```
$ erl
1> c(hi). 
{ok,hi}
2> hi:start(). 
Hi.
ok
```

`c(name)` compiles the code in the file name.erl.

```
$ erlc hi.erl
$ erl -noshell -s hi start -s init stop
Hi.
```

`hi start` evaluates `hi:start()`, `init stop` evaluates `init:stop()`(terminate the Erl session).
