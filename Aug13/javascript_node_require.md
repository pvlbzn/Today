## `require(module)`

From nodejs's source:

```
// Nodejs source: https://github.com/nodejs/node/blob/master/lib/module.js
// Module constructor

function Module(id, parent) {
  this.id = id;
  this.exports = {};
  this.parent = parent;
  if (parent && parent.children) {
    parent.children.push(this);
  }

  this.filename = null;
  this.loaded = false;
  this.children = [];
}
```

It has two functions: foundation for all node's modules and handling node's module loading mechanism. Function `require` is an abstraction over `Module.require` which is a wrapper around `Module._load`.

```
// Nodejs source: https://github.com/nodejs/node/blob/master/lib/module.js
// require function

Module.prototype.require = function(path) {
  assert(path, 'missing path');
  assert(typeof path === 'string', 'path must be a string');
  return Module._load(path, this, /* isMain */ false);
};
```

After assertions `Module.require` function calls `Module._load`

```
// Nodejs source: https://github.com/nodejs/node/blob/master/lib/module.js
// _load function

// Check the cache for the requested file.
// 1. If a module already exists in the cache: return its exports object.
// 2. If the module is native: call `NativeModule.require()` with the
//    filename and return the result.
// 3. Otherwise, create a new module for the file and save it to the cache.
//    Then have it load  the file contents before returning its exports
//    object.
Module._load = function(request, parent, isMain) {
  if (parent) {
    debug('Module._load REQUEST %s parent: %s', request, parent.id);
  }

  var filename = Module._resolveFilename(request, parent, isMain);

  var cachedModule = Module._cache[filename];
  if (cachedModule) {
    return cachedModule.exports;
  }

  if (NativeModule.nonInternalExists(filename)) {
    debug('load native module %s', request);
    return NativeModule.require(filename);
  }

  var module = new Module(filename, parent);

  if (isMain) {
    process.mainModule = module;
    module.id = '.';
  }

  Module._cache[filename] = module;

  tryModuleLoad(module, filename);

  return module.exports;
};
```

`Module._load` is in charge of loading new modules and managing the module cache. If a module doesn't exists in the cache and is not a `NativeModule`, `Module._load` will create a new base module for it. `Module._cache` is a simple dictionary. `module.exports` return a `module` property of an object `Module`. *This is what `require` will return*.
