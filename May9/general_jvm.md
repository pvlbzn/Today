####Java Virtual Machine

JVM is an interesting piece of techology. JVM topic is massive, I'll try to cover only basic concepts/principles. JVM is an abstract computing machine that runs a Java program.

- Specification
- Implementation
- Instance

Specification is a document that formally describes what is required of a JVM implemetation. Implementation is a computer program that meets the requirements of the JVM specification. Instance of a JVM is an implementation running in a process that executes a computer program compiled into Java bytecode.

The JVM is an abstract, virtual computer defined by a specs. Specs omits implementation details that are not essential to ensure interoperability: memory layout, GC algorithm, optimizations.

-

For each hardware acrh a different Java bytecoe interpreter is needed. When Java bytecode is executed by an interpreter, the execution will always be slower than the execution of the same program compled into native machine lang. Problem is solved by JIT. JIT translates pieces of bytecode into native machine code while executing.
