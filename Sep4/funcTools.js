/**
 * Custom implementation of a filtering function. Done
 * for an educational purpose.
 */
function filter(data, condition) {
  const res = [];

  for (let item in data) {
    if (condition(data[item]))
      res.push(data[item]);
  }

  return res;
}

/**
 * Custom implementation of a map function. Done
 * for an educational purpose.
 */
function map(data, fn) {
  const res = [];

  for (let item in data)
    res.push(fn(data[item]));

  return res;
}

/**
 * Custom implementation of a reduce function. Done
 * for an educational purpose.
 */
function reduce(data, typeResolution, fn) {
  let red = typeResolution;

  for (let item in data)
    red = fn(red, data[item]);

  return red;
}



// Dataset
const x = [1, 2, 3, 4, 5];

// Even filter example
console.log(filter(x, n => { return n % 2 === 0; }));

// Add 25% example
console.log(map(x, n => { return n + ((n / 100) * 25) }));

// Sum all data
console.log(reduce(x, 0, (n1, n2) => { return n1 + n2 }));
