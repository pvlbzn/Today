## Library
jQuery is an unavoidable library in the world of JavaScript. The main point of it is a cross-platform and simplifying things. It was very cool 9 years ago, when browsers API and DOM implementations were different and for each operation some workaround were needed. Nowadays jQuery used because of historial reasons since most native things works just well. 

If you need a 1 or 2 functions from jQuery - just write them and your code will be less for 10,000+ less lines of code. However, keep in mind that jQuery is a most notable front-end library and as a consicuence it is very reliable and robust.


## $
`$` just a valid name like 'jQuery' for a function. 

```
$(document).ready(() => { console.log('ready'); });

// An equivalent to
$(() => { console.log('ready'); });
```

An example:

```
// jQuery
$.ajax('service/uname', { data : { id: '5' } })
    .then((name) => { console.log('Name: ${name}'); },
          (data, status) => { console.log('Fail with status ${status}); });

// Native equivalent
const xhr = new XMLHttpRequest();
xhr.open('GET', encodeURI('service/name?id=5'));
xhr.onload = () => {
    if (xhr.status === 200)
        console.log('Name: ${xhr.responseText});
    else
        console.log('Fail with status ${xhr.status});
};
xhr.send();

// Self written variant
function get(url) {
    return new Promise((res, rej) => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onload = () => {
            if (this.status == 200) {
                res(this.response);
            } else {
                const err = new Error(this.statusText);
                err.code = this.status;
                rej(err);
            }
        };
        xhr.onerror = () => {
            rej(new Error("network error"));
        };
    });
}
```

There is a good blog on topic [You Don't Need jQuery](http://blog.garstasio.com/you-dont-need-jquery/).
