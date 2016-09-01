# Scripts
`npm` is capable to run some scripts on project. There is two ways to do it

1. `man npm-scripts`
2. `man npm-run-script`

*`npm` has a documentation `help` alias to `man` pages, e.g. `npm help scripts` or `npm help run-script`*

## `npm-scripts`
`npm` support the "scripts" property of the package.json. One functionality may has pre, present, post scripts.

- Publish: run on publish
    - `prepublish`
    - `publish`
    - `postpublish`
- Install: run on install
    - `preinstall`
    - `install`
    - `postinstall`
- Uninstall: run on uninstall
    - `preuninstall`
    - `uninstall`
    - `postuninstall`
- Version: run on bump
    - `preversion`
    - `version`
    - `postversion`
- Test: run by the `npm test`
    - `pretest`
    - `test`
    - `posttest`
- Start: run by the `npm start`
    - `prestart`
    - `start`
    - `poststart`
- Stop: run by the `npm stop`
    - `prestop`
    - `stop`
    - `poststop`
- Restart: run by the `npm restart`
    - `prerestart`
    - `restart`
    - `postrestart`

`npm [test/start/stop/restart]` is an alias for a `npm run-script [test/start/stop/restart]` command.


## `npm-run-script`
Run arbitrary package script. Custom scripts also have a `pre` and a `post` options.

## Example
`package.json`

```
{
  "name": "npm-func-test",
  "version": "0.0.1",
  "main": "noscript.js",
  "scripts": {
    "prestart": "echo prestart",
    "start": "echo start",
    "poststart": "echo poststart",

    "precustom-script": "echo precustom-script",
    "custom-script": "echo custom-script"
  },
  "author": "pvlbzn",
  "license": "UNLICENSED"
}
```

```
$ npm run-script start
> echo prestart

prestart

> echo start

start

> echo poststart

poststart

$
$
$ npm run-script custom-script
> echo precustom-script

precustom-script

> echo custom-script

custom-script
```
