### Clang: Linked Lists
Based on [this](http://cslibrary.stanford.edu/103/LinkedListBasics.pdf) Stanfod paper by Nick Parlante.

To read:

- [Linked Lists Problems](http://cslibrary.stanford.edu/105/LinkedListProblems.pdf)
- [Binary Trees](http://cslibrary.stanford.edu/110/BinaryTrees.pdf)
- [Tree List Recursion](http://cslibrary.stanford.edu/109/TreeListRecursion.pdf)
- Refreshers
	- [Essential C](http://cslibrary.stanford.edu/101/EssentialC.pdf)
	- [Pointers and Memory](http://cslibrary.stanford.edu/102/PointersAndMemory.pdf)


-

###Refrechers

####Arrays

```
int scores[100];

scores[0] = 1;
```

Dissadvantages:

* Size is fixed
* Allocate arrays which "large enough".
	1. Empty space will be just wasted.
	2. If code needs to process more than "large enough" everything breaks.
* Inserting new elements at the front is potentially expensive.


####Pointers

**Pointer/Pointee**: Pointer stores a reference to another variable, known as its "pointee".

**Dereference**: Operation on a pointer accesses its "pointee".

**Bad Pointer**: Pointer which doesn't have an assigned a pointee is "bad" and shouldnt be dereferenced. It may **randomly corrupt the memory**. In C all pointers start out with bad values.

**Pointer assignment**: Assignment operation between two pointers, makes two pointers point to the same pointee.

**`malloc()`**: System function which allocates a block of memory in the heap and returns a pointer to the new block. The prototype for `malloc()` and other heap functions are in `stdlib.h`.

**`free()`**: Call `free()` on a block of heap memory to indicate to the system that you are done with it.


-


###Linked List
An array allocates memory for all its elementa lumped together as ob block of memory. Linked list allocates space for each element separately in its own block of memory called a **linked list element** or **node**. The list gets its overall structure by using pointers to connect all its nodes together like the links in a chain.

Each node contains two fields: a *data* field to store whatever element type the list holds for its client, and a *next* field which is a pointer used to link one node to the next node.

####Linked List Types
**Node**: The type for the nodes which will make up the body of the list. Each node contains a single client data element and a pointer to the next node in the list.

```
struct node {
	int				data;
	struct node*	next;
};
```

**Node Pointer**: The type for pointers to nodes.



