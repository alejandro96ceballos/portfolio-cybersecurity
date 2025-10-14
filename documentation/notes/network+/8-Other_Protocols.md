## ICMP

Internet Control Message Protocol

Not TCP or UDP, own protocol

Used to administrative requests like "ping"

## GRE

Generic Routing Encapsulation

Creates a tunnel between two endpoints.
Not encrypted
Used on VPN

## VPN

Encrypted data through a public network

Uses a VPN concentratior for encryption/decryption, often inside firewalls.
Can be hardware or software based.


## IPSEC

Layer 3 security
Encryption and authentication on every packet using IP
Common use, multi-vendor implementation. Standard for environment

Uses AH authentication header and Encapsulation Security Payload to function

## IKE

Internet Key Exchange

Allows to exchange keys for a private connection
Used Diffie-Hellman to create a shared secrett key
UDP 500
ISAKMP

Uses 2 modes
Transport modes makes a packer have IP header-IPSEC header-DATA-IPSEC Trailer. Only data is encrypted
Tunnel mode makes New IP header- IPSEC header-IP header -DATA - IPSEC trailers. IP header and data is encrypted here. More secure




