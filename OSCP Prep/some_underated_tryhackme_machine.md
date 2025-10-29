### Tier 1: The Essentials (Start Here)

These rooms are perfect for learning the fundamental enumeration -> foothold -> privesc cycle. They are considered easy but cover concepts you will see again and again.

1. **Vulnversity**
    
    - **Why it's OSCP-like:** A perfect beginner box. It teaches you web enumeration, directory busting, finding an active vulnerability (file upload), and then using a classic SUID binary misconfiguration to escalate privileges. This is a mini-OSCP experience in one room.
    - **Key Concepts:** Web Enumeration, File Upload Vulnerabilities, SUID Privilege Escalation.
2. **Blue**
    
    - **Why it's OSCP-like:** This is a classic Windows box. It's designed to teach you how to exploit the infamous MS17-010 (EternalBlue) vulnerability. You'll learn to identify a vulnerable Windows version and use Metasploit (or a manual script) to get a SYSTEM shell directly. The OSCP allows Metasploit on one machine, so this is crucial practice.
    - **Key Concepts:** Windows Enumeration (SMB), MS17-010/EternalBlue, Metasploit.
3. **Kenobi**
    
    - **Why it's OSCP-like:** This Linux room is fantastic OSCP practice. It requires you to enumerate Samba (SMB) shares, exploit a known vulnerability in ProFTPD for a foothold, and then escalate privileges by finding and manipulating a SUID binary with a path variable vulnerability.
    - **Key Concepts:** Samba Enumeration (`enum4linux`), Exploiting a known vulnerability, SUID/Path Privilege Escalation.
4. **Steel Mountain**
    
    - **Why it's OSCP-like:** Another excellent Windows box. You'll gain your initial foothold by exploiting a known vulnerability in a web server (similar to Blue). The real lesson here is the privilege escalation, which involves identifying an "Unquoted Service Path" vulnerability—a very common Windows privesc vector.
    - **Key Concepts:** Metasploit, Windows Post-Exploitation, Unquoted Service Path Privilege Escalation.

---

### Tier 2: Building on the Basics

These rooms are a bit more complex and may require you to chain a few things together.

5. **LazyAdmin**
    
    - **Why it's OSCP-like:** This Windows machine focuses on password guessing and misconfigurations. You'll find a password backup in an SMB share, use it to log into a web admin panel, and then gain a reverse shell. The privilege escalation is a simple but common technique.
    - **Key Concepts:** SMB Enumeration, Password Cracking/Guessing, Web Exploitation.
6. **Bounty Hacker**
    
    - **Why it's OSCP-like:** This is a good reconnaissance and enumeration challenge. It forces you to be thorough with your initial scans to find the right entry point. It's a great exercise in "trying harder."
    - **Key Concepts:** FTP Enumeration, Weak Credentials, TTY Shells.
7. **Simple CTF**
    
    - **Why it's OSCP-like:** As the name implies, it's a straightforward CTF that follows the classic OSCP pattern. It involves exploiting a known vulnerability for a foothold and then finding a simple kernel exploit for privilege escalation.
    - **Key Concepts:** Exploiting a public CVE, Basic Linux Kernel Exploit.

---

### Special Mention: Buffer Overflow Practice

The OSCP exam has a mandatory buffer overflow component. TryHackMe has a **free** room dedicated to this exact skill.

- **Buffer Overflow Prep** (from the Offensive Pentesting Path)
    - **Why it's a must-do:** This room is a step-by-step guide to the Windows buffer overflow methodology required for the OSCP exam. It walks you through Fuzzing, Finding the Offset, Overwriting EIP, Finding Bad Characters, and Getting a Shell. It's one of the best free resources available for this specific topic.

---

### How to Approach These Machines for OSCP Prep

1. **No Walkthroughs (At First):** The single most important rule. The OSCP exam is about your ability to solve problems under pressure. Struggle with the machine for a few hours. Get stuck. This is where the real learning happens.
2. **Enumerate Everything:** Run `nmap` with `-sC` (scripts) and `-sV` (versions). If you find a web server, run a directory bruteforcer like `gobuster` or `dirb`. If you find SMB, use `enum4linux`. Don't stop until you've investigated every port.
3. **Take Detailed Notes:** Use a tool like CherryTree, Obsidian, or Notion. Document every command you run and its output. Note down potential vulnerabilities. This is a critical skill for the OSCP exam report.
4. **If You Get Stuck:** After you've truly tried, it's okay to get a small hint. Look at the official room write-up _one step at a time_. Find the hint for the foothold, then close the write-up and try to execute it yourself. Then, try to do the privilege escalation on your own.
5. **Think Manually:** While Metasploit is great for rooms like `Blue` and `Steel Mountain`, always ask yourself: "Is there a manual exploit script for this on Exploit-DB or GitHub?" Learning to run manual exploits is a core OSCP skill.
