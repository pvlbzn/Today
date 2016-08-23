## Modules
Modules helps to reduce complexity and improve maintainability. Frontend solves this task using some libraries such as `RequireJS`, `Browserify`, `Webpack` nowadays. `CommonJS` was an inspiration for Rayan Dahl and that is why node has `require(module)` syntax.

Main problem is that browsers doesn't understand modules yet, so some tools should be used.

## Task Runners
Grunt and Gulp are task runners. They kind of prepare runtime.

## Bundlers
Webpack and Browserify are package bundlers. They are designed to run through all of a package dependencies and concatenate them into one file.

## Transcompiler
Not all the browsers support ES6+, but ES6 is way better than ES5. There is a way to write even ES2017 and successfully run it in all the browsers. There is a tool for kind of compiling modern ES to well-supported ES version.

BabelJS will turn this code

```
[1, 2, 3].map(n => n * 2);
```

Into

```
[1, 2, 3].map(function(n) {
    return n * 2;
});
```

And this is a big deal. There is no point in waiting for companies like Google or Mozilla for implement a new feature in their VM and most importanly there is no point for waiting users until they will update their browsers/computers.
