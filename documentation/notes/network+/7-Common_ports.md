# Common Ports

## FTP file transfer protocol. 

TCP 20 and 21.

20 for data tranfer. 21 for control data

Authenticates with username and password, full functionality with add, delente, list...

## SSH

TCP 22
Secure shell.
Remote shell access. Encrypted.

## SFTP

Secure FTP

TCP 22, SSH port and SSH usage. Encrypted.

## Telnet

TCP 23

Console access, not encrypted. Weak security point.

## SMTP

TCP 25 not encrypted
TCP 587 encrypted
Mail exchange

## DNS

Translation between domain name and IP

UDP 53 for small transfers
TCP 53 for big transfers

## DHCP

Automated cnfiguration of IP address subnes mask and other network config
Pooled amount of addresses that are asigned to MAC addreses temporarily
UDP 67, UDP 68

## TFTP

UDP 69
Small fast transfers of information
No authentication, no security

## HTTP and HTTPS

TCP 80 for HTTP not encrypted
TCP 443 for HTTPS encrypted

## NTP 

Network time protocol, time sync
UDP 123
Used on network devices as router, switch...
Critical for logging, authentication...

## SNMP

Simple network manage protocol.
Gathers stadistics from devices
V1 tables, not encrypted
V2 better format for info, not encrypted
V3 Secure standard, integrity, authentication, encryption

UDP 161
UDP 162 notifications

## LDAP

TCP 389
Directory access protocol. Stores and retrieve information in network directories for easy access

TCP 636
LDAPS, encrypted with SSL

## SMB/CIFS

Windows protocol for file and printer sharing
Integrated on windows on explorer
PReviously used NETBIOS

TCP 445

## SYSLog

UDP 514
Consolidated logs accross network
Usually a central log collector uses this. Need a lot of space

## Databases

MS SQL TCP 1433

## RDP

Remote desktop protocol
TCP 3389
Connect to an entire desktop
Uses client service

## SIP

TCP 5060 5061
VoIP session for phone calls
