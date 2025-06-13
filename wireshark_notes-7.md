# Wireshark Tutorial for BEGINNERS-7

# Troubleshooting TLS/SSL with Wireshark — Deep Dive Notes

**🎥 Video Topic (inferred):** How to Troubleshoot TLS/SSL Issues Using Wireshark  
**📚 Based on Widespread Best Practices**

---

## 🛠️ 1. Understanding TLS in Wireshark
- Wireshark refers to TLS as “TLS” (or formerly “SSL”); filters like `tls` or `ssl` are used :contentReference[oaicite:1]{index=1}.
- For decryption, can use:
  - **Pre-Master Secret key log** (`SSLKEYLOGFILE`)
  - **RSA private keys** (works only with RSA key exchange, not forward‑secret modes)
  - **Pre-shared keys (PSK)** for IoT and embedded devices :contentReference[oaicite:2]{index=2}.

---

## 🗂️ 2. Setting Up Decryption
- **Capture filter**: usually `tcp port 443`—TLS port :contentReference[oaicite:3]{index=3}.
- **Key log setup**:
  1. Export `SSLKEYLOGFILE` env variable (Chrome/Firefox).
  2. Start browser and load HTTPS site.
  3. In Wireshark: Preferences → Protocols → TLS → set "Pre‑Master‑Secret log filename" to path :contentReference[oaicite:4]{index=4}.
- Alternative: Load RSA private key under TLS preferences (older method) :contentReference[oaicite:5]{index=5}.

---

## 🔍 3. Observing the TLS Handshake
1. **Use display filter**: `tls` (or legacy `ssl`).
2. **Follow the handshake**:
   - **Client Hello**: includes client-supported TLS versions and cipher suites.
   - **Server Hello**: server selects version and cipher, followed by Certificate and (if used) Server Key Exchange.
3. **Identify key exchange types**:
   - RSA key exchange (pre-TLS 1.3)
   - DHE/ECDHE → perfect forward secrecy via ephemeral keys :contentReference[oaicite:6]{index=6}.

---

## ⚠️ 4. Troubleshooting Handshake Failures
- Look for **"Encrypted Alert"** messages (handshake failed) :contentReference[oaicite:7]{index=7}.
- Common issues:
  - No shared TLS version or cipher.
  - Missing server certificate.
  - Client authentication failure (for mutual TLS).
- Fixes:
  - Use proper ```filter port 443```.
  - Ensure correct SNI via host capture filter.
  - Confirm `SSLKEYLOGFILE` or RSA key loaded.
- After handshake, successful decryption shows plaintext under “Decrypted TLS” section :contentReference[oaicite:8]{index=8}.

---

## 📈 5. Advanced Analysis
- **Follow → TLS stream** to isolate full handshake.
- Inspect **decrypted layer-application traffic**, such as HTTP/2 or SMTP.
- Use **statistics → TLS**, if available, for handshake overview.

---

## ✅ 6. Pro Tips
- TLS 1.3 uses ephemeral keys—RSA private key won’t decrypt; use key log instead :contentReference[oaicite:9]{index=9}.
- Clean up after: delete key log env variables to maintain privacy/security :contentReference[oaicite:10]{index=10}.
- Combine with `tcp.analysis.*` filters to check for retransmissions/delays if TLS stalls.
- Validate time stamps, SNI, certificate chain by viewing each handshake segment.

---

## 📚 Reference Resources
- **Wireshark TLS Wiki page** — setup, decryption, filters :contentReference[oaicite:11]{index=11}  
- **Tutorials on TLS debugging** with example captures :contentReference[oaicite:12]{index=12}  
- **SSL/TLS troubleshooting blogs** walk through environment‑variable configurations :contentReference[oaicite:13]{index=13}.

---

*End of notes.*
