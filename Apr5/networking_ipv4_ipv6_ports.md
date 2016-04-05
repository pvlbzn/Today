### IP Adresses, `structs`

#### IPv4, IPv6

The Internet Protocol Version N, IPvN. __IPv4__ had addresses made up of four bytes, like 0-255.0-255.0-255.0-255. Later, Vint Cerf warned everyone that we were about ot run out of IPv4 addresses.

**IPv4** is **32** bits(2^32), **IPv6** is **128** (2^128) bits.

-

**IPv6** addresses have a hexadecimal representation, with two-byte chunk separated by a colon:

`2001:0db8:c9d2:0012:0000:0000:0000:0051`

And here is an equavalent:

`2001:db8:c9d2:12::51`

Loopback address

`0000:0000:0000:0000:0000:0000:0000:0001`

`::1`

You can express a IPv4 address as an IPv6 address

```
// IPv4
192.0.2.33
// IPv6
::ffff:192.0.2.33
```

-


#### Port Numbers
Besides an IP address (used by the IP layer), there is another address that is used by TCP(stream sockets) and by UDP(datagram sockets) - port number. Is is a 16-bit number that is like the local address for the connection.

Analogy: IP address as the street of a building, a port number is a particular room in the building.
To see port numbers type the following:

`vim /etc/services`

It is a file which contains all port numbers of different applications.

```
#                          Bill Davidson <billd at equalizer.cray.com>
https           443/udp     # http protocol over TLS/SSL
https           443/tcp     # http protocol over TLS/SSL
```

Ports under 1024 are considered special, and usually require special OS privileges to use.


