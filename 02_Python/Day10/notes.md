# Day 10 - Tuples, Sets, File Handling & Exception Handling

**Date:** 12-07-2026

---

# Topics Covered

- Tuples
- Sets
- File Handling
- Reading Files
- Exception Handling
- try-except

---

# 1. Tuples

A tuple is an ordered collection of elements.

Tuples are **immutable**, meaning their values cannot be changed after creation.

## Syntax

```python
electronics = ("Laptop", "Mouse", "Keyboard", "Monitor")
```

## Accessing Elements

```python
print(electronics)
print(electronics[0])
print(electronics[3])
```

### Output

```
('Laptop', 'Mouse', 'Keyboard', 'Monitor')
Laptop
Monitor
```

### Characteristics

- Ordered
- Immutable
- Allows duplicate values
- Indexed

---

# 2. Sets

A set is an unordered collection of unique elements.

## Syntax

```python
languages = {"Python", "Java", "C++", "JavaScript", "Python", "Java"}
print(languages)
```

### Output

```
{'Python', 'Java', 'C++', 'JavaScript'}
```

Notice that duplicate values are removed automatically.

### Characteristics

- Unordered
- Mutable
- No duplicate values
- Fast searching

---

# Tuple vs Set

| Tuple | Set |
|--------|-----|
| Ordered | Unordered |
| Immutable | Mutable |
| Allows duplicates | No duplicates |
| Uses () | Uses {} |

---

# 3. File Handling

File handling is used to read from and write to files.

## Opening a File

```python
file = open("notes.txt", "r")
```

## Reading a File

```python
print(file.read())
```

## Closing a File

```python
file.close()
```

---

## Recommended Method

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

Advantages:

- Automatically closes the file
- Cleaner code
- Recommended for professional programming

---

# File Modes

| Mode | Meaning |
|------|----------|
| r | Read |
| w | Write (overwrites file) |
| a | Append |
| x | Create new file |

---

# Example

### notes.txt

```
Hello Pratik
Python is awesome!
```

### Output

```
Hello Pratik
Python is awesome!
```

---

# 4. Exception Handling

Exception handling prevents a program from crashing when an error occurs.

## Syntax

```python
try:
    # code
except ErrorType:
    # handling code
```

---

## Example

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### Output

```
Enter first number: 8
Enter second number: 0

Cannot divide by zero.
```

---

## Handling Invalid Input

```python
try:
    number = int(input())

except ValueError:
    print("Enter numbers only.")
```

---

# Errors Learned Today

## ZeroDivisionError

Occurs when dividing by zero.

Example

```python
10 / 0
```

---

## ValueError

Occurs when invalid input is entered.

Example

```python
int("Hello")
```

---

# Important Points

### Tuple

- Ordered
- Immutable
- Indexed
- Allows duplicates

### Set

- Unordered
- Mutable
- Stores only unique values

### File Handling

- open()
- read()
- close()
- with open()

### Exception Handling

- try
- except
- ZeroDivisionError
- ValueError

---

# Commands I Used Today

```bash
python practice.py
```

---

# One New Thing I Discovered

- Tuples cannot be modified after creation.
- Sets automatically remove duplicate values.
- File handling allows reading data from text files.
- The `with open()` statement automatically closes files.
- Exception handling makes programs more reliable by preventing crashes.

---

# Interview Questions

### 1. What is a tuple?

A tuple is an ordered and immutable collection of elements.

---

### 2. Can tuples be modified?

No.

---

### 3. What is a set?

A set is an unordered collection of unique elements.

---

### 4. Why are duplicate values removed in a set?

Because a set stores only unique values.

---

### 5. What is file handling?

File handling is the process of reading from and writing to files.

---

### 6. What are the file modes?

- r → Read
- w → Write
- a → Append
- x → Create

---

### 7. Why should we use `with open()`?

Because it automatically closes the file after use.

---

### 8. What is exception handling?

It is a mechanism for handling runtime errors without stopping the program.

---

### 9. What is ZeroDivisionError?

An error that occurs when dividing by zero.

---

### 10. What is ValueError?

An error that occurs when an invalid value is provided, such as converting text into an integer.

---

# Today's Progress

- ✅ Learned Tuples
- ✅ Learned Sets
- ✅ Learned File Handling
- ✅ Read data from text files
- ✅ Learned Exception Handling using try-except
- ✅ Understood common runtime errors

---

# Git Commit

```bash
git add .
git commit -m "Day 10: Learned tuples, sets, file handling and exception handling"
git push
```