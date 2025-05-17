# Command Line – Windows CMD

## 🔍 System Info
- `ver`              – OS version  
- `systeminfo`       – Detailed system info  

## 📁 File & Dir
- `dir`              – List contents  
  - `/w` wide, `/p` pause, `/s` recursive  
- `cd <path>`        – Change directory  
- `copy <src> <dst>` – Copy files  
- `move <src> <dst>` – Move/rename  
- `del <file>`       – Delete file  

## 🌐 Network
- `ipconfig`         – IP config  
  - `/all` detailed  
- `ping`, `tracert`, `nslookup` – diagnostics  
- `netstat -an`      – Active connections  

## 🛑 Processes & Shutdown
- `tasklist`         – List processes  
- `taskkill /PID <pid> /F` – Force kill  
- `shutdown /s /t 0` – Shutdown now  
- `shutdown /r /t 0` – Restart now  

---


# Command Line – Linux Shell

## 🐚 Shell Environment
- `$PS1`           – Prompt variable  
- `~`              – Home directory alias  

## 📂 FS & Navigation
- `ls -lah`        – All files, human sizes  
- `cd -`           – Previous directory  
- `tree`           – Directory tree (install)  

## 🔍 Search & Filter
- `grep -Cin "error" /var/log/syslog`  
- `awk '{print $1}' file` – Field extraction  
- `sed 's/old/new/g' file` – Inline replace  

## 🔧 Process & Jobs
- `&`              – Background job  
- `fg %1`          – Bring job 1 to foreground  
- `jobs`           – List background jobs  

## 🔄 Networking
- `curl -I example.com`  
- `wget https://site/file`  
- `nc -lvnp 4444`  – Netcat listener  
