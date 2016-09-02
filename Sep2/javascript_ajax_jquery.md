# `jquery` AJAX
`jquery` basically is a DOM abstraction library. However it also abstracts browser APIs making work with them more easy and kind of stable for those who don't mess hard with frontend development. In this *TIL for TIL* `jquery` abstraction will be used.

## AJAX
AJAX is an async js and xml, so every call goes asynchronously.

```
const call = {
    type: GET,                          // HTTP verb
    url: '/api',                        // path
    data: {                             // Specify data that will be send to a server
        'key': 'value',
        'id': '1opjel1y7t632ue'  
    },
    contentType: application/json',     // MIME type
    success: msg => {
        // success callback
    },
    error: () => {
        // error callback
    }
}

jQuery.ajax(call);
```

`jquery` abstracts AJAX to AJAX itself `.ajax()` and some convinient methods `.get()`, `.getScript()`, `.getJSON()`, `.post()`, `.load()`.


To test and try them will be used the following wild mix of javascript in html which is in javascript itself code which is made for brevity, not readability or scalability

@{server.js} 

