# HTTP
HTTP has no state, it's stateless. That means that every new request is entierly new, as well as response, they have no state.

> HTTP request contains all the information necessary for the server to satisfy the request.

Therefore *log in* is impossible through a pure http, because there is simply no state.

# Cookies
Cookies is a way to build a state on top of HTTP. Server sends some information and the browser stores it for some period of time. In this way an illusion of a state can be achieved.

However, due to sequrity reasons user have full control over cookies.

- User can delete or disallow cookies
- Cookies can be corrupted
- Cookies cab be used for attacks

Therefore better to prefer *sessions* over *cookies*.

There are two main approaches:

1. Store everything in cookies
2. Store only only a unique ID in the cookie and rest on the server

## Safety
To make cookies secure, a *cookie secret* is necessary. It is a string that is know to the server and used to encrypt secure cookies before they are sent to the client.

## Sessions
To implement sessions something has to be stored on the client. For example a cookie with unique id. However sessions arent limited to cookies, it is also possible to make use of HTML5 - *local storage*.
