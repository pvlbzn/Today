/*

// ES5 version

var util = require('util');
var EventEmitter = require('events').EventEmitter;

function Emitter() {
    EventEmitter.call(this);
}

util.inherits(Emitter, EventEmitter);

Emitter.prototype.do = function() {
    console.log('1');
    this.emit('someEvent');
    console.log('3');
};

var ee = new Emitter();
ee.on('someEvent', function() {
    console.log('2');
});

ee.do();
*/

// ES6 version

const EventEmitter = require('events').EventEmitter;

class Em extends EventEmitter {
    constructor() {
        super();
    }
    do() {
        console.log('1');
        this.emit('someEvent');
        console.log('3');
    }
}

const ee = new Em();
ee.on('someEvent', () => {
    console.log('2');
})

ee.do();