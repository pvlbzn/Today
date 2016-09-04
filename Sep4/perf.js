const functools = require('./funcTools');

const filter = functools.filter;
const map    = functools.map;
const reduce = functools.reduce;


function generateDataset() {
  const dataset = [];
  
  for (let i = 0; i < 1e6; i++)
    dataset.push(i);

  return dataset;
}


// Custom implementation
const ct1 = process.hrtime();
const cf = filter(generateDataset(), n => { return n % 3 === 0 });
const cm = map(cf, n => { return n / 15.7 });
const cr = reduce(cm, 0, (n1, n2) => { return n1 + n2 });
const ct2 = process.hrtime(ct1);
console.log(cr, ct2);

// Native implementation
const nt1 = process.hrtime();
const nf = generateDataset().filter(n => { return n % 3 === 0 });
const nm = nf.map(n => { return n / 15.7 });
const nr = nm.reduce((n1, n2) => { return n1 + n2 });
const nt2 = process.hrtime(nt1);
console.log(nr, nt2);

console.log(`time diff: ${nt2[1] - ct2[1]}`);
