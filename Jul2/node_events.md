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

See runnable code `./ee.js`

```
class Em extends EventEmitter {
    constructor() {
        super();
    }
    do() {
        console.log('1');
        this.emit('call');
        console.log('3');
    }
}

const ee = new Em();
// Attach callback to the 'call' event. When 'call' will happen
// 2 will be printed.
ee.on('call', () => {
    console.log('2');
})

ee.do();
```

It will produce 1, 2, 3. This is the synchronous code. `.on` just attached a callback to the event. Basicaly it means just call this function later when this event will occur.

`EventEmitter` often appears async because it is regularly **used to signal the completion of async ops**, but the `EventEmitter` API is synchronous.
