
# Windows Fundamentals 1 – File Systems & Accounts

## 🗂️ NTFS vs FAT32

### NTFS
- **Max file size**: practically unlimited  
- **Permissions**: ACLs per file/folder  
- **Journaling**: quick recovery after crashes  
- **Encryption**: EFS support  
- **Compression & quotas**: built-in  

### FAT32
- **Max file size**: 4 GB  
- **Max volume**: 2 TB  
- **No permissions**: open access  
- **No journaling**: higher corruption risk  
- **Use case**: USB drives for cross-platform  

## 👤 User Accounts
- **Administrator**: full system control  
- **Standard**: limited privileges  
- **Guest**: minimal, disabled by default  

## 🔐 UAC (User Account Control)
- **Always notify**: prompt on all changes  
- **Default**: notify on apps, not on user changes  
- **Never notify**: disabled (insecure)  

---

# Windows Fundamentals 2 – System Tools & Configuration

## 🛠️ System Tools
- **Task Manager** (`Ctrl+Shift+Esc`):  
  - Processes, Performance, App history, Startup  
- **Event Viewer** (`eventvwr.msc`):  
  - Windows Logs → Application, Security, System  
- **Services** (`services.msc`):  
  - Start/stop services; set startup type (Automatic, Manual, Disabled)  

## ⚙️ System Configuration (msconfig)
- **Boot**: Safe Mode, Boot logs  
- **Services**: Enable/disable system services  
- **Startup**: Manage startup apps (moved to Task Manager in Win10+)  

## 📄 Registry Editor (`regedit`)
- **Hives**: HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER, etc.  
- **Backup**: File → Export before changes  
- **Common tweaks**:  
  - Disable lock screen  
  - Auto-login settings  

---



# Windows Fundamentals 3 – Networking & AD Basics

## 🌐 Networking Commands
- `ipconfig /all`     – Full IP config  
- `ping <host>`       – Test reachability  
- `tracert <host>`    – Trace route  
- `nslookup <domain>` – DNS query  
- `netstat -ano`      – Active connections + PIDs  

## 🏢 Active Directory Basics
- **Domain Controller**: Authenticates users  
- **OU (Organizational Unit)**: Logical grouping of objects  
- **Users & Groups**:  
  - `Active Directory Users and Computers` console  
  - Group scopes: Global, Domain Local, Universal  
- **GPOs (Group Policy Objects)**:  
  - Applied at Site/Domain/OU  
  - Settings for security, software deployment  

---


