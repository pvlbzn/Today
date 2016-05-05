###Pipeline

A pipeline consist of a chain of processing elements, aranged so that the output of each element is the input of the next one. So, `stdout` feeds directly next `stdin`.

The standard shell syntax for pipelines:

```
command1 | command2 | command3
```

Each `|` tells the shell to connect the `stdout` of the left program to the `stdin` of the right programm bt an interprocess communication - anonymous pipe, which is implemented in OS.
