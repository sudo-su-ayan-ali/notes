## 1️⃣ If / Else: Decisions

This is the “choose your adventure” part.

```bash
#!/bin/bash

if [ $USER == "root" ]; then
    echo "Welcome, almighty Root. You have full power."
else
    echo "Access limited. Normal mortal detected."
fi
```

- `[ condition ]` → test something.
- `==` → equals.
- `-eq, -lt, -gt` → equal, less than, greater than (for numbers).

Example with numbers:

```bash
x=5
if [ $x -gt 3 ]; then
    echo "$x is greater than 3"
else
    echo "$x is 3 or less"
fi
```

---
## 2️⃣ Else If: Multiple Conditions

```bash
#!/bin/bash

read -p "Enter a secret code: " code
if [ "$code" == "123" ]; then
    echo "Door unlocked 🚪"
elif [ "$code" == "007" ]; then
    echo "Welcome, Mr. Bond 🕶️"
else
```

---
## 3️⃣ Loops: Repetition

Loops let your script _keep doing stuff until told to stop_.

### For Loop

Repeats a fixed number of times:

```bash
for i in {1..5}
do
    echo "Hack attempt #$i"
done
```

Output:

text

```
Hack attempt #1  
Hack attempt #2  
...  
Hack attempt #5
```

---
### While Loop

Repeats **while** the condition is true:

Bash

```
count=1
while [ $count -le 3 ]
do
    echo "Looping... ($count)"
    ((count++))
done
```

Output:

text

```
Looping... (1)
Looping... (2)
Looping... (3)
```

---
### Until Loop

Opposite of `while`: keeps looping **until** condition becomes true.

```bash
number=1
until [ $number -gt 3 ]
do
    echo "Number = $number"
    ((number++))
done
```

---
## 4️⃣ Case Statement: Switchboard of Options

Instead of a mess of `if... elif... elif...` you can use `case`.

```bash
#!/bin/bash

read -p "Choose [start/stop/restart]: " action

case $action in
    start)
        echo "System starting..."
        ;;
    stop)
        echo "System stopping..."
        ;;
restart)
        echo "System rebooting..."
        ;;
    *)
        echo "Unknown command!"
        ;;
esac
```

---

### ⚡ Summary 

- **if / else** → decisions.
- **elif** → extra conditions.
- **for** → repeat over items or numbers.
- **while / until** → keep looping by condition.
- **case** → cleaner menu-style branching.

---

