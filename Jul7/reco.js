const brain = require('brain.js'),
      mnist = require('mnist');

const net = new brain.NeuralNetwork();
const set = mnist.set(0, 1);
const tset = set.test;
net.fromJSON(require('./data/mnistTrain'));
const output = net.run(tset[0].input);

function softmax(output) {
    let maximum = output.reduce((p, c) => {
        return p > c ? p : c;
    });
    let nominator = output.map((e) => {
        return Math.exp(e - maximum);
    });
    let denominator = nominator.reduce((p, c) => {
        return p + c;
    });
    let softmax = nominator.map((e) => {
        return e / denominator;
    });

    let maxIndex = 0;
    softmax.reduce((p, c, i) => {
        if (p < c) {
            maxIndex = i;
            return c;
        } else {
            return p;
        }
    });
    let result = [];
    for (var i = 0; i < output.length; i++) {
        if (i == maxIndex) {
            result.push(1);
        } else {
            result.push(0);
        }
    }
    return result;
}

console.log(tset[0].output);
console.log(softmax(output));
