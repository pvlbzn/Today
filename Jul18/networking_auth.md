## Basic Access Authentication
BAA in the context of a HTTP transaction is a method for an HTTP uaser agent to provide a user name and password when making a request.

HTTP Basic Auth uses standard fields in the HTTP header. Its mechanism provides no confidentiality protection for the transmitted credentials. They are encoded, but not encrypted or hashed.

HTTP BA is non-secure unless used in conjunction with SSL.

## Digest Access Authentication
Is one of the agreed-ipon methods a web server can use to negotiate credentials with a user's web browser. It applies a hash function to the username and password before sending them over the network.

DA is an application of MD5, crypto hashing with usage of nonce values.

#### Nonce
In cryptography, a nonce is an arbitrary number that may only be used once. It is a pseudo-random number issued in an auth protocol to ensure that old communication can't be reused like replay attacks.

```
+--------+                       +--------+
| CLIENT |                       | SERVER |
+--------+                       +--------+
    |             getNonce()          |
    |------------------------------->|||
    |                                |||
    |             nonce              |||
    |<-------------------------------|||
    |                                 |
    |  login(uname, cnonce, hash(     |
    |    nonce + cnonce + password))  |
    |------------------------------->|||
    |                                |||
    |             token              |||
    |<-------------------------------|||
    |                                 |
    |                                 |
    |                                 |
```

