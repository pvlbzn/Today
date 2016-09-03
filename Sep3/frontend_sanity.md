# Frontend and Software Developer Sanity
Unfortunately frontend things is unavoidable if you are doing things for web. But there are some tools which makes things much better.

## HTML
`html` is awful, however there is a way to abstract it away complitely. Instead of plain html some html engine can be used. There are many of them, but `jade` (new name is pug) is stands out because it abstracts `html` complitely and it is great.

### `pug`

```
const pug = require('pug');

const teamplate = pug.compile('h1#id_name #{text}');
teamplate({
    text: 'custom header text'
});
```

It compiles to: `'<h1 id="id_name">custom header text</h1>'`.

`pug` supports everything what is expected from a html template language. Variables, cases, blocks and even code:

```
-
    m = {'link1': 'some.url', 'link2': 'another.url'}
each val, key in m
    a(href=val) #{key}
`;
```

Compiles down to `<a href="some.url">link1</a><a href="another.url">link2</a>`. *Why do people even use html?*.
