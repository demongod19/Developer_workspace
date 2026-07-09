# Day 07 - Functions in Python

## What is a Function?

A function is a block of reusable code that performs a specific task. Instead of writing the same code multiple times, we can write it once inside a function and call it whenever needed.

### Syntax

```python
def function_name(parameters):
    # code
    return value
```

---

## Parts of a Function

### 1. Function Definition

```python
def greet():
    print("Hello")
```

### 2. Function Call

```python
greet()
```

Output

```
Hello
```

---

## Function with Parameters

Parameters allow us to pass values into a function.

Example

```python
def square(number):
    return number * number

num = int(input("Enter a number: "))
result = square(num)

print(result)
```

Output

```
Enter a number: 8
64
```

---

## Function with Multiple Parameters

```python
def area(length, width):
    return length * width

length = int(input("Enter length: "))
width = int(input("Enter width: "))

print(area(length, width))
```

Output

```
30
```

---

## Return Statement

The `return` keyword sends a value back to the place where the function was called.

Example

```python
def add(a, b):
    return a + b

result = add(5, 6)

print(result)
```

Output

```
11
```

---

## Why use Functions?

- Reuse code
- Reduce repetition
- Easy to debug
- Easy to maintain
- Makes code organized

---

# Project 1 - Largest Number

```python
def largest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = largest_number(a, b, c)

print("Largest number is:", result)
```

Sample Output

```
Enter first number: 5
Enter second number: 8
Enter third number: 2

Largest number is: 8
```

---

# Project 2 - Calculator using Functions

```python
def calculator(a, b, operation):

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":

        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed."

    else:
        return "Invalid Operation"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

result = calculator(a, b, operation)

print(result)
```

Example

```
Enter first number: 5
Enter second number: 6
Enter operation: add

11
```

---

# Common Mistakes

### Forgetting to call the function

Wrong

```python
def add(a, b):
    return a + b
```

Correct

```python
result = add(5, 6)
print(result)
```

---

### Forgetting to return

Wrong

```python
def square(n):
    n * n
```

Correct

```python
def square(n):
    return n * n
```

---

### Using variables without taking input

Wrong

```python
largest_number(a, b, c)
```

Correct

```python
a = int(input())
b = int(input())
c = int(input())

largest_number(a, b, c)
```

---

# Real-Life Uses of Functions

- Login System
- ATM Machine
- Calculator
- Banking Applications
- Password Generator
- Student Management System
- Expense Tracker
- File Organizer
- Web APIs

---

# Interview Questions

### What is a function?

A function is a reusable block of code that performs a specific task.

---

### Difference between Parameter and Argument

Parameter

```python
def add(a, b):
```

Argument

```python
add(5, 6)
```

---

### What is return?

The `return` statement sends a value back to the caller.

---

### Can a function return multiple values?

Yes.

```python
def numbers():
    return 10, 20

a, b = numbers()
```

---

# Commands Used Today

```powershell
cd Day07
python practice.py
```

---

# Day 07 Summary

Today I learned:

- Functions
- Function Definition
- Function Calling
- Parameters
- Arguments
- Return Statement
- Multiple Parameters
- Building reusable code
- Largest Number Program
- Calculator using Functions
