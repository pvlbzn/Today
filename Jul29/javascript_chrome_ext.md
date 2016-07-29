## Chrome Extension
Chome's extensions are simple *injected* after DOM loaded JavaScript code with some manifest file and sequrity checks.

### Anatomy

#### Manifest
[`manifest.json`](https://developer.chrome.com/extensions/manifest) is a first thing that have to be done:

```
{
    // Required
    "manifest_version": 2,
    "name": "Extension name",
    "version": "0.1",

    // Recommended
    "default_locale": "en",
    "description": "Plain-text description",
    "icons": {
        ...
    }
}
```

#### Content Script
Content scripts are JavaScript files that run in the context of web pages. By using the standard DOM they can read details of the web pages the browser visits, or make changes to them.

They can:
- Find unlinked URLs in web pages and convert them into hyperlinks
- Increase the font size
- Find and process micoformat data in the DOM

They can not:
- Use `chrome.*` API, with the exception of:
    - `getUrl`, `inIncognotoContext`, `lastError`, `onRequest`, `sendRequest`
    - `i18n`
    - `connect`, `getManifest`, `getUrl`, `id`, `onConnect`, `onMessage`, `sendMessage`
    - `storage`
- Use variables or function defined by their extension
- Use variables or function defined by web pages or by other content script

However, *content scripts* can **indirectly** use the `chrome.*` APIs, get access to extension data, and request extension actions by exchanging *messages* with their parent extension.

```
// Add to manifest file content script
"content_scripts": [
    {
        "matches": [
            "<all_urls>"
        ],
        "js": ["support.js", "content.js"]
    }
]
```

#### Browser Actions
When an extension adds a little icon next to your address bar, that's a browser action. In addition to its icon, a browser action can also have a tooltip, a badge, and a popup.

```
// Manifest
"browser_action": {
    "default_icon": "icon.png"
}
```

#### Message Passing
Content script has access to the current page but its limited in the API. However a *background script* has access to every chrome API, but it **cant** access the current page. Message passing is the only way to interact between content script and background script.

```
"background": {
    "scripts": [
        "background.js"
    ]
}
```

```
// background.js

chrome.browserAction.onClicked.addListener((tab) => {
    // Send a message to the active tab
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        let activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id,
            {"message": "clicked_browser_action"});
    });
});
```

```
// content.js

chrome.runtime.onMessage.addListener((req, sender, resp) => {
    if (req.message === "clicked_browser_action") {
        // Do something
    }
    // Send message back to background
    chrome.runtime.sendMessage({"message": "open_new_tab", "url": "www.url.com"});
});
```

```
// background.js
chrome.runtime.onMessage.addListener((req, sender, resp) => {
    if (req.message === "open_new_tab") {
        chrome.tabs.create({"url": req.url});
    }
});
```

