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

const sync = () => {
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
    });
    return ee;
};

// s = sync();
// s.do();

/*
 * Next example
 */

var util = require('util');

/*
function MyThing() {  
  EventEmitter.call(this);

  doFirstThing();
  // Wont happen because MyThing must finish instantiating
  // before listening for any events. It can be fixed with
  // setImmediate.
  this.emit('thing1');
}
*/

function MyThing() {
    EventEmitter.call(this);

    doFirstThing();
    setImmediate(emitThing, this);
}

function emitThing(that) {
    that.emit('thing1');
}

function doFirstThing() {
    console.log('First');
}

util.inherits(MyThing, EventEmitter);

var mt = new MyThing();

mt.on('thing1', function onThing1() {  
  console.log('Yes!');
});