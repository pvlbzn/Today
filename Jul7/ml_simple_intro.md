## Neuro XOR
Without very much of an introduction, here is an example of the ^ exclusive or function which works like:

```
> 1 ^ 1
0
> 1 ^ 0
1
> 0 ^ 0
0
```

Mostly the same thing using 'neurons'

```
const b = require('brain.js);
const n = new b.NeuralNetwork();

n.train([{input: [0, 0], output: [0]},
         {input: [0, 1], output: [1]},
         {input: [1, 0], output: [1]},
         {input: [1, 1], output: [0]}]);

const xor = n.run([1, 0]);
> 0.9338693844621753
```

Run with `[1, 1]` will produce `0.08749120464462963`. Without knowing much about machine learning the idea can be seen. Here is 2 input neurons and 1 output. `brain` module by itself sets a required number of the *hidden neurons*.

Stuff from line 4 to 8 is a learning data. Data is already normalized by its nature.

## Handwritten numbers recognition
[MNIST](http://yann.lecun.com/exdb/mnist/) library will be used. 
