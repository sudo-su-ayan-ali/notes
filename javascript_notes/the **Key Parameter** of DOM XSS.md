# 🔐  the **Key Parameter** of DOM XSS

---

### ✅ **DOM-Based XSS (Cross-Site Scripting)** occurs when the *client-side JavaScript* reads data from a **source** (e.g., the URL, cookies, or `localStorage`) and dynamically writes it to the DOM without proper sanitization or validation — resulting in JavaScript execution.

---

## 🚨 Key Concepts

In DOM XSS, **the "key parameter"** generally refers to:

> Any **URL parameter**, **fragment**, or **input source** that can be manipulated by an attacker and is eventually accessed by the JavaScript code in the browser.

---

## 🧩 Common Key Sources for DOM XSS

| Source                        | JavaScript API Used       | Examples                         |
|------------------------------|---------------------------|----------------------------------|
| `location.search`            | Query parameters          | `?name=<script>alert(1)</script>` |
| `location.hash`              | Hash fragment             | `#<script>alert(1)</script>`     |
| `location.href`              | Full URL                  | Entire URL input                 |
| `document.URL`               | Full URL                  |                                  |
| `document.referrer`          | Previous page’s URL       |                                  |
| `document.cookie`            | Cookies                   |                                  |
| `localStorage`, `sessionStorage` | Stored values        |                                  |

---

## 🔑 Examples of Vulnerable Code

### ✅ 1. URL Parameter (Query String)
```javascript
// URL: http://example.com?name=<script>alert(1)</script>

let name = new URLSearchParams(window.location.search).get('name');
document.getElementById("output").innerHTML = name; // ❌ Vulnerable
```

> Here, **"name"** is the **key parameter** used to inject malicious code.

---

### ✅ 2. Hash Fragment
```javascript
// URL: http://example.com#<img src=x onerror=alert(1)>

let hash = location.hash.substring(1);
document.body.innerHTML = hash; // ❌ Vulnerable
```

---

### ✅ 3. From Cookies
```javascript
// Cookie: username=<script>alert('xss')</script>

let cookies = document.cookie;
document.write("Welcome " + cookies); // ❌ Vulnerable
```

---

## 💥 Key Parameter Examples in Real Attacks

Let’s say a script on the page does:

```javascript
let search = location.search.split('=')[1];
document.getElementById('result').innerHTML = search;
```

If the user visits:

```
https://example.com/page.html?key=<img src=x onerror=alert('XSS')>
```

> The **parameter `key`** is injected into the page, and if `innerHTML` is used, the XSS payload executes.

---

## ✅ How to Prevent DOM-Based XSS

| Preventive Action          | How                                        |
|---------------------------|---------------------------------------------|
| **Sanitize input**        | Use libraries like `DOMPurify`              |
| **Use textContent**       | Avoid `innerHTML`, prefer `textContent`     |
| **Escape HTML entities**  | Convert `<`, `>`, `&` to safe equivalents    |
| **Validate input**        | Whitelist allowed characters or patterns    |

---

## ✅ Quick Safe Alternative

```javascript
// Safe: Using textContent
document.getElementById("output").textContent = name;
```

