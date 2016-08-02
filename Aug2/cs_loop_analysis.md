## Analyzing the Time Complexity

This nested loop example has **O(n^2)** time complexity.

```
for (int i = 0; i < n; i++) {
    // O(n)
    for (int j = 0; j < n; j++) {
        // O(n) * O(n)
    }
}
```

Inner loop will iterate `j` times for each of the `i` iterations of the outer loop. Which means that if both loops are dependednt on the problem size *n*, the statements in the inner loop will be executed **O(n^2)** times.

```
for (int i = 0; i < n; i++) {
    // O(n)
    for (int j = 0; j < n; j++) {
        // O(n) * O(n)
        for (int k = 0; k < n; k++) {
            // O(n) * O(n) * O(n)
        }
    }
}
```

This will be equal to **O(n^3)**.

Consider the following loop:
```
for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
        // ...
    }
}
```

Here outer loop is dependent on the problem size `n`, but the inner loop in dependent of the current value of the index varibale of the outer loop.

On the final iteration of the outer loop (i = n - 1), the inner loop will iterate n - 1 times. The total number of times the statement in the inner loop will be executed will be equal to the sum of the integers from 1 to n - 1:

`((n - 1) * n) / 2 = n^2 / 2 - n / 2 = O(n^2)` times.
