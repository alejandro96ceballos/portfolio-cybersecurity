# Networking Secure Protocols

**Category:** Networking

---

## 📚 Key Concepts

- **TLS (Transport Layer Security):** Secures connections by encrypting data between client and server; used in HTTPS.
- **SSH (Secure Shell):** Provides secure remote command-line access.
- **VPN (Virtual Private Network):** Encrypts all traffic between a user and a remote network.

---

## 💡 Commands and Tools

- `ssh user@host`: Connect securely to a remote machine.
- `openssl s_client -connect host:443`: Inspect TLS certificates.
- VPN clients: `openvpn`, `wireguard`, OS-native options.

---

## 📌 Additional Notes

- Proper implementation of these protocols is vital for maintaining confidentiality and integrity of data in transit.
- Certificates, key pairs, and trusted authorities are central to how TLS/SSL operates.
