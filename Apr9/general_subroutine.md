###Subroutine

A subroutine is a sequence of program instructions that perform a specific task, packaged as a unit. In different PL, a subroutine may be called a procedure, a function, a routine, a method, or a subprogram.

The content of a subroutine is its body, which is the piece of program code that is executed when the subroutine is called or invoked.

**Call by value**
Argument is evaluated and copy of value is passed to subroutine. Usually default in mainstream languages.

**Call by reference**
Reference to argument, typically its address is passed. Selectable in C, C++ and some others.

**Call by result**
Parameter value is copied back to argument on return from the subroutine.

**Call by value-result**
Parameter value is copied back on entry to the subroutine and again on return.

**Call by name**
Like a macro - replace the parameters with the unevaluated argument expressions

**Call by constant value**
Like call by value except that the parameter is treated as a constant

---

Usually PL include specific constructs to:

- Delimit the part of the program body that makes up the subroutine
- Assign an identifier to the subroutine
- Specify the names and data types of its parameters and return values
- Provide a private naming scope for its temporary variables
- Identify variables outside the subroutine that are acessible within it
- Call the subroutine
- Provide values to its parameters
- Specify the return values from withtin its body
- Return to the calling program
- Dispose of the values returned by a call
- Handle any exceptional conditions encountered during the call
- Package subroutines into a module, library, object, class, etc

