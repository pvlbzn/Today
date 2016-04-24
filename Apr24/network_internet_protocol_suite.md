###Internet Protocol Suite

- Application layer
- Transport layer
- Internet layer
- Link layer

Most famous protocols are *http* via *TCP/IP*.

<br>

####Layers
[RFC1122](https://tools.ietf.org/html/rfc1122) emhasizes architectural princeples over layering. RFC1122 states *four layers* in IPS. However various networking models states in between 3-7 layers. Mostly all systems agreed in 4 layers: Application; Transport; Internet; Link, with some addition of 5th layer - Physical.

All these layers are about an *encapsulation*. Each next protocol *encapsulates* previous one. *Encapsulation* is used to provide abstraction of protocols.

```

1									|	DATA	|
	
2						|	UDP		|	UDP		|
						|	header	|	data	|

3			|	IP		|	IP					|
			|	header	|	data				|
			
4|	Frame	|	Frame							| Frame  |
 |	header	|	data							| footer |

```

This cool ascii art shows encapsulation layers.
1. Application layer
2. Transport layer
3. Internet layer
4. Link layer

[This](http://www.exa.unicen.edu.ar/catedras/comdat1/material/TP1-Ejercicio5-ingles.pdf) paper explains everything quite well.
