# CSS
CSS is fine but it lack every feature you can imagine. Preprocessors can help with writing more pleasant and maintainable style sheet.

## SASS
SASS is a CSS preprocessor. It lets programmer to write `.sccs` code which later can be transplited into old `.css`. This can be achieved in many ways, with bundlers or task runners. They run `sass` transcompliter against `.scss` file in order to produce `.css`.

There is two flavors of SASS: `.sass` and `.scss`. Difference is in syntax.

```
// .sass
body
    color: #333

// .scss
body {
    color: #333;
}
```

### Variables
SASS uses `$` symbol to define a variable

```
$font-color: #292929;

h1 {
    color: $font-color;
}
```

### Nesting
SASS alows nesting.

```
nav {
    ul {
        margin: 0;
        paddign: 0;
    }

    li {
        display: inline-block;
    }

    a {
        display: block;
        padding: 16px 16px;
    }
}
```

### Modules

#### Partials
A partials is simply a SASS file named with a leading underscore, like `_name.scss`. Partials are used with the `@import` derective.

#### Import
For exapmle there is a two files: `_partial.scss` and `style.scss`

```
// _partial.scss
html,
body,
ul,
ol {
    margin: 0;
    padding: 0;
}

// style.scss
@import 'partial';

body {
    font: 100% Helvetica;
    background-color: #AEAEAE;
}
```

#### Mixin
A mixin lets to make groups of CSS declarations that will be reused.

```
@mixin border-radius($radius) {
    -webkit-border-radius:  $radius;
    -moz-border-radius:     $radius;
    -ms-border-radius:      $radius;
    border-radius:          $radius;
}

.box {
    @include border-radius(10px);
}
```

### Inheritance

```
.msg {
    border: 1px solid #CCCCCC;
    padding: 10px;
}

.sucess {
    @extend .msg;
    border-color: green;
}

.error {
    @extend .msg
    border-color: red;
}

.warning {
    @extend .msg;
    border-color: yellow;
}
```

### Operators
SASS supports `+`, `-`, `*`, `/`, `%` operators.
