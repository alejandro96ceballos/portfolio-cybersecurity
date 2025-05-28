# Wireshark: The Basics

**Category:** Networking

---

## 📚 Key Concepts

- **Packet Capture (PCAP):** Saving network traffic for later analysis.
- **Filters:**
  - Capture filters: Applied during capture (e.g., `tcp port 80`)
  - Display filters: Applied to analyze data (e.g., `http`, `ip.addr == 192.168.1.1`)
- **Protocols analyzed:** DNS, HTTP, TCP, TLS, ARP, etc.

---

## 💡 Commands and Tools

- **Wireshark GUI**
- Example display filters:
  - `http`
  - `tcp.port == 443`
  - `ip.addr == 10.0.0.1`

---

## 📌 Additional Notes

- Wireshark is a vital tool for network forensics and protocol understanding.
- Use with caution on live networks—packet capture may reveal sensitive data.
