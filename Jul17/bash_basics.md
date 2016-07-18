## Bourne Again Shell
Bash is the GNU project shell. It is 'better' version of `sh`. It is available on all modern UNIX-like systems. It is a superset of the Bourne shell. `bash` can substitute `sh`, but if `bash` ran as `sh` it behaves differently. There are lots of shells: `csh`. `zsh`, `ksh`, `dash`, `bash`, etc.

`bash` can be tought like OS interface is some way. A funny thing that terminal *emulator* is already running a `bash` or whatever else. Actually every shell will have its own scripting language, all of them are different in details.

### Why Emulator?

Because a computer terminal is an electronic hardware device that is used for entering data into and displaying data from a computer.

![Hardware Terminal](https://en.wikipedia.org/wiki/File:DEC_VT100_terminal.jpg "terminal")

Typical terminal works like this

```
+------------+    stdin
|  KEYBOARD  | -----------+
+------------+            |
                          v
                    +-----------+
                    |  PROGRAM  |
                    +-----------+
                          |  |
+------------+    stdout  |  |
|  DISPLAY   | <----------+  |
+------------+               |
        ^                    |
        |         stderr     |
        +--------------------+
```

### File Descriptor
The kernel gives for each program a separate process inside which program will be executed. The process has a hooks to the outside world - a file descriptor. FD is one of the core conceptions in UNIX. First three also have standard names.

**standard input** - file descriptor 0
**standard output** - file descriptor 1
**standard error** - file descriptor 2

File descriptors are **process specific**. Imagine all programs with one `stderr`. 

### `bash`
{@see ./bsh.bash}
