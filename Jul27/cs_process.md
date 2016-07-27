## Process
Process is an instance of a program. It contains the programs code and its current activity. Process may be made up of multiple threads of execution that execute instructions concurrently.

A program is a *passive* collection of instructions, while a *process* it the actual execution of those instructions.

Multitasking is a method to allow multiple processes to share CPUs. Each CPU executes a single task at a time. A common form of multitasking is a *time-sharing*. In time-sharing context switches are performed rapidly. This illusion of the execution of multiple processes simultaneously is called *concurrency*.

A process is consists of the following resources:

- An image of the executable machine code associated with a program
- Some region of virtual memory, which includes the executable code, process-specifc  data (i/o), a call stack, and a heap to hold itermidiate computation data generated during a run time
- OS descriptors of resources
- Security attributes (permissions)
- Context (processor state). The state is typically stored in computer registers when the process is executing, and in memory otherwise.

