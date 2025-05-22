# Tcpdump: The Basics

**Category:** Networking


## 📚 Key Concepts

- **Live Capture:** Monitor network interface in real-time.
- **Saving Captures:** Use `-w` to write to `.pcap` files.
- **Filtering Traffic:** BPF syntax to match traffic (e.g., `tcp`, `port 80`, `host 8.8.8.8`)

---

## 💡 Commands and Tools

- `tcpdump -i eth0`: Capture from interface `eth0`.
- `tcpdump -w capture.pcap`: Save to file.
- `tcpdump -n port 53`: Capture DNS traffic without name resolution.

---

## 📌 Additional Notes

- Tcpdump is lightweight and script-friendly.
- Ideal for use in servers and remote systems where GUI tools like Wireshark aren't available.
