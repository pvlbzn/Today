## Document Object Model
DOM is an API for HTML and XML documents. DOM model is constructed as a tree of objects. HTML is parsed by the browser and turned into the DOM.

*Note: DOM has **nothing** in common with JS, but document named like it has. JS is a best conceptual fit from existing tags.*

![DOM](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/DOM-model.svg/428px-DOM-model.svg.png "DOM")

Actually, DOM, is a problem. And JavaScript usually blamed. They arent related. Different browsers have a different DOM implementation and it varies from the actual DOM standard..

Using DOM API programmers can create, build documents, navigate it, modify or edit its elements and their content.

#### Example
The DOM specifies method `getElementsByTagName`, which by the way can be accessed from a language different from JS since DOM is the API. This method expected to return a list of all the specified elements in the document.

```
const paragraphs = document.getElementsByTagName('p');
paragraphs[10];
// Content
```

For example `EventTarget.addEventListener()` method is a part of DOM API.

#### DOM Events
[Event Reference](https://developer.mozilla.org/en-US/docs/Web/Events) is a list of all DOM and not only DOM events in the browser.