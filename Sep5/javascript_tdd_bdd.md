# Test Driven Development
*Red, Green, Refactor* is a mantra of TDD (I guess this is was populated by RoR developers). It is a conception like *make it work and perfect it later* using tests.

# Behavior Driven Development
It compunes TDD with ideas from domain driven design. BDD is guided by the expected behavior. BDD is driven by the natural language and usually is done in very english like style. While TDD is more like a paradig, BDD is more a process.

# `chai`
Chai is a BDD/TDD *assertion library*. It has several interfaces: *should*, *expect*, *assert*.

### `assert`
Assert is a standard testing interface.

```
const assert = require('chai').assert;

assert.typeOf('', 'string', 'empty string is a string');
assert.equal(1, 1, '1 equal 1')
```

Assertion [API](http://chaijs.com/api/assert/) is really big. Better to consult documentation each time you want to perform some thing in which you are not quite sure. Asseption API has methods such as `isArray` or `isNotArray`, `increases` of `doesNotIncrease` etc.

### `expect` and `should`
`expect` is the BDD style expression as well as `should`.

```
const should = require('chai').should();
const expect = require('chai').expect;

const x = 'hello';

expect(x).to.be.a('string');
expect(x).to.have.length(5);

x.should.be.a('string');
x.should.have.length(5);
```

`expect` interface provides a function as a starting point for chaining lang assertions. `should` interface extends `Object.prototype` to provide a single getter as the starting point of lang assertions.
