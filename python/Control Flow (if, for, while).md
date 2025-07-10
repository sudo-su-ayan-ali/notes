# 🧠 Control Flow (if, for, while)

### 🔹 1. `if` Statement (Conditional Execution)

**Syntax:**

```bash
if [ condition ]; then
    # commands
elif [ another_condition ]; then
    # other commands
else
    # fallback commands
fi
```

**Example:**

```bash
#!/bin/bash
echo "Enter a number:"
read num

if [ "$num" -gt 0 ]; then
    echo "Positive"
elif [ "$num" -lt 0 ]; then
    echo "Negative"
else
    echo "Zero"
fi
```

---

### 🔹 2. `for` Loop (Iterating Over a List)

**Syntax:**

```bash
for item in list; do
    # commands
done
```

**Example:**

```bash
#!/bin/bash
for i in 1 2 3 4 5; do
    echo "Loop iteration $i"
done
```

**Example with range:**

```bash
for i in {1..5}; do
    echo "Number $i"
done
```

---

### 🔹 3. `while` Loop (Runs While Condition is True)

**Syntax:**

```bash
while [ condition ]; do
    # commands
done
```

**Example:**

```bash
#!/bin/bash
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

---

### 🧠 Bonus: Infinite Loop + Break

**Example:**

```bash
#!/bin/bash
while true; do
    read -p "Type 'exit' to quit: " input
    if [ "$input" == "exit" ]; then
        break
    fi
done
```

