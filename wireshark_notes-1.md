#Wireshark Tutorial for BEGINNERS-1
# 🧠 Wireshark Tutorial (Inspiration Academy) – Detailed Notes

## 📌 1. Introduction to Wireshark
Wireshark is a free, open-source network packet analyzer.

### Used for:
- Monitoring network traffic
- Diagnosing network issues
- Learning about protocols
- Ethical hacking and security auditing

---

## 🖥️ 2. Installing & Starting Wireshark
- Available on Windows, macOS, and Linux.
- Installation includes WinPcap or Npcap for packet capturing.
- Interface opens with a list of available network interfaces (Ethernet, Wi-Fi, etc.)

### Start Capture:
- Click on the interface (e.g., Wi-Fi).
- Live packet capture starts immediately.

---

## 🎯 3. Understanding the Interface
- **Top Pane:** Packet list (time, source, destination, protocol, info).
- **Middle Pane:** Packet details (broken into protocol layers).
- **Bottom Pane:** Hexadecimal and ASCII representation of raw data.

---

## 🔍 4. Capture & Display Filters

### 🧱 Capture Filters
- Set **before** capturing traffic.
- Limits the amount of data recorded.

#### Examples:
```bash
tcp port 80       # only HTTP traffic
host 192.168.1.5  # traffic to/from specific IP
```

### 🔎 Display Filters
- Used **after** capture.
- Helps isolate relevant packets.

#### Examples:
```bash
http
ip.addr == 8.8.8.8
tcp.port == 443
```

---

## 🌐 5. Protocol Analysis

### ✉️ HTTP
- View GET/POST requests.
- Status codes (200, 404, etc.).
- Headers and URLs.
- Use filter: `http`
- **Follow TCP Stream** to view entire HTTP conversation.

### 📡 DNS
- Use filter: `dns`
- Watch query names (QNAME), response IPs, TTL, record types (A, AAAA, CNAME).

### ⚡ TCP/UDP
- View TCP 3-way handshake: `SYN → SYN-ACK → ACK`
- TCP Flags: SYN, ACK, FIN, RST
- View port numbers (source/destination)

### 🟢 ICMP
- Use filter: `icmp`
- Shows ping requests (Echo) and replies

---

## 🛠️ 6. Wireshark Tools & Features

### ✅ Follow Stream
- Reconstructs full communication session (HTTP, TCP, etc.)
- Helpful for viewing chats, form data, login attempts

### 📁 Export Objects
- Export downloadable content from HTTP packets
- Menu: `File → Export Objects → HTTP`

### 📊 Statistics
- **Protocol Hierarchy:** Breakdown of all observed protocols
- **Conversations:** Lists communication between endpoints
- **IO Graphs:** Visual network activity over time

### 🗂️ Saving Captures
- Save as `.pcapng` or `.pcap`
- Can reopen later for offline analysis

---

## 🔒 7. Use Cases
- Capture DNS resolution steps
- Inspect website traffic (headers, cookies)
- Analyze malware or suspicious behavior
- Troubleshoot connectivity issues
- View device communication on LAN

---

## 🧪 8. Sample Lab Task

### 🧪 Lab: Capture Ping Traffic
1. Open Wireshark and select Wi-Fi interface
2. In terminal: `ping google.com`
3. Apply filter: `icmp`
4. Observe:
   - Echo Request and Reply
   - Time taken (RTT)
   - IP headers

---

## 🧠 9. Pro Tips
- Prefer Display Filters for real-time analysis
- Use Capture Filters to avoid massive captures
- Identify protocols manually if ports are misleading
- Use Coloring Rules (e.g., red = TCP reset)

---

## 📚 Suggested Practice
- Platform: **TryHackMe – Wireshark**

### Challenge:
- Capture DNS + HTTP + ICMP in one session
- Analyze each protocol
- Export HTTP objects from capture

---
