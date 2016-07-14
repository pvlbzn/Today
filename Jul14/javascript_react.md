## React
React is a frontend library which is V in MVC. Rect frontend is made out of 'components'.


HTML view:

```
<header>
    <div class="name">
        Log In
    </div>
</header>
```

JavaScript controller:

```
$.post('/login', credentials, (u) => {
    // DOM manipulations
    $('header .name').text(u.name);
});
```

React alternative:

```
render: function() {
    return <header>
           { this.state.name ? this.state.name : <span>Log In</span> }
           </header>;
}
```

Benefit: if you know the state, you know the render output. Classical approach is to manipulate DOM from JS like controller(js) > view(html) > controller(js) > bad times. In React all functionality tyied directly into markup and packaged into component.

#### Server Rendering
React can be rendered on the server-side and this is actually a good idea in the world of mobile things. Less rendering leads to less CPU cycles, less memory, longer battery life. Battery life is actually important, since not only mobile devices are battery driven, but also laptops, electrocars, and everything else in the future.

