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

### Explanation in Pure JS
View element:

```
<span   id="counter">0</span>
<input  id="color"></input>
<button id="inc"></button>
```

Classical JS approach:

```
$('#color').on('keyup', () => {
    $('#counter').css('color', this.value);
})

$('#inc').on('click' () => {
    const old = $('#counter').html();
    const new = 1 + Number(old);
})
```

React'ish approach:

```
let state = {
    color: '',
    value: 0
};

function upd() {
    $('#counter').css('color', state.color);
    $('#counter').html(state.value);
}

$('#color').on('keyup', () => {
    state.color = this.value;
    upd();
})

$('#inc').on('click', () => {
    state.value++;
    upd();
})
```

The difference is that classical approach interacts with element directly, while (I believe React approach should be called as Flux approach) Flux approach interacting with elements through its state. It is perfectly makes sense in large apps.


#### Server Rendering
React can be rendered on the server-side and this is actually a good idea in the world of mobile things. Less rendering leads to less CPU cycles, less memory, longer battery life. Battery life is actually important, since not only mobile devices are battery driven, but also laptops, electrocars, and everything else in the future.

#### Beeing V
React is a V in MVC therefore:

- No event system
- No ajax
- No data layer
- No Promises
- No framework

#### Illustration
*I'm not sure about is this image technically correct or not*

[!img](http://mateoclarke.com/public/images/jquery-style-vs-react-style.png "illustration")

