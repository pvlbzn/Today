####Java

Java world is **huge**. Sometimes confusing. Especially on alternative platforms such as Android, where used different virtual machine, not Oracle nor OpenJDK.

<br>

####Android and Java

Android system doesn't include JVM. Android uses Android Runtime (ART) which replaces Dalvik process virtual machine. ART and Dalvik are compatible runtimes running Dex bytecode, thus Dalvik apps should run fine on ART. On Dalvik programs was written on Java and compiled to bytecode for the JVM, which them translated to Dalvik bytecode and stored in .dex, Dalvik EXecutable.

Dalvik uses JIT, [just-in-time](https://en.wikipedia.org/wiki/Just-in-time_compilation), from 2.2, which optimize the execution by continally profiling apps each time they run and dynamically compiling frequently executed short segments of their bytecode into native machine code.

ART inroduces the AOT, [ahead-of-time](https://en.wikipedia.org/wiki/Ahead-of-time_compilation), 
