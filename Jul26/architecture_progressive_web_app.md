## Progressive Web App
This is very interesting idea to ship first-class, apps which are capable to work offline to *every* platform. There is such a thing like electron, but.

PWA is https by default and low on traffic. No need to explicitly download. And, its still a web.


### App Shell
The apps shell is the minimal HTML, CSS, JS which will load immediately after be cached. Like a native apps. App shell architecture separates the core app infrastructure and UI from the data. ALl of the UI and infrastructure is cached locally using a *service worker*. Therefore only required data will be loaded (fastest load time is no content to load).

App shell looks like following markup:

```
<header class="header">
    <h1 class="header__title">Weap</h1>
    <button id="bRefresh" class="headerButton"></button>
    <button id="bAdd" class="headerButton"></button>
</header>

<main class="main" hidden>
<!-- forecast-card.html -->
</main>

<div class="dialog-container">
<!-- add-new-city-dialog.html -->
</div>

<div class="loader">
    <svg viewBox="0 0 32 32" width="32" height="32">
        <circle id="spinner" cx="16" cy="16" r="14" fill="none"></circle>
    </svg>
</div>
```
