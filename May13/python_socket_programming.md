#### Prelude
I already did some research of this topic, and sometimes it happends that authors of articles/books/tutorials took a copy of some chapters or another tutorials. For today I choose an article, which happen that I already did: an introduction from [this](https://github.com/pvlbzn/Today/blob/2dd52be40d27667679ed6379314d1f1cd5ec0f21/Apr6/unix_server_socket_client_socket.md) document, however [this](https://docs.python.org/3/howto/sockets.html) article is much more interesting and on topic.

<br>

#### Design Decisions
An important thing - server sockets and client sockets are identical beasts. Usually a client starts a conversation. But that is a design decision, it isn't a rule of sockets.

#### Use
There are two verbs: `send` and `recv`, or `read` and `write`. The later is the way Java presents its sockets. You have to `flush` on sockets. These are buffered, and you can write something and tne read for a reply. Without `flush` you'll wait for ever.

The major focus of `send` and `recv` is handling the network buffers. In general they return when the associated network buffers have been `send` or `recv`, and after that they tell you how many bytes they handled. *It is your responsibility to call them again until your message has been completely dealt with*.

A protocol like **http** uses a socket for only one transfer. This means tahat a client can detect the end of the reply by receiving 0 bytes.

Thus: messages must either be fixed length, or be delimited, or indicate how long they are, or end by shutting down the connection.

#### Binary Data
The major problem in binary data that not all machines uses a same bit order. Socket libraries have calls for converting bits (16 and 32) `ntohl`, `ntonl`, `ntohs`, `ntons`.

