function t() {
    const t1 = process.hrtime();
    return () => {
        return process.hrtime(t1);
    }
}

// Test function 1a
function f1(n) {
    function i1(n) {
        return [1, 2, 3].indexOf(n);
    }
    return i1(n);
}

// Test function 1b
function f2(n) {
    return i2(n);
}

function i2(n) {
    return [1, 2, 3].indexOf(n);
}
    
const stopA = t();
for (i = 0; i < 10e6; i++)
    f1(2);
const timerA = stopA();

const stopB = t();
for (i = 0; i < 10e6; i++)
    f2(2);
const timerB = stopB();

console.log("(hr): %ds %dms", timerA[0], timerA[1]/1000000);
console.log("(hr): %ds %dms", timerB[0], timerB[1]/1000000);


