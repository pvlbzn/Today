## Stack
Stack is an abstract data type with two principal operations: *push* and *pop*. Push onto stack, pop from the stack. Stack is *last in, first out* data structure.

![Stack](https://upload.wikimedia.org/wikipedia/commons/b/b4/Lifo_stack.png) `CC0 license, public domain`.

From practical perspective programmers usually see a *stack trace* (also known as *stack backtrace*, *stack traceback*) on program crash.

```
Traceback (most recent call last):
  File "so_parse.py", line 167, in <module>
    jobs = get_jobs(url)
  File "so_parse.py", line 51, in get_jobs
    jobs = parse_entry(jobs_raw)
  File "so_parse.py", line 67, in parse_entry
    'summary': get_job_summary(t)} for t in jobs_raw]
  File "so_parse.py", line 67, in <listcomp>
    'summary': get_job_summary(t)} for t in jobs_raw]
  File "so_parse.py", line 80, in find_title
    return correct_title(entry.find(class_='job-link').attrs['title'])
  File "so_parse.py", line 89, in correct_title
    return t / 0
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

Or famous *stack overflow* when space of the stack drains because of bug, for example, in the recursive call.


## Call Stack
Call stack is a stack that stores information about the active subroutines. Subroutine is a sequence of program instructions that performs a specific task, packaged as a unit. More common name for a subroutine is a procedure, a function, a method.

There is usually exactly one call stack associated with a thread. A call stack is composed of *stack frames*. Each stack frame corresponds to a call to a subroutine(method, function) which has not yet terminated with a return.

```
// An example of call stack using some mystical language,

func foo() int {
	return 1
}

func bar() int {
	return foo()
}

func main() {
	print bar()	
}
```

The stack will look like

```
top of the stack
+---------------+	--+
| locals of foo |	  |
| return addr 	|	  |- stack frame for a foo subroutine
| parameters	|	  |
+---------------+   --+
| locals of bar |
| return addr 	|
| parameters 	|
+---------------+
| locals of main|
| return addr 	|
| parameters 	|
+---------------+
```

Top of the stack is a currently executing routine. The stack frame usually includes at least these elements:

- Arguments or parameters values
- Return address back to the routine's caller
- Space for a local variables of the routine
