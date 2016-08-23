# Webpack
Webpack is a modern *bundler* for javascript. I find this picture is best to describe Webpack:

![Webpack](https://webpack.github.io/assets/what-is-webpack.png "webpack")

## General Approach
Four initial files: `index.html`, `entry.js`, `content.js` and `style.css`. To execute `webpack` use `webpack ./entry.js bundle.js`.

#### `index.html`

```
<body>
    <script type="text/javascript"
            src="bundle.js"
            charset="utf-8">
    </script>
</body>
```

#### `entry.js`

```
require("!style!css!./style.css");
document.write(require(./content.js));
```

#### `content.js`

```
module.exports = "It works from content.js file."
```

#### `style.css`
body {
    background: #313131;
}

## Loaders
`require("!style!css!./style.css");` can be changed to `require("./style.css");` using loaders:

```
webpack ./entry.js bundle.js --module-bind 'css=style!css'
```

## Config file
To start webpack only with `webpack` command a config file must be used, `webpack.config.js`:

```
module.exports = {
  entry: "./entry.js",
  output: {
    path: __dirname,
    filename: "bundle.js"
  },
  module: {
    loaders: [
      { test: /\.css$/, loader: "style!css" }
    ]
  }
};
```

Now the whole thing can be started with just `webpack`.

## Watch
Watch mode is kind of automatic compiler. When any file changed it automatically recompiles changed file:

```
webpack --progress --colors --watch
```
