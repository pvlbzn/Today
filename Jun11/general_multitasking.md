## Multitasking
Multitasking is a concept of performing multiple processes over a certain period of type by executing them concurrently. Multitasking doesnt imply parallel execution. Multitasking solves problem by scheduling which task may be the one running at any given time. This act of switching CPU from one task to another called a *context switching*. This switching creates the illusion of parallelims if context switched frequent enough.

TLDR multitasking is an illusion. CPU core execute only one task at a time. OS feels as a multitasking because of context switching.

## Context Switching
It is a process of storing and restoring the state, execution context, of a process or thread so that execution can be resumed from the same point at a later time. This enables multiple processes to share a single CPU.

Context switches are usually computationally intensive. That is why 800 threads is slower than 8.