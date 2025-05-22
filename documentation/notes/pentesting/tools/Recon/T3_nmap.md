# Nmap: The Basics

**Category:** Networking


## 📚 Key Concepts

- **Host Discovery:** Find active systems.
- **Port Scanning:** Identify open TCP/UDP ports.
- **Service Version Detection:** Use `-sV` to fingerprint services.
- **OS Detection:** Use `-O` to try to determine the OS.
- **Scripting Engine (NSE):** Use `-sC` or `--script=<script>` to run vulnerability detection and enumeration scripts.

---

## 💡 Commands and Tools

- `nmap 192.168.1.0/24`: Scan an entire subnet.
- `nmap -sV -p 22,80 target`: Scan specific ports with version detection.
- `nmap -A target`: Aggressive scan including OS, version, script, and traceroute.
- `nmap -oN scan.txt target`: Save output to file.

---

## 📌 Additional Notes

- Nmap is essential for reconnaissance in penetration testing.
- Be mindful of IDS/IPS systems when scanning production networks.
