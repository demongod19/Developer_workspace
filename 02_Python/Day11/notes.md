# 📅 Day 11 – Object-Oriented Programming (OOP) Basics

## 🎯 Topics Covered
- Introduction to Object-Oriented Programming
- Class and Object
- Constructor (`__init__`)
- `self` Keyword
- Attributes
- Methods
- Creating Multiple Objects
- Real-life OOP Examples

---

# What I Learned Today

## 1. Class
A class is a blueprint or template used to create objects.

Example:
```python
class Laptop:
    pass
```

---

## 2. Object
An object is an instance of a class.

Example:
```python
laptop1 = Laptop()
laptop2 = Laptop()
```

Each object has its own data.

---

## 3. Constructor (`__init__`)
The constructor is automatically called whenever an object is created.

Example:

```python
class Laptop:
    def __init__(self, brand, ram, model):
        self.brand = brand
        self.ram = ram
        self.model = model
```

---

## 4. self Keyword

`self` refers to the current object.

Example:

```python
self.brand = brand
```

Here,

self.brand belongs to the object.

---

## 5. Attributes

Attributes are variables that belong to an object.

Example:

```python
self.brand
self.ram
self.model
```

Every object stores its own attributes.

---

## 6. Methods

Methods are functions inside a class.

Example:

```python
def display_info(self):
    print(self.brand)
```

Methods define the behavior of an object.

---

## 7. Multiple Objects

Example:

```python
laptop1 = Laptop("Dell",16,"Inspiron 15")
laptop2 = Laptop("HP",8,"Pavilion 14")
```

Output:

Laptop 1
Brand : Dell

Laptop 2
Brand : HP

Both objects have different data even though they belong to the same class.

---

# Programs Practiced Today

## Program 1
Laptop Class

- Brand
- RAM
- Model
- display_info()

---

## Program 2
Mobile Class

Attributes

- Company
- Model
- Price

Method

- display_info()

Created two mobile objects.

---

## Program 3
Bank Account Class

Attributes

- Account Number
- Account Holder
- Balance

Methods

- deposit()
- withdraw()
- display_info()

Concepts learned

- Updating object attributes
- Validation using if statements
- Multiple bank accounts

---

# Real-Life Examples

Class → Student

Objects

Rahul

Pratik

Aman

Each student has

Name

PRN

Branch

CGPA

---

Class → Car

Objects

BMW

Audi

Mercedes

Each object has

Brand

Model

Price

Color

---

Class → Bank Account

Objects

Pratik Account

Rahul Account

Each account has

Account Number

Balance

Holder Name

---

# Interview Questions

## Q1. What is OOP?

Object-Oriented Programming is a programming paradigm that organizes code using classes and objects.

---

## Q2. What is a class?

A blueprint used to create objects.

---

## Q3. What is an object?

An instance of a class.

---

## Q4. What is a constructor?

A special method (`__init__`) that automatically runs when an object is created.

---

## Q5. Why do we use self?

It refers to the current object and allows access to its own attributes and methods.

---

## Q6. What are attributes?

Variables that belong to an object.

---

## Q7. What are methods?

Functions defined inside a class.

---

## Q8. Can two objects have different values?

Yes.

Example:

Laptop1

RAM = 16GB

Laptop2

RAM = 8GB

Each object stores its own data.

---

# Commands Used Today

```bash
python practice.py

git add .

git commit -m "Day 11: Learned Python OOP Basics"

git push origin master
```

---

# One New Thing I Discovered

Using classes allows us to organize code into reusable objects. Each object has its own attributes and methods, making programs easier to manage and closer to real-world scenarios.

---

# Questions I Still Have

- What is inheritance?
- What is polymorphism?
- When should I use classes instead of functions?
- What is encapsulation?

---

# Today's Mini Project

Bank Account System

Features

- Create multiple accounts
- Deposit money
- Withdraw money
- Display account details
- Balance validation

---

# Today's Progress

✅ Learned Object-Oriented Programming

✅ Understood Classes and Objects

✅ Used Constructors

✅ Learned self keyword

✅ Created Multiple Objects

✅ Built Laptop Class

✅ Built Mobile Class

✅ Built Bank Account Class

---

# Difficulty Level

⭐⭐⭐⭐☆ (4/5)

OOP was a new concept, but practicing with real-life examples made it much easier to understand.