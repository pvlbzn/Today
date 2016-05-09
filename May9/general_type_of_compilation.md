####JIT

Just-in-time compilation, also known as dynamic transtalion, is compilation done during execution of a program, at run time. JIT is a combination of the two traditional approaches to translation to machine code - AOT and interpretation. 

In theory, JIT combines the speed of compiled code with the flexibility of interpteration, with the overhead of an interpreter and the additional overhead of compiling.

Generaly JIT runs after the program has started and compiles the code (usually bytecode or kind of VM) on the fly. JIT has access to dynamic runtime information whereas a standard compiler doesn't and can make better optimizations like inlining functions that are used frequently, thus JIT can be faster than the host CPU native instruction set. With a cost of the overhead.

<br>

####AOT

Ahead-of-time compilation is the act of compiling a high-level programming language into a native, system-dependent, machine code. Like C.

<br>

-

####Iterpreted

A little bit offtopic, however this is a third type of mainstream programming languages, like Python or Ruby. An interpreter is a program, or some mechanism, that executes any program written in interpreted language. 
