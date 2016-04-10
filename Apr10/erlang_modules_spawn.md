###Modules, exports, spawn

```
-module(modulename).
-export([function/N]).

function(Argument) -> ...
```

Module name should be the same with a filename, must start with a small letter because technically the module name is an atom.

Export declaration tells which function can be called from outside, like Golang function with a uppercase letter or public in Java. `[]` means list of, function_name/number of arguments.


```
spawn(module_name, function_name, [Arg1, Arg2, ..., ArgN])
```

`spawn` in an Erlang primitive that creates a concurrent process and returns a process identifier.

When `spawn` is evaluated, the Erlang runtime system creates a new process (not an OS process, a lightweight Erlang process). *PID* (a process identifier) can be used to interact with the process.

*OOPL analogy*: Modules are like classes, processes are like objects. `spawn` creates a new process by running a method defined in a module. In Java, new creates a new obj by running a method defined in a class.
