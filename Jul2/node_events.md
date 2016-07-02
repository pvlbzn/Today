## Event Driven Programming
Much of node core API is build around event-driven architecture in which certain kinds of objects periodically *emit* named events that cause Function objects to be called. All obhects that *emit* events are instances of the [EventEmitter](https://github.com/nodejs/node/blob/master/lib/events.js) class.

Event driven programming is application flow control that is determined by events or changes in state.

```
const EventEmitter = require('events').EventEmitter;


let ee = new EventEmitter();
ee.on('test', function () {
    console.log('test event has occured');
});
 
ee.emit('test');

// Will print
> test event has occured
```

`EventEmitter` API is entirely synchronous

```
const EventEmitter = require('events').EventEmitter;

// Different 
function Emitter() {
    EventEmitter.call(this);
}

util.inherits(Emitter, EventEmitter);

Emitter.prototype.do = function do() {
    console.log('1');
    emitter.emit('someEvent');
    console.log('3');
};

var ee = new Emitter();
ee.on('someEvent', function() {
    console.log('2');
});

ee.do();
```

A small deviation on `util` module. [`util`](https://nodejs.org/docs/latest/api/util.html) module is designed to support the needs of node own internal API. In code above used function `util.inherits(constructor, superConstructor)`, note that this function is **discouraged**, instead `class` and `extends` must be used. This function will set the prototype of `constructor` to a new object created from `superConstructor`.