#Wireshark Tutorial for BEGINNERS-3
# 🧠 Advanced Wireshark Notes: Troubleshooting Network Slowness

## 📌 Overview
This guide provides a step-by-step real-world troubleshooting approach using Wireshark to investigate network slowness. It explains how to identify problems like high latency, packet loss, retransmissions, TCP window issues, and application-level delays with practical analysis using packet captures.

---

## 🧰 Preparation Phase

### 1. Understand the Complaint
- Who is affected? (specific user or global)
- What is slow? (file transfers, loading, database queries, etc.)
- When does it happen? (always, peak hours, random)
- Where is the slowness felt? (internal network, internet access, VPN?)

### 2. Decide Where to Capture
- Ideally between **client ↔ server** or near firewall/router.
- Ensure port mirroring or use packet capture tools if on virtualized infrastructure.

---

## 🎥 Packet Capture Using Wireshark

### ✅ Start the Capture
- Launch Wireshark with admin/root privileges.
- Select the correct **interface** (Ethernet, Wi-Fi).
- Use **Capture Filters** to limit unnecessary data (e.g., `host <IP>`).
- Start the capture *before* reproducing the slowness.

### 🔄 Reproduce the Issue
- Try accessing the slow application or process.
- Ensure the capture includes the interaction causing delay.

### 🛑 Stop & Save
- Save the `.pcapng` file.
- Use a meaningful name like `slow_http_2025-06-13.pcapng`.

---

## 🔍 Step-by-Step Deep Analysis in Wireshark

### 1. Initial Filtering
Apply **Display Filters** to isolate relevant traffic:
```bash
ip.addr == 192.168.1.5

tcp.port == 443

tcp.analysis.retransmission

tcp
```

### 2. Identify TCP Streams
- Right-click a packet → **Follow** → **TCP Stream**.
- View the entire conversation.
- Observe request/response delays.

### 3. Analyze TCP Three-Way Handshake
- `SYN →`, `SYN-ACK ←`, `ACK →`
- Check RTT between these.

### 4. Check for Retransmissions
```bash
tcp.analysis.retransmission
```
- Look for duplicate ACKs and retransmitted packets.

### 5. Examine TCP Window Size
Enable column: `Window Size Value`
```bash
tcp.window_size == 0
```

### 6. Analyze Response Time
- Sort by `Time` or use **Delta Time**.
- Use: `Statistics → TCP Stream Graphs → RTT`.

### 7. Check Throughput Bottlenecks
- Use: `Statistics → Conversations` and `Statistics → IO Graphs`.

### 8. Identify Server vs Network Delays
| Layer | Indicators |
|-------|------------|
| Network | High RTT, retransmissions |
| Server | Long delay in response with no packet loss |
| Application | Delay after successful delivery |

---

## 📈 Example Scenario
- User experiences app slowness.
- TCP handshake is fast.
- 2s+ delay in server response.
- No retransmissions → **Application Layer Issue**.

---

## 🩺 Diagnostic Patterns
| Symptom | Likely Cause |
|---------|---------------|
| High RTT | WAN issue |
| Packet loss | Link failure, congestion |
| Duplicate ACKs | Congestion or fault |
| Zero TCP Window | Receiver bottleneck |
| Long response time | App/server lag |

---

## 🛠️ Fix Suggestions
| Problem | Action |
|---------|--------|
| Packet loss | Check NICs, links |
| Small window | Adjust TCP buffers |
| High RTT | Optimize routes |
| Duplicate ACKs | Check duplex, QoS |
| App delay | Profile app, backend |

---

## ✅ Final Checklist
- [x] Captured clean session
- [x] Used correct filters
- [x] Reviewed handshake/stream/RTT
- [x] Identified retransmissions/window issues
- [x] Compared with healthy session
- [x] Reported findings with .pcap

---

## 📦 Exporting & Reporting
- Export filtered packets: `File → Export Specified Packets`
- Export tables: `File → Export as CSV`
- Include .pcap, graphs, and notes in ticket

---

## 💬 Conclusion
Wireshark enables deep packet inspection and slowness root cause analysis. Master its filters, graphs, and TCP tools to bridge network and application troubleshooting.

---
