/*
function t() {
    const t1 = process.hrtime();
    return () => {
        return process.hrtime(t1);
    }
}
*/

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
    
for (i = 0; i < 10e6; i++)
    f1(2);

for (i = 0; i < 10e6; i++)
    f2(2);

