'use strict'

function f1(a, b) {
	return a + b;
}

function f2(a, b) {
	return a + b;
}

function t() {
	let t = process.hrtime();
	return () => {
		return process.hrtime(t);
	}
}

const stop1 = t();
for (let i = 0; i < 1e8; i++) {
	f1(2, 2);
	f1('a', 'b');
}
const time1 = stop1();

const stop2 = t();
for (let i = 0; i < 1e8; i++) {
	f1('a', 'a');
	f1('h', 'j');
}
const time2 = stop2();

console.log("%ds %dms", time1[0], time1[1]/1e6);
console.log("%ds %dms", time2[0], time2[1]/1e6);
