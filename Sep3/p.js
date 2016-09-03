const pug = require('pug');

const template1 = `
- for (var x = 0; x < 3; x++)
  li item
`;

const template2 = `
-
    m = {'link1': 'some.url', 'link2': 'another.url'}
each val, key in m
    a(href=val) #{key}
`;

const template3 = `
//- Invisible comment
// Visible comment

//- buffered code
p= '<escaped>'

//- unbuffered
p!= '<unescaped>'
`;


const teamplates = [template1, template2, template3];

const cFn = teamplates.map(pug.compile);

let html = '';
for (let f in cFn) {
    html += cFn[f]();
}

console.log(html);

/*
 * This code produces following html
 * <li>item</li>
 * <li>item</li>
 * <li>item</li>
 * <a href="some.url">link1</a>
 * <a href="another.url">link2</a>
 * <!-- Visible comment-->
 * <p>&lt;escaped&gt;</p>
 * <p><unescaped></p>
 */
