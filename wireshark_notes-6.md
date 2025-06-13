#Wireshark Tutorial for BEGINNERS-6
# Troubleshooting Network Latency Issues Using Wireshark — Deep Dive Notes

**🎥 Video Title:** How to Troubleshoot Network Latency Issues Using Wireshark  
**📅 Published:** Approximately 2.1 years ago :contentReference[oaicite:2]{index=2}

---

## 🌐 Introduction: Understanding Latency
- Definition: **Latency** = packet transit delay; critical in network performance.
- Video objectives:
  - How to identify latency using Wireshark.
  - Analyze contributing factors like jitter, retransmissions, RTT spikes.

---

## ⚙️ Step 1: Capture Setup for Latency Analysis
- Use capture filters: e.g. `ip` or `tcp` to focus captures.
- Ensure data captured includes source, destination, and timing headers.
- Save captures with descriptive filenames (e.g., `latency_test.pcap`).

---

## 📊 Step 2: Analyzing Round-Trip Time (RTT)
- Enable **TCP Analysis flags** in `Analyze → Enabled Protocols → TCP`.
- Key metrics:
  - `tcp.analysis.ack_rtt` shows RTT per ACK packet.
  - Check variation across ACKs to see latency spikes and trends.
- RTT spikes often indicate congestion, overloaded servers, or network loops.

---

## 🌀 Step 3: Jitter and Spikes Detection
- Calculate **jitter** by comparing consecutive RTT values.
- Use differences in `tcp.analysis.ack_rtt` to determine instability.
- Identify consistent vs. transient jitter patterns.

---

## 🔄 Step 4: Find Retransmissions & Duplicate ACKs
- Filter: `tcp.analysis.retransmission` and `tcp.analysis.duplicate_ack`.
- Retransmissions show packet loss or late/dropped ACKs—impact latency.
- Group retransmissions to locate problematic endpoints.

---

## 📈 Step 5: Visual Trends with IO Graphs
- Go to `Statistics → IO Graphs`.
  - Chart RTT over time to visualize latency trends.
  - Overlay retransmissions counts to correlate with RTT spikes.

---

## 🕵️ Step 6: Stream Analysis for End-to-End View
- Right-click packet → "Follow TCP Stream" to view full request/response sequence.
- Observe timestamps at:
  1. Client request
  2. Server response
  3. ACKs
- Helps locate where delays occur: server processing vs. network delay.

---

## 🏗️ Step 7: Factor in Infrastructure and Network Path
- Check for high latency due to:
  - Network loops, broadcast storms
  - Unoptimized routes (e.g. long AS path, suboptimal hops)
  - Device overload (queues, CPU spike)
- Use TTL values and packet paths to inspect routing behavior.

---

## 💡 Pro Tips & Best Practices
- Always label capture files with date/time and context.
- Save filters and profiles (e.g., “Latency‑analysis”).
- Correlate Wireshark findings with external tools (ping, traceroute).
- Document and export key streams for sharing.

---

## ✅ Summary — Key Takeaways
- Use `tcp.analysis.ack_rtt` to measure RTT per packet.
- Monitor jitter via variation in RTT.
- Retransmits and duplicate ACKs signal underlying issues.
- Visual IO Graphs help detect patterns at scale.
- Follow full streams to pinpoint delays.
- Pair packet insights with network/device monitoring.

---

## 🚀 Additional Resources
- Official Wireshark docs: TCP analysis options.
- Case studies on latency debugging.
- Community forums, StackOverflow threads.

---

*End of notes.*
