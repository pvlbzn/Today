###Data Encapsulation

####Send/Receive

Packet **sending**:

- Packet is born
- Paket is wrapped (encapsulated) in a header (or rarely a footer) by the first protocol (TFTP for example)
- The whole thing encapsulated by the next protocol (IP)
- And again wrapped by the final protocol on the hardware layer (say, Ethernet)



When another computer receives the packet, the hardware strips the Ethernet header, the kernel strips the IP and UDP headers, the TFTP program strips the TFTP header, and it finally has the data.



####Layered Network Model ISO/OSI

Layers:

- Application
- Presentation
- Session
- Transport
- Network
- Data Link
- Physical

This is a full blown layers, but a layered model more consistent with Unix might be

- Application Layer (telnet, ftp, etc)
- Host-to-Host Transport Layer (TCP, UDP)
- Internet Layer (IP and routing)
- Network Access Layer (Ethernet, wifi, whatever)

However, all you have to do for **stream sockets** is `send()` the data out. All you have to do for **datagram sockets** is **encapsulate** the packet in the method of your choosing and `sendto()` it out.