# Design Choice
Google's "Material Design" is good not because it is good by itself, but because user knows it. User know where to find settings, where to look for a button, and what does this splash screen means. This is also true for a software engineering world. Better to use standard designs solutions instead of customs, especially for an API.

## JSONAPI
There is an initialive called [JSONAPI](http://jsonapi.org/) which tries to help with JSON API design choices. It is just a conventions, nothing more. However it helps to focus on building an application, not on API.

JSON API requires use of the JSON API media type `application/vnd.api+json`.

Documentation highlights every point with the following keywords: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL.

### Basics
Clients MUST send all JSONAPI data with header `Content-Type: application/vnd.api+json`. Client MUST specify the media type. Clients MUST ignore any parameters for the `application/vnd.api+json`.

Servers MUST send all data in response with the header `Content-Type: application/vnd.api+json`. Server MUST respond with 415 status code if a req specifies the `Content-Type: application/vnd.api+json` with any media type parameters. Servers MUST repond with a 406 if a req `Accept` header contains media type.

A document MUST contain at least one of the:
- `data`
- `errors`
- `meta`

```
{
    "data": {
        "type": "articles",
        "id": "1",
        "attributes": {

        },
        "relationship": {

        }
    }
}
```

### Conslusion
The documentation is quite comprehensive and perhaps too overwelming because of the amout of conditions (like musts). However it MUST be considered for a large-scale project.
