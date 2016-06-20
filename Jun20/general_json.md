## ECMA-404
JSON: JavaScript Object Notation. It is a common object serialization format in the web. It is a kind of less verbose and more readable XML. JSON is a language-independent despite its "JavaScript" in the name. It has a `application/json` MIME type signature.

#### Data Types

- Number
- String
- Boolean
- Array
- Object
- null

JSON is a value-pair based format. Whitespace allowed and ignored everywhere outside `""`. Objects are delimeted using `{}`, arrays `[]`. JSON has no comments. Object is unordered.

#### Syntax

```
{
    "menu": {
        "header": "SVG Viewer",
        "items": [
            {"id": "Open"},
            {"id": "ZoomIn", "label": "Zoom In"},
            null,
        ]
    }
}
```

```
{
    "type": "object",
    "properties": {
        "street_address": {"type": "string"},
        "city": {"type": "string"}
    },
    "required": ["street_address", "city"]
}
```
