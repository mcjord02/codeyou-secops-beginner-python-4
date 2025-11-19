# 🧮 **Week 4: Loops and Iteration – “Automating Repetition for Security Tasks”**

### **Learning Objectives**

By the end of this week, students will be able to:

1. Understand and use `for` and `while` loops effectively.
2. Loop through lists and perform conditional checks on each item.
3. Use loops to process structured security data (like IP addresses).
4. Begin thinking about efficiency and automation in repetitive security workflows.

---

## 🧩 **Lecture & Demo Overview**

| Concept                   | Description                           | Short Demo Example                   |
| ------------------------- | ------------------------------------- | ------------------------------------ |
| **`for` loops**           | Iterate over a list or range of items | `for i in range(5): print(i)`        |
| **`while` loops**         | Repeat while a condition is true      | `while x < 5: x += 1`                |
| **Loop control keywords** | `break`, `continue`, `pass`           | Demonstrate skipping or stopping     |
| **Nested loops**          | Loops inside loops (simple intro)     | Example: iterate users × permissions |
| **Lists and iteration**   | How lists connect to loops            | Show looping over list of IPs        |

---

## 🧰 **Walkthrough Exercise: “Filtering IP Addresses”**

> **Scenario:**
> As a junior SOC analyst, you’ve been given a list of IP addresses from network logs.
> Your task is to identify which ones are **internal** (private) vs. **external** addresses.

### **Step 1 – Starter Code**

```python
# Week 4: Loops and Iteration
# Goal: Identify internal vs external IP addresses

ip_addresses = [
    "192.168.1.25",
    "10.0.0.8",
    "172.16.5.14",
    "8.8.8.8",
    "172.15.3.2"
]

for ip in ip_addresses:
    print(ip)
```

Ask students: *“What does this do?”*
Then discuss how we can use `if` statements inside loops to classify.

---

### **Step 2 – Add Conditional Checks**

```python
for ip in ip_addresses:
    if ip.startswith("192.168.") or ip.startswith("10."):
        print(f"{ip} is an internal address.")
    else:
        print(f"{ip} is an external address.")
```

🧠 **Teaching Moment:**
Explain what `.startswith()` does and why this is an example of automation — imagine having to do this manually for hundreds of log entries.

---

### **Step 3 – Extend to Handle More Cases**

```python
for ip in ip_addresses:
    if ip.startswith("192.168."):
        zone = "Private (Class C)"
    elif ip.startswith("10."):
        zone = "Private (Class A)"
    elif ip.startswith("172.16.") or ip.startswith("172.17.") or ip.startswith("172.31."):
        zone = "Private (Class B)"
    else:
        zone = "Public"

    print(f"{ip} → {zone}")
```

This introduces **elif** and more structured logic.

---

### **Step 4 – While Loop Challenge**

Have students convert part of this logic to a `while` loop for practice.

Example:

```python
index = 0
while index < len(ip_addresses):
    ip = ip_addresses[index]

    if ip.startswith(("192.168.", "10.")):
        print(f"{ip} is internal.")
    else:
        print(f"{ip} is external.")

    index += 1
```

---

## 💻 **Challenge Tasks**

### **Challenge 1 – Count Internal vs External**

Add counters to determine how many internal and external IPs are in the list.

**Hint:**
Use two variables — `internal_count` and `external_count` — and increment inside the loop.

Output example:

```
Internal: 3
External: 2
```

---

### **Challenge 2 – Store Results in New Lists**

Create two lists: `internal_ips` and `external_ips`, then append items during iteration.

**Stretch:** Print the total and show the lists at the end.

---

### **Challenge 3 – Looping from User Input**

Allow the user to type IP addresses until they type `done`, then classify each.

Example:

```
Enter an IP (or 'done' to finish): 192.168.2.5
192.168.2.5 is internal.
Enter an IP (or 'done' to finish): 8.8.8.8
8.8.8.8 is external.
Enter an IP (or 'done' to finish): done
```

This reinforces the *“while loop until condition”* concept interactively.

---

## 🧠 **Reflection & Discussion**

* Why might a SOC analyst need to separate internal vs external traffic?
* What mistakes could happen if this script were written incorrectly?
* How could this scale to a file with thousands of IPs?

---

## 🧩 **Optional Advanced Task (for faster students)**

Read IPs from a text file and write results to another file.

```python
with open("ips.txt") as f:
    ip_addresses = f.read().splitlines()

internal_ips = []

for ip in ip_addresses:
    if ip.startswith(("192.168.", "10.")):
        internal_ips.append(ip)

with open("internal_ips.txt", "w") as out:
    for ip in internal_ips:
        out.write(ip + "\n")
```

---

## 📄 **Deliverables**

Students should submit:

1. Their Python script (`loops_ips.py`).
2. Screenshot or copy of successful run output.
3. 2–3 sentence reflection on what loops made easier.

---

## 🧾 **Rubric (20 points)**

| Category                  | Points | Criteria                                    |
| ------------------------- | ------ | ------------------------------------------- |
| Correct use of `for` loop | 5      | Loops through all items                     |
| Correct conditional logic | 5      | Correctly identifies internal vs external   |
| Code organization         | 5      | Readable, uses comments                     |
| Reflection / explanation  | 5      | Shows understanding of why loops are useful |
