# 🧠  Variables & Data Types
## 🔹 What is a Variable?

A **variable** is a name that stores a value. You can think of it like a container that holds data.

### Example in Python:

```python
name = "Alice"
age = 20
is_student = True
```

Here:

* `name` holds a **string**
* `age` holds an **integer**
* `is_student` holds a **boolean**

---

## 🔹 What is a Data Type?

A **data type** defines the kind of value a variable can hold.

### 🔸 Common Data Types in Python:

| Data Type  | Example         | Description                  |
| ---------- | --------------- | ---------------------------- |
| `int`      | `10`, `-5`, `0` | Integer numbers              |
| `float`    | `3.14`, `-0.5`  | Decimal numbers              |
| `str`      | `"hello"`       | Text (string of characters)  |
| `bool`     | `True`, `False` | Boolean (true or false)      |
| `list`     | `[1, 2, 3]`     | Ordered collection           |
| `tuple`    | `(1, 2, 3)`     | Immutable ordered collection |
| `dict`     | `{"a": 1}`      | Key-value pairs (dictionary) |
| `set`      | `{1, 2, 3}`     | Unordered unique collection  |
| `NoneType` | `None`          | Represents no value          |

---

## 🔹 Declaring Variables (Python Style)

```python
x = 5            # int
y = 3.14         # float
name = "John"    # str
is_cool = True   # bool
```

---

## 🔹 How to Check the Data Type

Use the `type()` function:

```python
print(type(x))        # <class 'int'>
print(type(name))     # <class 'str'>
```

---

## 🔹 Rules for Naming Variables

✅ Must start with a letter or underscore (`_`)
✅ Can include letters, numbers, and underscores
❌ Cannot start with a number
❌ Cannot use reserved keywords (like `if`, `for`, etc.)

---

## 🧠 Mini Practice

```python
city = "Delhi"
population = 32000000
is_capital = True

print(type(city))        # str
print(type(population))  # int
print(type(is_capital))  # bool
```

---

Would you like a **PDF cheat sheet** or **interactive quiz** on variables and data types?
