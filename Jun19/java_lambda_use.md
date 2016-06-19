## Java Lambda in Use

Syntax is: `parameter -> expression body`.

```
class Lambdy {
    
    interface MathOp {
        int op(int a, int b);
    }

    interface Printer {
        void print(int n);
    }

    psvm {
        // Short syntax
        MathOp mul = (a, b) -> a * b;
        // Full syntax
        MathOp sub = (int a, int b) -> {return a - b;);

        Printer p = msg -> System.out.println(msg);

        p.print(add.op(5, 5));
    }

}
```

Will print 10.

So, basically lambda expression is a block of code that you can pass around and it can be execute later.

