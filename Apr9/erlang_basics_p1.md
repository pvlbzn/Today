### Basics

Invariable variables must begin with an uppercase. In FP variables can't be variable.

```
Five = 5. 
5

one = 1.
** exception error: no match of right hand side value 1

Two = 2#10. 
2

Seven = 2#101 + Two. 
7

Two = 5. 
** exception error: no match of right hand side value 5
```

**Operator `=`**

```
5 = 4. 
** exception error: no match of right hand side value 4

5 = 5.
5

F = 4. 
4

4 = F. 
4
```

**Atoms**

There is a reason why variables can't begin with a lowercase: *atoms*. *Atoms* are literals.

```
a. 
a

atom. 
atom

'This is atom'. 
This is atom

a = 'Atom'. 
** exception error: no match of right hand side value 'Atom'
```

The atom table isnt GC, and so atoms will accumulate until the system tips over, either from memory usage or because 1048577 atoms were declared. Atoms shouldnt be generated dynamically for whatever reason.

**Boolean Algebra**

```
true and false. 
false

false of true. 
true

not true. 
false

true xor true. 
false
```

`and` and `or` always evaluate arguments on both sides of the logical operator, use `andalso` and `orelse` for short-circuit.

```
5 =:= 5. 
true
```

`==` is `=:=`, `!=` is `=/=`.

```
5 == 5.0. 
true

5 /= 5.0. 
false

5 =:= 5.0. 
false
```

