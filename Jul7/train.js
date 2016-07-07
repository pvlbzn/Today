const brain = require('brain.js');
const net = new brain.NeuralNetwork();
const fs = require('fs');
const mnist = require('mnist');
// Get a 1000 elements of a learning data.
const set = mnist.set(1000, 0);
const tset = set.training;


net.train(tset, {
    errorThresh: 0.005,
    iterations: 20000,
    log: true,
    logPeriod: 1,
    learningRate: 0.3
});

let wstream = fs.createWriteStream('./data/mnistTrain.json');
wstream.write(JSON.stringify(net.toJSON(), null, 2));
wstream.end();

console.log('done');

