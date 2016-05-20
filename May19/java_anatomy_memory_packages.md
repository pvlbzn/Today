### To Understand The Java Code You Have To Think Like The Java Code
To think like the Java code, you have to understand how it works, how it behaves, what it is.

### Memory
Java runs as an OS level process, with the restrictions that the OS imposes. When program started JVM gets some memory from OS, and this memory space is a heap. Whenever object created its allocates memory from the heap.

Different JVM realizations uses diffrent GC collection algorithms.

There are two settings, `-Xms` - the initial heap size; `-Xmx` - the maximum heap size.

Working set could be considered as total memory for a live objects on heap.

```
+------------------------+
|	 Virtual Memory		 |
|						 |
|						 |
|						 |
|						 |
|						 |
|	+----------------+   |
|	|	    JVM		 |   |
|	|----------------+   |
|	|	  Garbadge   |	 |
|	|   Working Set  |	 |
|   +----------------+   |
|						 |
+------------------------+
```

TODO: Research different GC algorithms.

### Packages
Folder where Java stuff is stored on machine exists `src` folder, where all java packages are stored. `import java.io.BufferedReader` statement is actually a real path. While class names are bloated as hell, they still readable and understandable.

IDE really helps while writing, however it makes more harm while learning. It makes obvious things cryptic and overcomplicated.