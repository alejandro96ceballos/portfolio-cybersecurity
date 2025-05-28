# LAN

## Topology

### Star

Each device individually connected via a central device suck a switch or hub.

- Advantages and disadvantages

More escalable, standard use.
Expensive, higher maintenance, prone to failure.

### Bus

Devices are connected to a backbone connection.

- Advantages and disadvantages

Easy and cost-efficient
No redundancy, prone to bottlenecking

### Ring

Devices are connected with eachother directly generating a one direction loop.

- Advantages and disadvantages

Easy to troubleshoot
Multiple steps to reach destination, prone to failure, 

## Devices

### Switch

Aggregates multiple devices via ethernet. Interconnect devices in a single place keeping track of who-is-who and sending packets within destination.

### Router

Device that connects different networks and pass traffic between them. The door to a network.



## ARP

ARP is the protocol responsible for allowing devices to identify on a network. It creates a "map" where each IP address within a network is tied to the MAC address of the device holding that IP.

## DHCP

Protocol to assign IPs to new devices within a network. Once the new device enters the networks sends a DHCP Discover to connect with the DHCP server, then the server sends a DHCP offer with the IP the new device can use, then the device sends a DHCP Request confirming the IP used and lastly the server returns an ACK for confirmation.
