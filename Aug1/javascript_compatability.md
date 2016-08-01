## Many Platforms
There are many platrofms which owns JS runtime. Mostly it is browsers. Not every browser support every new feature. But there are a two ways to run newest JS on the old platform.

### Polyfilling
A [polyfill](https://remysharp.com/2010/10/08/what-is-a-polyfill) is a piece of code that provides the technology that developers expect the browser to provide natively.

```
if (!Number.isNaN) {
    Number.isNaN = function isNaN(n) {
        // Only NaN is not equal to itself
        return n !== n;
    };
}
```

ES6 has `Number.isNaN` function, ES5 not. Therefore `if` checks is there is a function or not. If not - declare a new on on a `Number` object.

There is a community [ECMAScript Shims](https://github.com/es-shims/) which works on polyfills.


### Transpiling
Transforming + compiling.

Consider this ES6-syntax example:

```
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  getCoordinates() {
    return [x, y];
  }
}

class ColorPoint extends Point {
    constructor(x, y, color) {
        super(x, y);
        this.color = color;
    }
    get() {
      return [[this.x, this.y], this.color];
    }
}
```

Use it

```
let rp = new Point(15, 25);
let cp = new ColorPoint(35, 61, 'blue');

console.log(`x: ${rp.x} | y: ${rp.y}`);
console.log(`x: ${cp.x} | y: ${cp.y} | color: ${cp.color}`);

> x: 15 | y: 25
> x: 35 | y: 61 | color: blue
```

However it won't run on the old platform.

[Babel](https://babeljs.io) the solution:

```
'use strict';

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Point = function () {
  function Point(x, y) {
    _classCallCheck(this, Point);

    this.x = x;
    this.y = y;
  }

  Point.prototype.getCoordinates = function getCoordinates() {
    return [x, y];
  };

  return Point;
}();

var ColorPoint = function (_Point) {
  _inherits(ColorPoint, _Point);

  function ColorPoint(x, y, color) {
    _classCallCheck(this, ColorPoint);

    var _this = _possibleConstructorReturn(this, _Point.call(this, x, y));

    _this.color = color;
    return _this;
  }

  ColorPoint.prototype.get = function get() {
    return [[this.x, this.y], this.color];
  };

  return ColorPoint;
}(Point);

var rp = new Point(15, 25);
var cp = new ColorPoint(35, 61, 'blue');

console.log('x: ' + rp.x + ' | y: ' + rp.y);
console.log('x: ' + cp.x + ' | y: ' + cp.y + ' | color: ' + cp.color);
```

Technically these two snippents are identical, but for a human there is a big difference.

Even more, there is [traceur](https://github.com/google/traceur-compiler) compiler (compiler in a sence of compiling new syntax to the old one equivalent) which allows to use not only ES6 but ES7 as well.
