# Wireshark Tutorial for BEGINNERS-9
# Advanced Wireshark Network Troubleshooting Guide

## 🔁 TTL (Time To Live) Troubleshooting

### 💡 Concept Recap
- TTL is an IP header value set by the source OS.
  - **Windows**: 128
  - **Cisco**: 255
  - **Linux/macOS**: 64
- Each router hop decrements TTL by 1. If TTL is **not** decreasing → routing problem.

### 🧪 Practical Demo
- **Lab Setup**:
  - Routers configured in GNS3.
  - IP routing and static routes used.
  - TTL monitored during ICMP ping.

- **Wireshark Capture**:
  - Confirm TTL decrementing per hop.
  - Directly connected devices won't decrement TTL.
  - Trace route shows where TTL drops (proof of multi-hop).

- **Use Case**:
  - Detect black holes or misconfigured routers.
  - TTL not decrementing → indicates traffic not leaving local segment.

---

## 🎨 Custom Coloring Rules in Wireshark

### 🎯 Goal
- Visualize packet types more efficiently using color filters.

### 🛠 Configuration Steps
1. Open `View > Coloring Rules`
2. Click ➕ to add new rule
3. Enter filter (e.g., `icmp`, `tcp.flags.syn == 1`)
4. Choose colors for background/foreground

### 🧠 Usage
- Highlight SYN, ACK, FIN packets.
- Track ARP requests visually.
- Easily follow conversation chains.

---

## ⏱️ Delta Time (Round Trip Time Measurement)

### ⌛ Importance
- Delta Time = time between captured packets.
- Used to measure:
  - Network delay
  - Application lag
  - Initial ARP resolution delay

### 🧪 Lab Observations
- First ICMP packet: ~62 ms (includes ARP).
- Next packets: lower times (~46 ms).
- Anything >1 sec indicates a network issue.

### 🔧 How To Enable
1. Go to `Preferences > Columns`
2. Add `Delta Time Display`
3. Customize via right-click → Add as column

### 📌 Tip
- Track Delta Time in TCP handshakes and retransmissions.
- Helps identify congested links.

---

## 📊 Statistics and Endpoints

### 🔍 Purpose
- Monitor live communications (TX/RX).
- Track protocols: TCP, UDP, ICMP, IPv4, IPv6.

### 📈 Access:
- Go to `Statistics > Endpoints`
- Sort by IP, packets, bytes

### 🧠 Use Case
- Identify top talkers.
- See if a device is reaching external networks.
- Detect unused or suspicious endpoints.

---

## 🚨 Expert Info (Wireshark Error Dashboard)

### 🛠 Functionality
- Found in bottom left → "Expert Info"
- Highlights issues like:
  - TCP retransmissions
  - Duplicate ACKs
  - TCP FIN/Window problems
  - Malformed packets

### 🧪 Filters to Use
```wireshark
tcp.analysis.retransmission
tcp.analysis.duplicate_ack
tcp.flags.fin == 1
```

### 🧠 Use Case
- Troubleshoot broken sessions.
- Isolate packet-level problems quickly.

---

## 🔁 SPAN Port Mirroring (Switch Port Analyzer)

### 📘 What is SPAN?
- Duplicates traffic from a source port/VLAN to a destination port.
- Useful for capturing ingress + egress in Wireshark.

### 🧪 SPAN Lab Setup
```bash
monitor session 1 source interface Fa0/1 both
monitor session 1 destination interface Fa0/2
```

- Monitor both traffic directions.
- Use trunk ports for VLAN-specific captures.

### ⚠️ Note:
- Overuse of SPAN with VLANs may overload switch CPU.
- Always ensure only needed VLANs/interfaces are mirrored.

---

## 💾 Global Packet Capture on Cisco Devices

### 📥 Capture Directly From Router
```bash
monitor capture mycap interface fa0/1 match ip host 192.168.1.1
monitor capture mycap start
monitor capture mycap export flash:mycap.pcap
```

### 📤 Export Flow
1. Save to Flash
2. Transfer via TFTP
3. Open `.pcap` in Wireshark

### ✅ Benefit
- No SPAN needed.
- Works for routing paths inside routers/switches.

---

## 🧠 Final Insights

- **TTL Monitoring** = confirms routing.
- **Delta Time** = reveals delay/bottleneck.
- **Coloring Rules** = enhances visual packet tracking.
- **Expert Info** = your error log.
- **SPAN** = lets you sniff production interfaces.
- **Statistics** = helps audit network behavior.

---

## 🎯 Practice Filters

```wireshark
ip.addr == 192.168.1.1
icmp
arp
tcp.flags.syn == 1
tcp.analysis.retransmission
frame.time_delta > 0.5
```

---
