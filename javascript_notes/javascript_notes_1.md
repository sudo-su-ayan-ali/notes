### ▶️ Common Functions & Built-ins

| Function          | What it does                              | Example                           |
| ----------------- | ----------------------------------------- | --------------------------------- |
| `alert()`         | Shows a browser popup                     | `alert("Hello!")`                 |
| `console.log()`   | Prints to the browser console             | `console.log("Debug info")`       |
| `document.cookie` | Access cookies of the current page        | `console.log(document.cookie)`    |
| `eval()` ⚠️       | Executes a string as code (⚠️ Dangerous!) | `eval("alert('This is unsafe')")` |

#### ✅ 2. DOM Manipulation

JavaScript can read or change HTML elements using **DOM methods**.

### ▶️ Common DOM Methods:

#### Accessing Elements:

```
document.getElementById("myElement"); document.querySelector(".class"); // CSS selector document.querySelectorAll("p");   // All <p> elements`
```
#### Modifying Elements:
```
document.getElementById("myElement").innerHTML = "New content"; // ⚠️XSS risk document.getElementById("myElement").textContent = "Safe text"; // ✅ safer
```

#### Modifying Style or Attributes:

```
let btn = document.getElementById("submitBtn"); btn.style.color = "red"; btn.setAttribute("disabled", true);
```


## ✅ 3. JavaScript Events

Events are how JavaScript **responds to user actions** like clicks or mouse movement.

|Event|Triggered when...|Example|
|---|---|---|
|`onclick`|Element is clicked|`<button onclick="sayHi()">Click</button>`|
|`onmouseover`|Mouse hovers over an element|`<div onmouseover="hoverEffect()">`|
|`onload`|Page finishes loading|`<body onload="initPage()">`|

### Event Listener (JavaScript way):

```
let btn = document.getElementById("btn");
btn.addEventListener("click", function() {
	alert("Button clicked!");
})
```

## ✅ 4. Scope and Variable Injection

### ▶️ JavaScript Scope

- **Global Scope**: Variables declared outside a function.
- **Function/Local Scope**: Variables declared within a function.
- **Block Scope**: Declared with `let` or `const` inside `{}`.

Example:

```
let globalVar = "I'm global"; 

function myFunction() { 
	let localVar = "I'm local";
	console.log(globalVar); // ✅ Accessible 
	console.log(localVar); // ✅ Accessible 
}

console.log(localVar); // ❌ Error: not defined
```

### ❗ Variable Injection (Security Risk)

If developers use dangerous functions like `eval()` or set innerHTML with untrusted data, attackers can inject malicious code (a common **XSS attack** vector).

#### ❌ Bad: innerHTML used unsafely

```
let userInput = "<img src=x onerror=alert('XSS')>"; document.getElementById("output").innerHTML = userInput;
```

#### ✅ Good: use textContent or sanitize

```
document.getElementById("output").textContent = userInput;
```

## ✅ Summary Table

| Concept               | Example                                 |
| --------------------- | --------------------------------------- |
| Alert popup           | `alert("Hello!")`                       |
| Console logging       | `console.log("Debug")`                  |
| Read cookie           | `document.cookie`                       |
| Get element by ID     | `document.getElementById("id")`         |
| Change content        | `element.innerHTML = "text"` ⚠️         |
| Event: Click          | `<button onclick="doSomething()">`      |
| Add JS event listener | `element.addEventListener('click', fn)` |
| Global vs Local scope | `let` inside and outside functions      |
| fAvoid `eval()`       | Use safer alternatives                  |
