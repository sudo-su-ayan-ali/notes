## ✅ **1. JavaScript Basics**
### 📌 Script Tags (in HTML)
To use JavaScript in HTML, we use the `<script>` tag.

```html
<script>
  alert("Hello, JavaScript!");
</script>
```

You can also link external JS files:

```html
<script src="script.js"></script>
```

---

## ✅ **2. JavaScript Data Types**
### Primitive Data Types:
| Type       | Example              |
|------------|----------------------|
| String     | `"Hello World"`      |
| Number     | `123`, `3.14`        |
| Boolean    | `true`, `false`      |
| Null       | `null`               |
| Undefined  | `undefined`          |
| Symbol     | `Symbol("id")`       |
| BigInt     | `123n`               |

### Non-Primitive:
- **Object**: Collection of key/value pairs.

```javascript
const person = {
  name: "Alice",
  age: 25
};
```

- **Array**: Ordered collection.

```javascript
const fruits = ["Apple", "Banana", "Mango"];
```

---

## ✅ **3. Variables**
Used to store data values.

```javascript
let x = 5;
const pi = 3.14;
var name = "John";
```

| Keyword | Scope       | Reassignment | Usage                      |
|---------|-------------|--------------|----------------------------|
| `var`   | Function     | Yes          | Old way, avoid in modern JS |
| `let`   | Block        | Yes          | Preferred for mutable vars |
| `const` | Block        | No           | Preferred for constants   |

---

## ✅ **4. Operators**
### Arithmetic:
`+`, `-`, `*`, `/`, `%`, `**`

### Comparison:
`==`, `!=`, `===`, `!==`, `<`, `>`, `<=`, `>=`

### Logical:
`&&`, `||`, `!`

### Assignment:
`=`, `+=`, `-=`, `*=` etc.

### Other:
`typeof`, `instanceof`, `delete`, `in`

---

## ✅ **5. Control Structures**
### Conditional Statements:

```javascript
if (condition) {
  // code
} else if (another) {
  // code
} else {
  // code
}
```

### Switch:

```javascript
switch (value) {
  case 1:
    break;
  default:
    break;
}
```

### Ternary Operator:

```javascript
let result = age > 18 ? "Adult" : "Minor";
```

---

## ✅ **6. Loops**
### For Loop:
```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

### While Loop:
```javascript
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}
```

### Do...While:
```javascript
do {
  console.log(i);
  i++;
} while (i < 5);
```

### For...of (used with arrays):
```javascript
for (let fruit of fruits) {
  console.log(fruit);
}
```

### For...in (used with objects):
```javascript
for (let key in person) {
  console.log(key, person[key]);
}
```

---

## ✅ **7. Functions**
### Regular Function:
```javascript
function add(a, b) {
  return a + b;
}
```

### Arrow Function:
```javascript
const add = (a, b) => a + b;
```

### Anonymous Function:
```javascript
const greet = function () {
  console.log("Hi");
};
```

---

## ✅ **8. JavaScript Objects**
Used for storing keyed collections.

```javascript
const car = {
  brand: "Toyota",
  year: 2024,
  start: function () {
    console.log("Starting car...");
  }
};
```

---

## ✅ **9. Arrays & Methods**
### Creating Array:
```javascript
const colors = ["Red", "Green", "Blue"];
```

### Common array methods:
- `push()`, `pop()`, `shift()`, `unshift()`
- `map()`, `filter()`, `reduce()`
- `forEach()`, `indexOf()`, `includes()`
- `sort()`, `reverse()`, `slice()`, `splice()`

---

## ✅ **10. Events**
Handling user interactions.

```javascript
<button onclick="greet()">Click Me</button>

<script>
function greet() {
  alert("Hello!");
}
</script>
```

Or using `addEventListener`:

```javascript
document.getElementById("myBtn").addEventListener("click", greet);
```

---

## ✅ **11. DOM Manipulation**
DOM = Document Object Model

### Selecting elements:
```javascript
document.getElementById("id")
document.querySelector(".class")
document.querySelectorAll("p")
```

### Changing content/style/attribute:
```javascript
element.innerHTML = "New Text";
element.style.color = "red";
element.setAttribute("href", "https://google.com");
```

---

## ✅ **12. Error Handling**
```javascript
try {
  // code
} catch (error) {
  console.error(error);
} finally {
  // always run
}
```

---

## ✅ **13. Promise, Async/Await**
### Promise:
```javascript
let promise = new Promise((resolve, reject) => {
  resolve("Done!");
});

promise.then(res => console.log(res));
```

### Async/Await:
```javascript
async function getData() {
  let data = await fetch(url);
  let result = await data.json();
}
```

---

## ✅ **14. Classes (ES6)**
```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} speaks.`);
  }
}
```

Inheritance:

```javascript
class Dog extends Animal {
  speak() {
    console.log(`${this.name} barks.`);
  }
}
```

---

## ✅ **15. Useful JS APIs**
- `fetch()` – HTTP requests
- `localStorage`, `sessionStorage` – store data in browser
- `setTimeout`, `setInterval` – timers
- `Math`, `Date` – built-in objects
- `JSON.stringify`, `JSON.parse`

---

## ✅ **16. Modern JavaScript (ES6+) Features**
- **Template literals**: `` `Hello ${name}` ``
- **Destructuring**: `let {a, b} = obj;`
- **Spread/Rest**: `...args`
- **Modules**:
```javascript
// moduleA.js
export function greet() { ... }

// main.js
import { greet } from './moduleA.js';
```

---

## ✅ Summary Table of Key JS Concepts

| Category          | Examples                                |
|-------------------|-----------------------------------------|
| Data Types        | String, Number, Object, Array, Boolean  |
| Variable Keywords | `var`, `let`, `const`                   |
| Control Flow      | `if`, `switch`, `for`, `while`          |
| Functions         | Regular, Arrow, Anonymous               |
| Objects           | `{ key: value }`                        |
| Array Methods     | `.push()`, `.map()`, `.filter()`        |
| DOM               | `.getElementById()`, `.innerHTML`       |
| Events            | `onclick`, `addEventListener()`         |
| Asynchronous      | `setTimeout`, Promises, `async/await`   |

---

