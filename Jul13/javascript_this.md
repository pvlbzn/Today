## This
`this` is confusing, especially in the callbacks or *advanced* cases. `this ` is a special identifier keyword that automatically defined in the scope of every function.

*The source of an information is [you-dont-know-js](https://github.com/getify/You-Dont-Know-JS/blob/master/this%20&%20object%20prototypes/ch1.md).*

```
function id() {
    return this.name.toUpperCase();
}

function speak() {
    let greeting = `Hello, I'm ${id.call(this)}`;
    console.log(greeting);
}

var p1 = {
    name: "Steve"
};

var p2 = {
    name: "Kate"
};

/*
 * .call method calls a function with a given this value
 * and arguments provided individually.
 * func.call(thisArg[, arg1[, arg2[, ...]]])
*/
speak.call(p1);
> Hello, I'm STEVE
speak.call(p2);
> Hello, I'm KATE
```

#### What is `this`
It is kind of runtime based pointer to the context (lexical?). `this` based on runtime.
