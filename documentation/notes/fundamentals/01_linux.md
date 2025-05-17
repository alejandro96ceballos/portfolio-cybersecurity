# Linux Fundamentals 1 – Introduction & Navigation

## 🗄️ Filesystem Hierarchy
- `/` – Root  
- `/home` – User directories  
- `/etc` – Configuration files  
- `/var` – Variable data (logs, mail)  
- `/usr` – Installed applications and libraries  
- `/bin` – Essential binaries  
- `/sbin` – System binaries  

## 🔸 Basic Commands
| Command               | Description                                            |
|-----------------------|--------------------------------------------------------|
| `pwd`                 | Print working directory                                |
| `ls`                  | List files/directories                                 |
| `ls -l`               | Long listing (permissions, owner, size, date)         |
| `ls -a`               | Include hidden files (`.`)                             |
| `cd <dir>`            | Change directory                                       |
| `cd ..`               | Up one level                                           |
| `mkdir <dir>`         | Create directory                                       |
| `rmdir <dir>`         | Remove empty directory                                 |
| `touch <file>`        | Create empty file or update timestamp                  |
| `rm <file>`           | Remove file                                            |
| `rm -r <dir>`         | Remove directory and its contents                      |

## 🔍 Viewing & Searching
- `cat <file>`       – Concatenate and display file  
- `less <file>`      – View file with scroll (q to quit)  
- `head -n 10 <file>` – First 10 lines  
- `tail -n 10 <file>` – Last 10 lines  
- `grep "pattern" <file>` – Search for pattern (case‐sensitive)  
  - `grep -i` – Case‐insensitive  
  - `grep -r` – Recursive in directories  
- `find /path -name "*.conf"` – Find files by name  

## 🔄 Redirection & Pipes
- `>`  – Redirect stdout to file (overwrite)  
- `>>` – Redirect stdout to file (append)  
- `2>` – Redirect stderr to file  
- `|`  – Pipe stdout of one command into stdin of another  
  ```bash
  ls -l /etc | grep ".conf" > conf_list.txt

# Linux Fundamentals 2 – Permissions & Users

## 🔐 File Permissions
- Represented as `rwxr-xr--` (owner/group/others)
  - `r`=4, `w`=2, `x`=1 → numeric mode (e.g. `chmod 755 file`)
- Commands:
  - `chmod u+x file` – Add execute for user  
  - `chmod 600 file` – Owner read/write only  
  - `ls -l` – View permissions  

## 👥 Ownership
- `chown user:group file` – Change owner and group  
- `chown user file` – Change owner only  

## 🛠️ User & Group Management
- `adduser <user>` – Add new user (interactive)  
- `userdel <user>` – Delete user  
- `usermod -aG <group> <user>` – Add user to group  
- `groupadd <group>` – Create new group  
- `groups <user>` – Show groups of user  

## 🔑 Sudo & Root
- `sudo <command>` – Execute as superuser  
- `sudo su -` – Switch to root shell  
- `visudo` – Safely edit `/etc/sudoers`  


# Linux Fundamentals 3 – Packages, Processes & Logs

## 📦 Package Management (Debian/Ubuntu)
- `apt update`    – Refresh package index  
- `apt upgrade`   – Upgrade all packages  
- `apt install <pkg>` – Install package  
- `apt remove <pkg>` – Remove package  
- `dpkg -i <file>.deb` – Install local .deb  

## ⚙️ Process Management
- `ps aux`       – List all processes  
- `top` / `htop` – Interactive process viewer  
- `kill <PID>`   – Send SIGTERM  
- `kill -9 <PID>` – Force kill (SIGKILL)  
- `pkill <name>` – Kill by process name  

## 📝 System Logs
- Stored in `/var/log/`  
- `dmesg`         – Kernel messages  
- `journalctl`    – Systemd logs  
- `tail -f /var/log/syslog` – Follow log file  

