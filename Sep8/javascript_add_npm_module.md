# New Package in the Node Package Manager
First of all credidentials must be set.

```
npm set init.author.name "name"
npm set init.author.email "mail"
npm set init.author.url "url"

npm adduser
```

or use `npm login` in case if you are already registered. `npm config ls` will help to see what user is currently set.

## Naming
Naming is always hard, especially with a density of npm repository. As documentation suggests:

- Name must be < 215 chars long
- No uppercase
- Name can't contain any non-url-safe chars

And a common sense like no *js* in the name, because it is hard to push Python on npm, etc.

Name can be checked using `npm view [name]`

```
npm ERR! 404 Registry returned 404 for GET on https://registry.npmjs.org/some_non-claimed-name
npm ERR! 404
npm ERR! 404  'some_non-claimed-name' is not in the npm registry.
```

If 404 on choosed name that means that name can be used.

## package.json
Here is a full [documentation](https://docs.npmjs.com/files/package.json) on `package.json` file, it is comprehensive.

## Version Control System
Create a new repository and add its address to the `package.json` file:

```
"repository": {
    "type": "git",
    "url": "https://github.com/pvlbzn/cycle-status.git"
},
```

## `push` & `publish`

```
$ git push origin master
$ npm publish
```

Done.
