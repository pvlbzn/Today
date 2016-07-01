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
    EventEmitter
}
```

morning: https://nodesource.com/blog/understanding-the-nodejs-event-loop/
         https://nodejs.org/docs/latest/api/util.html#util_util_inherits_constructor_superconstructor