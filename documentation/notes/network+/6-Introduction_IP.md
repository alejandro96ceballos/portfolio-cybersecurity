#IP introduction

- Data to move


- Infrastructure used to move it (cables, DSL, ethernet...)
- Transpor vehicle (IP)
- Containers holding chunks of data (TCP/UDP packets)
- Application data inside those packets



The structure of IPs is Ethernet Header - IP - TCP/UDP - TCP payload - Ethernet Trailer

## TCP/UDP

Layer 4
 TCP is connection oriented with a formal process to start and end connections.
 Makes the protocol reliable. Each data is acknowledged by the destination.
 Can manage unordered messages
 Connection and end of connection is done by a TCP handshake.
 The reciever can control the speed of transmission
 
 UDP is connectionless, no formal start or end of connection
 Makes the protocol fast but not as reliable. Can't recover from errors or reordering data
 Sender controls the speed of transmission
 
## IP

After the packets are prepared, IP is the vehicle to move them from one device to another. Each device has an IP as it's address
Each IP has different ports for different purposes. Each packet determines the destination port alongside the destination IP.

### IPv4

Sockets

Server has an IP address, determines a protocol and a port to forward the information
Client has an IP address and determines a protocol and a port to recieve the information

Ports 0-1023 have standard use. The rest are ephemeral
Ports 1024-65535 are ephemeral ports, normally for client usage.

Not a rule, just a standard
Not security, just communication standards.

If port standard is changed on servers the clients will not know how to communicate with it.


