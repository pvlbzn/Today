/**
 * This is an example of a possible use of the EventEmitter.
 */

const EventEmitter = require('events').EventEmitter;
const util = require('util');

const showSync = true;

function Dealer() {
    this.open = false;
    this.units = 1;
    this.deal = () => {
        if (showSync) console.log('# 1 deal');
        this.units--;
        if (showSync) console.log('# 2 deal');
        this.emit('deal');
        if (!this.units) this.close();
        if (showSync) console.log('# 3 deal\n');
        this.callToBoss();
    };
    this.open = () => {
        if (showSync) console.log('# 1 open');
        this.open = true;
        if (showSync) console.log('# 2 open');
        this.emit('open');
        if (showSync) console.log('# 3 open\n');
        this.callToBoss();
    };
    this.close = () => {
        if (showSync) console.log('# 1 close');
        this.open = false;
        if (showSync) console.log('# 2 close');
        this.emit('close');
        if (showSync) console.log('# 3 close\n');
        this.callToBoss();
    };
    this.callToBoss = () => {
        // When event is emitted but no listener is attached
        // event lost.
        this.emit('call');
    };
};

util.inherits(Dealer, EventEmitter);

let d = new Dealer();
d.on('close', () => {
    console.log('Dealer is done for today.');
});
d.on('open', () => {
    console.log('Dealer is ready to work.');
});
d.on('deal', () => {
    console.log('Sucessful deal. Units left: ' + d.units);
});

d.open();
d.deal();

console.log('Done.');
