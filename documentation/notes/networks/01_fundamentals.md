# Networking Fundamentals – Summary

## 1. What is a Network?

- A set of connected devices that share information.
- Can be **Local (LAN)**, **Wide Area (WAN)**, or **Virtual (VPN)**.



## 2. IP Addressing

### IP (Internet Protocol)
- Every device on a network has a unique IP address.
- **IPv4**: format `192.168.0.1`
- **IPv6**: modern extended format `2001:0db8:85a3::8a2e:0370:7334`

### IP Classes:
- Class A: 1.0.0.0 – 126.0.0.0
- Class B: 128.0.0.0 – 191.255.0.0
- Class C: 192.0.0.0 – 223.255.255.0

### Subnets and Mask:
- Divide networks into smaller parts.
- Example: `192.168.1.0/24` → 256 usable addresses



## 3. Common Network Protocols

| Protocol | Description                    | Port |
|----------|--------------------------------|------|
| TCP      | Reliable, connection-based     | Varies |
| UDP      | Fast, connectionless           | VoIP, games |
| HTTP     | Web (non-encrypted)            | 80   |
| HTTPS    | Encrypted web traffic          | 443  |
| FTP      | File Transfer Protocol         | 21   |
| SSH      | Secure remote login            | 22   |
| DNS      | Domain resolution              | 53   |
| DHCP     | Auto IP assignment             | 67/68|

---

##  4. Basic Network Tools

- `ping` → Test host availability
- `traceroute` → Shows path to a destination
- `ip a` / `ifconfig` → Display interfaces and IPs
- `netstat` / `ss` → Show active connections
- `nmap` → Port and service scanning



## 5. OSI Model (7 layers)

1. **Physical** (cables, signals)
2. **Data Link** (MAC addresses, switches)
3. **Network** (IP, routing)
4. **Transport** (TCP/UDP)
5. **Session** (session control)
6. **Presentation** (data format)
7. **Application** (HTTP, DNS, FTP)


##  6. Basic Network Security Concepts

- Firewalls (packet filtering, stateful)
- MAC/IP filtering
- VPNs for encrypted communication
- NAT to mask internal IPs


##  7. NAT and DHCP

- **NAT (Network Address Translation)**: translates private IPs to public IPs.
- **DHCP (Dynamic Host Configuration Protocol)**: assigns IPs automatically to devices.
