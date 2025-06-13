# Wireshark Tutorial for BEGINNERS-8


# Wireshark Network Analysis & Troubleshooting

## 🔁 TTL (Time to Live) Analysis in Wireshark

### 🧠 Concept
- TTL is a field in the IP header used to prevent infinite routing loops.
- Each router hop decrements the TTL by 1.
- TTL values differ based on OS:
  - Cisco: 255
  - Windows: 128
  - Linux: 64

### 🧪 Use Case
- **Routing Issue Detection**: If TTL isn't decrementing, routing isn't occurring.
- TTL decrement observed via packet capture using Wireshark.

### 🧪 Lab Overview
1. Devices configured in GNS3 with routed ports.
2. Ping from a host through multiple routers.
3. Wireshark shows TTL values reducing with each hop.
4. Directly connected devices won't show TTL change.

---

## 🎨 Coloring Rules in Wireshark

### 👨‍🎨 Purpose
- Enhance readability during analysis.
- Visually distinguish packet types (e.g., ICMP, SYN, ARP).

### ⚙️ How to Configure
1. Go to `View > Coloring Rules`.
2. Click ➕ to add a custom rule.
3. Set a name (e.g., `ICMP Packets`).
4. Use a filter (e.g., `icmp`).
5. Assign a background/foreground color.

### ✅ Tip
- Color code `tcp.flags.syn == 1` for SYN packets.
- Great for analyzing handshakes and ARP floods.

---

## ⏱️ Delta Time in Wireshark

### 🔍 What is Delta Time?
- Time difference between captured packets.
- Used to measure:
  - Round-trip time (RTT).
  - Network latency.
  - Delay in handshakes or responses.

### 📈 How to Enable
1. Windows: `Edit > Preferences > Columns`
2. macOS: `Wireshark > Preferences > Columns`
3. Add: `Delta Time Display`

### 🛠 Use Cases
- RTT over ICMP:
  - First packet takes longer due to ARP resolution.
  - Subsequent packets show reduced RTT.
- Slowness if delta times >1s persistently.

---

## 📊 Statistics & Endpoints

### 📦 Use Case
- View communication between IPs.
- Analyze packet count, bytes, protocols used.

### 🔍 Access Path
- `Statistics > Endpoints`
  - See IPv4, IPv6, TCP, UDP, Ethernet communication.
  - Sort by RX, TX, packet count, etc.

### 🧪 Practical Insight
- Check if a PC is generating/receiving traffic.
- Spot top talkers or dormant endpoints.

---

## ❗ Expert Info in Wireshark

### 🚨 Purpose
- Aggregate and show potential issues:
  - Retransmissions
  - Duplicate ACKs
  - Malformed packets
  - TCP FIN flags
  - Window size problems

### 💡 How to Use
- Bottom-left of Wireshark: Click **Expert Info**.
- Right-click any issue:
  - `Apply as Filter`
- Examples:
  - `tcp.analysis.retransmission`
  - `tcp.analysis.duplicate_ack`

---

## 🔄 SPAN (Port Mirroring) Configuration

### 📘 What is SPAN?
- Port mirroring forwards all traffic from a source interface/VLAN to a monitoring port.

### 🧪 Lab Steps (Cisco-like syntax)
```bash
monitor session 1 source interface Fa0/1 both
monitor session 1 destination interface Fa0/2
```

### 🧪 Use Case
* Connect Wireshark to monitoring port.
* See all ingress/egress traffic for an interface.
* Useful in production for live traffic debugging.

---

## 💾 Packet Capture on Device (No Mirroring)

### 🔍 Alternative Method
* Use global capture if port mirroring is unsupported.
* Save `.pcap` to local flash:
```bash
monitor capture mycap interface fa0/1 match ip host 192.168.1.1
monitor capture mycap start
monitor capture mycap export flash:mycap.pcap
```
* Use TFTP to export and analyze in Wireshark.

---

## 🧠 Key Takeaways
* **TTL decrement** confirms multi-hop routing.
* **Coloring rules** simplify visual packet identification.
* **Delta Time** helps detect latency or slowness.
* **Expert Info** is your error dashboard in Wireshark.
* **SPAN Ports** or local capture provide access to live traffic.
* Use **Endpoints/Statistics** for high-level traffic analysis.

---

## ✅ Suggested Filters for Practice
```wireshark
ip.addr == 10.0.0.1
icmp
tcp.analysis.retransmission
tcp.flags.syn == 1
udp
frame.time_delta > 1
```
