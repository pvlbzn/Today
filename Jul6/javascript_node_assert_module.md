## Prelude
In order to understand nodejs I will go through every module from node API documentation. It is a well writen source with proper examples in es6, so it will be a good exercise to understand this platform.

## Assertion Testing
The `assert` module provides a set of assetion tests. It is intended for internal use, but also can be used in application code via `require('assert')`. `assert` is not a testing framework and not intended to be used as one.

*Stability: 3 - Locked*

*Nodejs API has 4 stability indices: 0 - Deprecated, 1 - Experemental, 2 - Stable, 3 - Locked.*

#### Examples

```
const assert = require('assert');

// assert (value[, message]), an alias of assert.ok()
assert(false, '\nfalse assertion');

// assert.deepEqual() and assert.deepStrictEqual()
// Difference between them is that strict equal checks
// primitives with === and checks prototypes.
const o1 = {
    val1: 15
}
const o2 = {
    val2: 10
}
assert.deepEqual(o1, o1);
assert.deepEqual(o1, o2);
> AssertionError: { val1: 15 } deepEqual { val2: 10 }

// assert.fail(actual, expected, message, operator)
assert.fail(5, 15, false, '>');
> AssertionError: 5 > 15
assert.fail(5, 15, '5 is smaller than 15', '>');
> AssertionError: 5 is smaller than 15

// assert.ifError(value)
assert.ifError(0);
// ok
assert.ifError(true);
// Throws true

// There are also notStrictEqual method.
assert.notEqual(1, 1);
> AssertionError: 1 != 1

```


