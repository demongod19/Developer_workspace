# 📅 Day 12 – Inheritance in Python

## 🎯 Topics Covered
- Inheritance
- Parent Class
- Child Class
- `super()` Function
- Method Inheritance
- Constructor Inheritance
- Method Overriding
- Employee Management System
- Savings Account System

---

# What I Learned Today

## 1. Inheritance

Inheritance is an OOP concept where one class acquires the properties and methods of another class.

It helps us reuse existing code instead of writing it again.

Syntax:

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

## 2. Parent Class

A parent class (Base Class) is the class whose properties and methods are inherited.

Example:

```python
class Employee:
    pass
```

---

## 3. Child Class

A child class inherits all the properties and methods from the parent class.

Example:

```python
class Manager(Employee):
    pass
```

The Manager class can use everything inside Employee.

---

## 4. Constructor Inheritance

The child class can reuse the constructor of the parent class.

Example:

```python
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
```

Child class:

```python
class Manager(Employee):

    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
```

---

## 5. super() Function

`super()` is used to call the parent class constructor or methods.

Example:

```python
super().__init__(name, age, salary)
```

Benefits:

- Reuses parent code
- Avoids duplicate code
- Makes programs easier to maintain

---

## 6. Method Inheritance

The child class automatically inherits methods from the parent class.

Example:

```python
employee.display_info()
manager.display_info()
```

If the method exists in the parent class, the child can use it directly.

---

## 7. Method Overriding

A child class can redefine a method from the parent class.

Example:

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")
```

The child's version replaces the parent's version.

---

# Programs Practiced Today

## Program 1

Animal → Dog

Concept:

- Basic Inheritance

---

## Program 2

Person → Student

Concept:

- Parent Method
- Child Method

---

## Program 3

Vehicle → Car

Concept:

- Constructor Inheritance

---

## Program 4

Employee → Manager

Concepts:

- Constructor Inheritance
- super()
- display_info()

---

## Program 5

BankAccount → SavingsAccount

Concepts:

- Inheritance
- Deposit
- Withdraw
- Interest Calculation
- Method Reuse

---

# Mini Project

## Employee Management System

Parent Class

Employee

Attributes

- Name
- Age
- Salary

Method

- display_info()

Child Class

Manager

Additional Attribute

- Department

Used:

- Inheritance
- super()
- Method Reuse

Output:

```text
********** Employee Management System **********

========== Employee ==========
Name : Pratik
Age : 30
Salary : 90000
==============================

========== Employee ==========
Name : Alice Johnson
Age : 35
Salary : 100000
==============================

========== Manager ==========
Department : Marketing
==============================
```

---

# Challenge Completed

Savings Account System

Parent Class

BankAccount

Methods

- Deposit
- Withdraw
- Get Balance

Child Class

SavingsAccount

Additional Features

- Interest Rate
- Add Interest

Output

```text
Deposited: 500. New balance: 1500
```

---

# Real-Life Examples

### Person

Parent

Person

Children

- Student
- Teacher
- Doctor

---

### Vehicle

Parent

Vehicle

Children

- Car
- Bike
- Truck

---

### Animal

Parent

Animal

Children

- Dog
- Cat
- Lion

---

### Bank

Parent

BankAccount

Children

- Savings Account
- Current Account

---

# Interview Questions

## Q1. What is inheritance?

Inheritance is an OOP concept where one class acquires the properties and methods of another class.

---

## Q2. Why is inheritance used?

- Code Reusability
- Easy Maintenance
- Less Code Duplication
- Better Organization

---

## Q3. What is a Parent Class?

A class whose properties and methods are inherited.

---

## Q4. What is a Child Class?

A class that inherits another class.

---

## Q5. What is super()?

`super()` is used to call the parent class constructor or methods.

---

## Q6. What is Method Overriding?

Redefining a parent method inside the child class.

---

## Q7. Can a child class access parent methods?

Yes.

---

## Q8. What are the advantages of inheritance?

- Reusability
- Readability
- Less Duplication
- Easy Maintenance

---

## Q9. Give a real-life example of inheritance.

Vehicle → Car

Animal → Dog

Person → Student

BankAccount → SavingsAccount

---

# Commands Used Today

```bash
python practice.py

python Employee_management_system.py

git add .

git commit -m "Day 12: Learned Inheritance and super()"

git push origin master
```

---

# One New Thing I Discovered

Inheritance allows one class to reuse another class's code, making programs shorter, cleaner, and easier to maintain. The `super()` function is the correct way to initialize parent class attributes from a child class.

---

# Questions I Still Have

- What are the different types of inheritance?
- What is Multiple Inheritance?
- What is Method Resolution Order (MRO)?
- What is Polymorphism?

---

# Today's Progress

✅ Learned Inheritance

✅ Learned Parent and Child Classes

✅ Understood Constructor Inheritance

✅ Learned super()

✅ Understood Method Overriding

✅ Built Employee Management System

✅ Built Savings Account System

---

# Difficulty Level

⭐⭐⭐⭐☆ (4/5)

Inheritance introduced a new way of organizing programs. Understanding `super()` and parent-child relationships took some practice, but building real-world examples made the concept much clearer.